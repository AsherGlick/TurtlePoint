import json
from api_request import get_api_json
import os
from map_info import central_tyria_map_ids
from typing import List, Any, Set, Dict, TypedDict, Tuple


################################################################################
# WaypointData
#
# The datastructure of the waypoint information that is returned from the GW2
# rest api and stored in the waypoint_cache.json file.
################################################################################
class WaypointData(TypedDict):
    name: str
    type: str
    floor: int
    coord: Tuple[float, float]
    id: int
    chat_link: str
    optional: bool


################################################################################
# get_waypoint_data
# 
# Returns data about all waypoints. The data is cached so subsequent calls to
# the function are faster.
################################################################################
def get_waypoint_data(ignored_waypoints: List[int] = []) -> Dict[str, List[WaypointData]]:
    if os.path.exists("waypoint_cache.json"):
        with open("waypoint_cache.json", "r") as f:
            return filter_ignored_waypoints(
                json.load(f),
                ignored_waypoint_ids=set(ignored_waypoints),
            )

    waypoints = {}
    for map_id in central_tyria_map_ids:
        waypoints[str(map_id)] = get_map_wapoints(str(map_id))

    with open("waypoint_cache.json", "w") as f:
        json.dump(waypoints, f, indent=4)

    return filter_ignored_waypoints(
        waypoints,
        ignored_waypoint_ids=set(ignored_waypoints),
    )


################################################################################
# filter_out_ignored_waypoints
#
# A helper function to filter out waypoints from any map given the waypoint id
################################################################################
def filter_ignored_waypoints(waypoints: Dict[str, List[WaypointData]], ignored_waypoint_ids: Set[int]) -> Dict[str, List[WaypointData]]:
    output = {}
    for map_id, map_waypoints in waypoints.items():
        points = []

        for point in map_waypoints:
            if point["id"] not in ignored_waypoint_ids:
                points.append(point)
        output[map_id] = points
    return output


# Some descrepencies between the v2/maps api and the v2/continents api exist
# and need to be forced to be a certian value in order to be interoperable.
force_map_region_id = {
    "39": 8, # "Mount Maelstrom" is in the "Steamspur Mountains"
    "53": 8, # "Sparkfly Fen" is in the "Steamspur Mountains"
}


################################################################################
# get_map_waypoints
#
# Get all of the waypoints for a given map_d using the gw2 rest apis.
################################################################################
def get_map_wapoints(map_id: str) -> List[WaypointData]:
    map_info = get_api_json(
        "https://api.guildwars2.com/v2/maps/{map_id}".format(
            map_id=map_id
        )
    )
    continent_id = map_info["continent_id"]
    region_id = map_info["region_id"]

    if map_id in force_map_region_id:
        region_id = force_map_region_id[map_id]

    waypoints = {}

    for floor in map_info["floors"]:
        floor_info = get_api_json(
            "https://api.guildwars2.com/v2/continents/{continent_id}/floors/{floor}/regions/{region_id}/maps/{map_id}".format(
                continent_id=continent_id,
                floor=floor,
                region_id=region_id,
                map_id=map_id
            )
        )

        for _, poi in floor_info["points_of_interest"].items():
            if poi["type"] == "waypoint":
                poi["optional"] = False # TODO: instead of hacking "optional" into the TypedDict we should make a dataclass and do real typechecking
                waypoints[str(poi["id"])] = poi

    return list(waypoints.values())
