These are the modules that define waypoint lists to hit. They are dynamically
parsed by the main.py file and can be used with the flag `--path <path name>`.

Each path module must export the following values:
* segments - A crafted list of nested segments between maps that define the path
* waypoint_data - data about the waypoints in each map that need to be hit
* origin - A MapInfo object that denotes the start
