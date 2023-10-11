from dataclasses import dataclass, field
from typing import Optional, List
from build_portal_data import PortalInfo

################################################################################
#
################################################################################
@dataclass
class Point:
    x: float
    y: float
    end_x: float
    end_y: float
    identifier: str
    can_waypoint_teleport_to: bool
    walking_distance=0
    teleporting_cost=0

    _point_path_source: Optional["PointPath"] = field(default=None, repr=False,)

    def __init__(
        self,
        x: float,
        y: float,
        identifier: str,
        end_x: Optional[float] = None,
        end_y: Optional[float] = None,
        can_waypoint_teleport_to: bool = True,
        walking_distance: float = 0,
        teleporting_cost: int = 0,

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

        self.walking_distance = walking_distance
        self.teleporting_cost = teleporting_cost

    ############################################################################
    @staticmethod
    def from_portal_info(portal: PortalInfo) -> 'Point':
        return Point(
            x=portal.location[0],
            y=portal.location[1],
            identifier=portal.uid,
            can_waypoint_teleport_to=False,
        )

    ############################################################################
    # Transforms the args into an arglist array that can be passed as a part of
    # the call to the cpp solver program.
    ############################################################################
    def to_arglist(self) -> List[str]:

        position: str

        if self.x == self.end_x and self.y == self.end_y:
            position = "{}:{}".format(self.x, self.y)
        else:
            position = "{}:{}:{}:{}".format(self.x, self.y, self.end_x, self.end_y)

        return [
            position,
            self.identifier,
            'T' if self.can_waypoint_teleport_to else 'F',
            "{}:{}".format(self.walking_distance, self.teleporting_cost)
        ]


@dataclass
class PointPath():
    walking_distance: float
    teleporting_cost: int
    points: List[Point]
