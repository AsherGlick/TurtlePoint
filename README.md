This is an attempt to create the most optimal path to unlock all of the central
tyria waypoints on a Siege Turtle.


Each individual map has the optimal path through the map calculated.
Additionally a path from the end of one map to the start of the next is taken
into account when calculating the path.


Things that are not accounted for yet
================================================================================
* Places like southsun cove with only one entrance/exit could be done in the middle of the rest of lions arch
* All characters start with the 5 waypoints outside each starting city
* Characters have every waypoint they have already visited unlocked and can teleport back to them
* Final stop optimization, the final stop on a route, or before waypointing does not need to end on an exit portal. Final stop before waypointing does take into account distance from final location and new waypoint though.



Organization
================================================================================
This code is not very well organized yet. It is currently still in a prototype
phase just to experiment to see what is possible. There is a lot of caching
going on in order to prevent reprocessing or respect rate limits.

* TurtleRoute/ - A CPP Traveling Salesman Problem solver given a fixed start and end point
* shortpath_cache/ - A cache of all the outputs from `TurtleRoute/`'s executable
* api_cache/ - A cache of GW2 API responses
* wiki_cache/ - A cache of wiki.guildwars2.com pages
* map_info.py - A python library containing information about maps. run `python mapinfo.py` to generate the information
* build_portal_data.py - a python library to get all the portal data. Run `python build_portal_data.py` to validate the information
* main.py - the main process that can be run to generate the marker pack
