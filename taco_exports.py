import json
import os
from api_request import get_api_json
from typing import List, Tuple, Dict, Any
from point import Point
import struct


# TODO: use units.continent_to_meters() instead of this constant
# two feet to meters
feet_per_meter = 3.28084
map_to_ingame_scale = 1.64042 # feet_per_meter/2


# A helper type to represent an xyz vector as a tuple.
Vector3 = Tuple[float, float, float]


################################################################################
# convert_continent_point_to_ingame_point
#
# Take a 2d continent point and convert it an reposition it to an ingame 3d
# point with a default vertical height.
################################################################################
def convert_continent_point_to_ingame_point(
    continent_coordinate: Tuple[float, float],
    map_api: Any,
    default_height: float = 29
) -> Vector3:
    map_x = continent_coordinate[0]
    map_y = continent_coordinate[1]

    map_size = map_api["continent_rect"]
    map_origin_x = map_size[0][0]
    map_origin_y = map_size[0][1]

    map_size_x = map_size[1][0] - map_origin_x
    map_size_y = map_size[1][1] - map_origin_y

    map_offset_x = (map_api["map_rect"][1][0]+map_api["map_rect"][0][0]) / 24 / 2
    map_offset_y = (map_api["map_rect"][1][1]+map_api["map_rect"][0][1]) / 24 / 2

    ingame_x = (map_x - map_origin_x - map_size_x/2 + map_offset_x) / map_to_ingame_scale
    ingame_y = default_height
    ingame_z = (map_y - map_origin_y - map_size_y/2 - map_offset_y) / map_to_ingame_scale

    return(ingame_x, ingame_y, -ingame_z)


################################################################################
# search_for_map
#
# A helper function to figure out which map a particular point is in
################################################################################
def search_for_map(point: Tuple[float, float], map_data: Dict[int, Any]) -> int:
    for map_id, map_value in map_data.items():
        if within_bounds(point, map_value["continent_rect"]):
            return map_id

    raise ValueError("Map id not found for point".format(point))


################################################################################
# within_bounds
#
# A helper function used to determine if a specific point is within the bounds
# of a box defined by two a top left corner and a bottom right corner point.
################################################################################
def within_bounds(
    point: Tuple[float, float],
    bounds: Tuple[Tuple[float, float], Tuple[float, float]]
):
    return (
        bounds[0][0] < point[0]
        and point[0] < bounds[1][0]
        and bounds[0][1] < point[1]
        and point[1] < bounds[1][1]
    )


################################################################################
# export_taco
#
# Takes all of the points, and output folder, and a list of all the map ids
# we care about. Then writes data to the output folder to create a taco marker
# pack from the list of points given.
################################################################################
def export_taco(points: List[Point], folder: str, map_ids: List[int]):
    map_data: Dict = {}
    for map_id in map_ids:
       map_data[map_id] = get_api_json("https://api.guildwars2.com/v2/maps/{map_id}".format(map_id=map_id))


    current_map = search_for_map((points[0].x, points[0].y), map_data)
    current_map_bounds = map_data[current_map]["continent_rect"]
    current_path: List[Vector3] = []
    paths: List[Tuple[int, List[Vector3]]] = []

    for point in points:

        if not within_bounds((point.x, point.y), current_map_bounds):
            raise ValueError("Unexpected map jump")

        current_path.append(convert_continent_point_to_ingame_point(
            (point.x, point.y),
            map_data[current_map])
        )

        # This is a split in the paths
        if point.x != point.end_x or point.y != point.end_y:
            paths.append((current_map, current_path))

            # print("splitting the path", len(current_path))

            current_map = search_for_map((point.end_x, point.end_y), map_data) 
            current_map_bounds = map_data[current_map]["continent_rect"]
            current_path = [convert_continent_point_to_ingame_point(
                (point.end_x, point.end_y),
                map_data[current_map]
            )]

    paths.append((current_map, current_path))

    trail_id = 0

    xml_output = ['<OverlayData><MarkerCategory name="a" DisplayName="IggyTurtle"/><POIs>']
    for trail_pair in paths:

        trail_filename = "{}.trl".format(trail_id)
        trail_path = os.path.join(folder, trail_filename)

        # write the .trl file
        with open(trail_path, 'wb') as f:
            f.write(struct.pack("<i", 0)) # Version
            f.write(struct.pack("<i", trail_pair[0]))

            for trail_point in trail_pair[1]:
                f.write(struct.pack("<fff", *trail_point))

        trail_id += 1


        xml_output.append('<Trail type="a" trailData="{}" texture="a.png"/>'.format(trail_filename))
    xml_output.append("</POIs></OverlayData>")

    with open(os.path.join(folder, "TurtlePoint.xml"), "w") as f:
        f.write("".join(xml_output))
