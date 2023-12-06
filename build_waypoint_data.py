import json
from api_request import get_api_json
import os
from map_info import central_tyria_map_ids
from typing import List, Any, Set, Dict, TypedDict, Tuple


class WaypointData(TypedDict):
    name: str
    type: str
    floor: int
    coord: Tuple[float, float]
    id: int
    chat_link: str




force_region_id = {
    "39": 8, # "Mount Maelstrom" is in the "Steamspur Mountains"
    "53": 8, # "Sparkfly Fen" is in the "Steamspur Mountains"
}


################################################################################
# Reads or constructs the waypoint information.
# 
#
################################################################################
def get_waypoint_data():
    if os.path.exists("waypoint_cache.json"):
        with open("waypoint_cache.json", "r") as f:
            return filter_globally_ignored_waypoints(json.load(f))

    waypoints = {}
    for map_id in central_tyria_map_ids:
        waypoints[str(map_id)] = get_map_wapoints(str(map_id))

    with open("waypoint_cache.json", "w") as f:
        json.dump(waypoints, f, indent=4)

    return filter_globally_ignored_waypoints(waypoints)


ignored_waypoints: Set[int] = set()
def globally_ignore_waypoints(waypoint_ids: List[int]) -> None:
    global ignored_waypoints
    for waypoint_id in waypoint_ids:
        print("ignoring", waypoint_id)
        ignored_waypoints.add(waypoint_id)
    print(ignored_waypoints)

def filter_globally_ignored_waypoints(waypoints: Dict[str, List[WaypointData]]) -> Dict[str, List[WaypointData]]:
    print (ignored_waypoints)
    output = {}
    for map_id, map_waypoints in waypoints.items():
        points = []

        for point in map_waypoints:
            if point["id"] not in ignored_waypoints:
                points.append(point)
        output[map_id] = points
    return output

################################################################################
def get_map_wapoints(map_id: str):
    map_info = get_api_json(
        "https://api.guildwars2.com/v2/maps/{map_id}".format(
            map_id=map_id
        )
    )
    continent_id = map_info["continent_id"]
    region_id = map_info["region_id"]

    if map_id in force_region_id:
        region_id = force_region_id[map_id]

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
                waypoints[str(poi["id"])] = poi

    return list(waypoints.values())
