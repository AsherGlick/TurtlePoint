from hashlib import new
from typing import Tuple, List
from dataclasses import dataclass
from build_waypoint_data import get_waypoint_data
from build_portal_data import get_portal_data
import math



from subprocess import Popen, PIPE
import json



# This file will load all the things that need to be loaded

waypoint_data = get_waypoint_data()
portal_data = get_portal_data()


@dataclass
class Point:
    x: float
    y: float
    identifier: str


def build_map(map_id: int):

    # <mapid>/<start><end>.json

    # Build the pointarray that will be used to calculate the shortest path
    pointarray: List[Point] = []
    for point in waypoint_data[str(map_id)]:
        pointarray.append(Point(
            point["coord"][0],
            point["coord"][1],
            point["name"],
        ))


    for combination in every_combination_between_zero_and(len(portal_data[map_id])):
        start = Point(
            portal_data[map_id][combination[0]].location[0],
            portal_data[map_id][combination[0]].location[1],
            str(portal_data[map_id][combination[0]].uid),
        )
        end = Point(
            portal_data[map_id][combination[1]].location[0],
            portal_data[map_id][combination[1]].location[1],
            str(portal_data[map_id][combination[1]].uid),
        )

        print("Shortest Path of {} nodes:".format(len(pointarray)))
        print(get_shortest_path(start, pointarray, end, map_id))


################################################################################
# every_combination_between_zero_and
#
# Creates every combination of numbers between 0 and value exclusive. Does not
# repeat reversed combinations. 
################################################################################
def every_combination_between_zero_and(value: int):
    first = 0
    second = 0
    while first < value:
        yield (first, second)
        second += 1
        if second == value:
            first += 1
            second = first



import os
def get_shortest_path(start_point: Point, points_to_hit: List[Point], end_point: Point, map_id: int):
    cachename = start_point.identifier + "_" + end_point.identifier + "shortest_path.json"
    cachedir = os.path.join("shortpath_cache", str(map_id))
    os.makedirs(cachedir, exist_ok=True)
    cachepath = os.path.join(cachedir, cachename)

    data = {}
    if os.path.exists(cachepath):
        with open(cachepath, 'r') as f:
            data = json.load(f)
    else:
        args = [str(start_point.x), str(start_point.y), start_point.identifier]
        for point in points_to_hit:
            args += [str(point.x), str(point.y), point.identifier]
        args += [str(end_point.x), str(end_point.y), end_point.identifier]
        process = Popen(["./TurtleRoute/route"] + args, stdout=PIPE)
        (output, err) = process.communicate()
        exit_code = process.wait()

        data = json.loads(output)

        with open(cachepath, 'wb') as f:
            f.write(output) 

    print(data)

    sorted_points: List[Point] = []
    for point in data["points"]:
        sorted_points.append(Point(point["x"], point["y"], point["id"]))
    return sorted_points


from map_info import central_tyria_map_ids

def main():
    for map_id in central_tyria_map_ids:
        build_map(map_id)

    



if __name__ == "__main__":
    main()