from build_waypoint_data import WaypointData
from typing import Tuple, List, Any, Optional, Dict, Generator
from build_portal_data import get_portal_data, get_portals_between, get_portal_by_id
import os
from segment import Segment
import hashlib
from leaflet_exports import export_leaflet
from map_info import MapInfo, central_tyria_map_ids
from subprocess import Popen, PIPE
import json
from itertools import product
from point import Point, PointPath
from taco_exports import export_taco


# This file will load all the things that need to be loaded
portal_data = get_portal_data()


################################################################################
# every_combination_between_zero_and
#
# Creates every combination of numbers between 0 and value exclusive. Does not
# repeat reversed combinations.
################################################################################
def every_combination_between_zero_and(value: int) -> Generator[Tuple[int, int], None, None]:
    first: int = 0
    second: int = 0
    while first < value:
        yield (first, second)
        second += 1
        if second == value:
            first += 1
            second = first


################################################################################
#
################################################################################
def get_shortest_path(
    start_point: Point,
    points_to_hit: List[Point],
    end_point: Optional[Point],
    map_id: int,
) -> PointPath:
    cachedir = os.path.join("shortpath_cache", str(map_id))
    os.makedirs(cachedir, exist_ok=True)

    points_to_hit = sorted(points_to_hit, key=lambda x: x.__repr__())

    args = start_point.to_arglist()
    for point in points_to_hit:
        args += point.to_arglist()

    if end_point is not None:
        args += end_point.to_arglist()
    else:
        args += ['v']

    argument_hash = hashlib.new('sha256')
    argument_hash.update(str(args).encode())
    # print(argument_hash.hexdigest())
    cachepath = os.path.join(cachedir, argument_hash.hexdigest() + ".json")

    data = {}
    if os.path.exists(cachepath):
        # print("   Using Cached Data - {}".format(cachepath))
        with open(cachepath, 'r') as f:
            data = json.load(f)
    else:
        process = Popen(["./TurtleRoute/route"] + args, stdout=PIPE)
        output, err = process.communicate()
        exit_code = process.wait()

        if exit_code != 0:
            pass  # TODO: Handle a nonzero exit code

        if len(err) != 0:
            pass  # TODO: Handle nonempty stderr

        print(output)
        data = json.loads(output)

        with open(cachepath, 'wb') as f:
            f.write(output)

    sorted_points: List[Point] = []
    # TODO: Sanity check the start point is the start point
    # TODO: Sanity check the end point is the end point

    sorted_points = [start_point] + find_point_from_reference(
        point_objects=points_to_hit,
        reference=data["points"][1:-1]
    )
    if end_point is not None:
        sorted_points.append(end_point)

    point_path = PointPath(
        walking_distance=data["walking_distance"],
        teleporting_cost=data["teleporting_cost"],
        points=sorted_points
    )

    return point_path


################################################################################
# TODO: better comment
# looks for exact points from the reference points
################################################################################
def find_point_from_reference(point_objects: List[Point], reference: List[Any]) -> List[Point]:
    out_points: List[Point] = []

    for reference_point in reference:
        found_point_object: Optional[Point] = None
        for point_object in point_objects:
            if (
                reference_point["x"] == point_object.x
                and reference_point["y"] == point_object.y
                and reference_point["id"] == point_object.identifier
                and reference_point["exit_x"] == point_object.end_x
                and reference_point["exit_y"] == point_object.end_y
            ):
                if found_point_object is None:
                    found_point_object = point_object
                else:
                    print("Duplicate Point Objects found", found_point_object, point_object)

        if found_point_object is None:
            print("    Did not find a point object for", reference_point)
            for point in point_objects:
                print("       - ", point)
        else:
            out_points.append(found_point_object)

    return out_points


################################################################################
#
################################################################################
def get_shortest_path_through_map(
    previous_map: MapInfo,
    current_map: MapInfo,
    next_map: Optional[MapInfo],
    additional_points: List[List[Point]],
    waypoint_data: Dict[str, List[WaypointData]]
) -> List[PointPath]:

    waypoints: List[Point] = []
    for point in waypoint_data[str(current_map.i)]:
        waypoints.append(Point(
            point["coord"][0],
            point["coord"][1],
            point["name"],
            is_optional=point["optional"],
        ))

    combinations = [list(comb) for comb in product(*additional_points)]

    out_points: List[PointPath] = []

    start_portals = get_portals_between(previous_map, current_map)
    if next_map is not None:
        end_portals = get_portals_between(current_map, next_map)

        for start_portal in start_portals:
            for end_portal in end_portals:
                start = start_portal.get_point_in_map(current_map)
                end = end_portal.get_point_in_map(current_map)

                if len(combinations) > 0:
                    possible_paths: List[PointPath] = []
                    for combination in combinations:
                        possible_paths.append(get_shortest_path(
                            Point.from_portal_info(start),
                            waypoints + combination,
                            Point.from_portal_info(end),
                            current_map.i,
                        ))

                    out_points.append(get_shortest_point_path(possible_paths))
                else:
                    point_path = get_shortest_path(
                        Point.from_portal_info(start),
                        waypoints,
                        Point.from_portal_info(end),
                        current_map.i,
                    )
                    out_points.append(point_path)
    else:
        for start_portal in start_portals:

            start = start_portal.get_point_in_map(current_map)
            # TODO implement the "end anywhere" version
            point_path = get_shortest_path(
                Point.from_portal_info(start),
                waypoints,
                None,
                current_map.i,
            )
            out_points.append(point_path)

    return out_points


