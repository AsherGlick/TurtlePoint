from typing import List
from point import Point
from build_waypoint_data import get_waypoint_data


################################################################################
# leaflet_export_paths
#
# Exports the paths passed in to a leaflet format using the continent
# coordinates so they can be rendered over top a live map. The path is colored
# so teleporting is red, walking is green, and the path of a portal is
# transparent purple.
################################################################################
def leaflet_export_paths(path: List[Point]) -> str:
    output_lines: List[str] = []
    previous_point = path[0]
    for point in path[1:]:
        if point.can_waypoint_teleport_to:
            output_lines.append(
                "L.polyline([unproject([{}, {}]), unproject([{}, {}])], {{color: '#FF0000'}}).addTo(map)".format(
                    previous_point.end_x,
                    previous_point.end_y,
                    point.x,
                    point.y
                )
            )
        else:
            output_lines.append(
                "L.polyline([unproject([{}, {}]), unproject([{}, {}])], {{color: '#00FF00'}}).addTo(map)".format(
                    previous_point.end_x,
                    previous_point.end_y,
                    point.x,
                    point.y
                )
            )
        if point.x != point.end_x or point.y != point.end_y:
            output_lines.append(
                "L.polyline([unproject([{}, {}]), unproject([{}, {}])], {{color: '#A020F080'}}).addTo(map)".format(
                    point.x,
                    point.y,
                    point.end_x,
                    point.end_y
                )
            )
        previous_point = point

    return "\n".join(output_lines)


################################################################################
# leaflet_export_waypoints
#
# Exports all of the waypoints as leaflet markers for all of the maps specified.
################################################################################
def leaflet_export_waypoints(maps: List[int]) -> str:
    # map_info_from_id(map_id: int):
    output_lines: List[str] = []
    for map_id in maps:
        waypoint_data = get_waypoint_data()[str(map_id)]
        for waypoint in waypoint_data:
            output_lines.append(
                "L.marker(unproject([{x}, {y}]), {{ title: \"{name}\" }}).addTo(map);".format(
                    x=waypoint["coord"][0],
                    y=waypoint["coord"][1],
                    name=waypoint["name"]
                )
            )

    return "\n".join(output_lines)



# def leaflet_export_portals() -> str:
#     pass