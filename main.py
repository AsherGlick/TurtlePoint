from hashlib import new
from typing import Tuple, List, Any, Optional
from dataclasses import dataclass, field
from build_waypoint_data import get_waypoint_data
from build_portal_data import get_portal_data
import math
import os

from map_info import central_tyria_map_ids

from map_info import M
from subprocess import Popen, PIPE
import json


################################################################################
#
################################################################################
@dataclass
class Segment:
    # start: Any
    map_itself: Any
    # next_map: Any
    injected_points: List[List["Segment"]] = field(default_factory=list)


# The segments
segments = [
    Segment(M.RATA_SUM), # Start
    Segment(M.RATA_SUM),
    Segment(M.METRICA_PROVINCE),
    Segment(M.CALEDON_FOREST, [
        [Segment(M.THE_GROVE)],
    ]),
    Segment(M.BRISBAN_WILDLANDS, [
        [Segment(M.DRY_TOP)],
        [Segment(M.THE_SILVERWASTES)],
    ]),
    Segment(M.KESSEX_HILLS),
    Segment(M.QUEENSDALE),
    Segment(M.GENDARRAN_FIELDS, [
        [Segment(M.HARATHI_HINTERLANDS)],
    ]),
    Segment(M.LIONS_ARCH, [
        [Segment(M.SOUTHSUN_COVE)],
        [
            Segment(M.BLACK_CITADEL),
            Segment(M.BLACK_CITADEL),
            Segment(M.PLAINS_OF_ASHFORD),
            Segment(M.DIESSA_PLATEAU),
            Segment(M.WAYFARER_FOOTHILLS),
            Segment(M.HOELBRAK),
            Segment(M.DREDGEHAUNT_CLIFFS),
            Segment(M.TIMBERLINE_FALLS),
            Segment(M.LORNARS_PASS),
            Segment(M.SNOWDEN_DRIFTS),
            Segment(M.FROSTGORGE_SOUND),
            Segment(M.FIREHEART_RISE),
            Segment(M.IRON_MARCHES),
            Segment(M.BLAZERIDGE_STEPPES),
            Segment(M.FIELDS_OF_RUIN),
            Segment(M.DIVINITYS_REACH),
        ],
    ]),
    Segment(M.BLOODTIDE_COAST),
    Segment(M.SPARKFLY_FEN),
    Segment(M.MOUNT_MAELSTROM),
    Segment(M.STRAITS_OF_DEVASTATION),
    Segment(M.MALCHORS_LEAP),
    Segment(M.CURSED_SHORE),
    None, # End
]




# This file will load all the things that need to be loaded

waypoint_data = get_waypoint_data()
portal_data = get_portal_data()


################################################################################
#
################################################################################
@dataclass
class Point:
    x: float
    y: float
    end_x: float
    eny_y: float
    identifier: str
    can_waypoint_teleport_to: bool

    def __init__(
        self,
        x: float,
        y: float,
        identifier: str,
        end_x: Optional[float] = None,
        end_y: Optional[float] = None,
        can_waypoint_teleport_to: bool = True
    ):
        self.x = x
        self.y = y
        self.identifier = identifier

        if end_x is None:
            end_x = x
        if end_y is None:
            end_y = y

        self.end_x = end_x
        self.end_y = end_y
        self.can_waypoint_teleport_to = can_waypoint_teleport_to


    ############################################################################
    # Transforms the args into an arglist array that can be passed as a part of
    # the call to the cpp solver program.
    ############################################################################
    def to_arglist(self) -> List[str]:
        return [
            str(self.x),
            str(self.y),
            str(self.end_x),
            str(self.end_y),
            self.identifier,
            'T' if self.can_waypoint_teleport_to else 'F',
        ]


################################################################################
#
################################################################################
def build_map(map_id: int, in_map_id: int, out_map_id: int):

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


################################################################################
#
################################################################################
def get_shortest_path(
    start_point: Point,
    points_to_hit: List[Point],
    end_point: Point,
    map_id: int
):
    cachename = start_point.identifier + "_" + end_point.identifier + "shortest_path.json"
    cachedir = os.path.join("shortpath_cache", str(map_id))
    os.makedirs(cachedir, exist_ok=True)
    cachepath = os.path.join(cachedir, cachename)

    data = {}
    if os.path.exists(cachepath):
        with open(cachepath, 'r') as f:
            data = json.load(f)
    else:
        args = start_point.to_arglist()
        for point in points_to_hit:
            args += point.to_arglist()
        args += end_point.to_arglist()
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


################################################################################
#
################################################################################
def main():
    # for map_id in central_tyria_map_ids:
    #     build_map(map_id)

    for segment in segments:
        print(segment)


if __name__ == "__main__":
    main()
