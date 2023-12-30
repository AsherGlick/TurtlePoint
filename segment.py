from dataclasses import dataclass, field
from typing import List
from map_info import MapInfo


################################################################################
# Segment
################################################################################
@dataclass
class Segment:
    # start: Any
    map_itself: MapInfo
    # next_map: Any
    injected_points: List[List["Segment"]] = field(default_factory=list)