################################################################################
#
################################################################################
def get_shortest_path_through_maplist(
    segments: List[Segment],
    origin_map: MapInfo,
    destination_map: Optional[MapInfo],
    waypoint_data: Dict[str, List[WaypointData]],
) -> List[List[PointPath]]:
    shortest_paths: List[List[PointPath]] = []

    previous_map = origin_map
    for i, segment in enumerate(segments):
        next_map: Optional[MapInfo] = destination_map
        if len(segments) > i + 1:
            next_map = segments[i + 1].map_itself

        print(previous_map.n, "->", segment.map_itself.n, "->", next_map.n if next_map is not None else "DONE")
        injected_points: List[List[Point]] = []
        for submap in segment.injected_points:
            submap_shortest_paths = get_shortest_path_through_maplist(
                submap,
                origin_map=segment.map_itself,
                destination_map=segment.map_itself,
                waypoint_data=waypoint_data,
            )

            combined_shortest_paths = combine_consecutive_point_path_options(submap_shortest_paths)
            injected_points.append(point_paths_to_in_map_points(
                combined_shortest_paths,
                segment.map_itself
            ))

        shortest_path = get_shortest_path_through_map(
            previous_map,
            segment.map_itself,
            next_map,
            injected_points,
            waypoint_data,
        )

        shortest_paths.append(shortest_path)

        previous_map = segment.map_itself

    return shortest_paths


def point_paths_to_in_map_points(
    point_paths: List[PointPath],
    origin_map: MapInfo,
) -> List[Point]:
    return [
        pack_point_path_to_point(point_path, origin_map) for point_path in point_paths
    ]


################################################################################
# get_shortest_point_path
#
# Iterates over a list of PointPaths and returns whichver point path is the
# shortest. It does not filter on any other criteria like start/end positions.
################################################################################
def get_shortest_point_path(point_paths: List[PointPath]) -> PointPath:
    shortest_distance: Tuple[float, int] = (
        point_paths[0].walking_distance,
        point_paths[0].teleporting_cost,
    )
    shortest_path: PointPath = point_paths[0]

    for matching_combined_path in point_paths:
        distance: Tuple[float, int] = (
            matching_combined_path.walking_distance,
            matching_combined_path.teleporting_cost
        )
        if distance < shortest_distance:
            shortest_distance = distance
            shortest_path = matching_combined_path

    return shortest_path


# Should this be recursive? I think it could be recursive
def combine_consecutive_point_path_options(
    consecutive_point_path_options: List[List[PointPath]]
) -> List[PointPath]:
    # Base case, return the final node's point paths as-is
    if len(consecutive_point_path_options) == 1:
        return consecutive_point_path_options[0]

    prefix_paths = consecutive_point_path_options[0]
    suffix_paths = combine_consecutive_point_path_options(consecutive_point_path_options[1:])

    if len(suffix_paths) < 1:
        print("we got a null suffix path... bailing out (and cascading the problem up)")
        return []

    # Combine all possible combinations of paths
    combined_paths: List[PointPath] = []
    for prefix_path in prefix_paths:
        for suffix_path in suffix_paths:
            combined_path = combine_point_paths(prefix_path, suffix_path)
            if combined_path is None:
                continue

            # Add the successfully combined path
            combined_paths.append(combined_path)

    # Remove duplicate paths by taking the shorter one
    # there should be exactly len(start_options) * len(end_options) elements returned

    # The start point for each of the possible start paths
    start_options: List[Point] = [
        x.points[0] for x in consecutive_point_path_options[0]
    ]

    # The end point for each of the possible end paths
    end_options: List[Point] = [
        x.points[-1] for x in consecutive_point_path_options[-1]
    ]

    filtered_paths: List[PointPath] = []

    for start_option in start_options:
        for end_option in end_options:
            matching_combined_paths: List[PointPath] = []
            for combined_path in combined_paths:
                if (
                    combined_path.points[0] == start_option
                    and combined_path.points[-1] == end_option
                ):
                    matching_combined_paths.append(combined_path)

            if len(matching_combined_paths) < 1:
                print(start_options, end_options)
                raise ValueError("We dont have a matching in-out group here, there is likely a logic error in the code")

            # shortest_distance: Tuple[float, int] = (
            #     matching_combined_paths[0].walking_distance,
            #     matching_combined_paths[0].teleporting_cost,
            # )
            # shortest_path: PointPath  = matching_combined_paths[0]

            # for matching_combined_path in matching_combined_paths:
            #     distance: Tuple[float, int] = (
            #         matching_combined_path.walking_distance,
            #         matching_combined_path.teleporting_cost
            #     )
            #     if distance < shortest_distance:
            #         shortest_distance = distance
            #         shortest_path = matching_combined_path

            filtered_paths.append(get_shortest_point_path(matching_combined_paths))

    # sanity check
    if len(filtered_paths) != len(start_options) * len(end_options):
        print("wat")

    return filtered_paths


################################################################################
# combined_point_path
#
# Combines two paths that share a end/start portal node into a single path
# that travels across all of the points, combining the shared end/start point
# into a single point along the chain. If the end/start portals do not match
# then this function returns None
################################################################################
def combine_point_paths(first: PointPath, second: PointPath) -> Optional[PointPath]:
    portal_out = first.points[-1]
    portal_in = second.points[0]

    # Validate the end and the start portals are linked
    if (portal_out.identifier != portal_in.identifier):
        return None

    merged_portal = Point(
        x=portal_out.x,
        y=portal_out.y,
        identifier=portal_out.identifier,
        end_x=portal_in.x,
        end_y=portal_in.y,
        can_waypoint_teleport_to=False,
        walking_distance=0,
        teleporting_cost=0,
    )

    return PointPath(
        walking_distance=first.walking_distance + second.walking_distance,
        teleporting_cost=first.teleporting_cost + second.teleporting_cost,
        points=first.points[:-1] + [merged_portal] + second.points[1:]
    )


################################################################################
#
################################################################################
def pack_point_path_to_point(
    point_path: PointPath,
    origin_map: MapInfo,
) -> Point:
    entrance_portal = get_portal_by_id(point_path.points[0].identifier)
    exit_portal = get_portal_by_id(point_path.points[-1].identifier)

    entrance_pont = entrance_portal.get_point_in_map(origin_map)
    exit_point = exit_portal.get_point_in_map(origin_map)

    point = Point(
        x=entrance_pont.location[0],
        y=entrance_pont.location[1],
        end_x=exit_point.location[0],
        end_y=exit_point.location[1],
        walking_distance=point_path.walking_distance,
        teleporting_cost=point_path.teleporting_cost,
        identifier="PointPathSummary",  # TODO add some more details to this with what maps it connects from->to etc or just a random number maybe

        # this happens to be false for all the points we care about, but...
        # it might not be universally true. A point path really is just the start node of another ... hmmmmmmmmmmm wait
        # this whole thing is wrong isnt it...
        # we actually want to be setting the start x/y and end x/y points to be the portals on the OTHER map not the one the point path is in...
        can_waypoint_teleport_to=False,
    )

    point._point_path_source = point_path

    return point


################################################################################
#
################################################################################
def unpack_points(points: PointPath) -> List[Point]:
    output_points: List[Point] = []
    for point in points.points:
        if point._point_path_source is None:
            output_points.append(point)
        else:

            subpoints = unpack_points(point._point_path_source)

            output_points.append(Point(
                x=point.x,
                y=point.y,
                end_x=subpoints[0].x,
                end_y=subpoints[0].y,
                identifier="fakeportal",
                can_waypoint_teleport_to=False
            ))
            # todo sanity check that subpoints[0] x = end_x y=end_y
            output_points += subpoints[0:-1]

            output_points.append(Point(
                x=subpoints[-1].x,
                y=subpoints[-1].y,
                end_x=point.end_x,
                end_y=point.end_y,
                identifier="fakeportal",
                can_waypoint_teleport_to=False
            ))
            # todo sanity check that subpoints[-1] x = end_x y=end_y

    return output_points


################################################################################
#
################################################################################
def get_full_waypoint_unlock_path() -> None:
    # from paths.fullpath import segments, waypoint_data, origin
    # from paths.fullpath_skipbad import segments, waypoint_data, origin
    from paths.minimal_core_wizard_vault_utility import segments, waypoint_data, origin

    shortest_paths: List[List[PointPath]] = get_shortest_path_through_maplist(
        segments,
        origin_map=origin,
        destination_map=None,
        waypoint_data=waypoint_data
    )

    shortest_path = combine_consecutive_point_path_options(shortest_paths)

    if len(shortest_path) > 1:
        print("Found two shortest paths combinations, picking the first one")
        # TODO: this warning is just stating what happens later down in the code
        #       we should instead do the selection of the shortest path here.

    if len(shortest_path) < 1:
        raise ValueError("We have zero shortest paths")

    true_path = unpack_points(shortest_path[0])

    export_leaflet(true_path, "interactive_map", waypoint_data)
    export_taco(true_path, "taco_output", central_tyria_map_ids)

    print("Number of paths", len(true_path))

    print("Cost:", shortest_path[0].teleporting_cost)
    print("Walking:", shortest_path[0].walking_distance)


def main() -> None:
    get_full_waypoint_unlock_path()


if __name__ == "__main__":
    main()
