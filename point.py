from dataclasses import dataclass, field
from typing import Optional, List
from build_portal_data import PortalInfo


################################################################################
# Point
#
# A class that contains a point that should be a part of the optimal distance
# calculation. A point may sometimes be a portal to another location, in which
# case the point will have an "end" position. A point may sometimes be a
# placeholder for an entire path, in which case the point will also contain an
# "end" position, and may possibly contain weights, and the list of points that
# create it so the points can later be re-added in place.
################################################################################
@dataclass
class Point:
    x: float
    y: float
    end_x: float
    end_y: float
    identifier: str
    can_waypoint_teleport_to: bool
    is_optional: bool
    walking_distance: float = 0
    teleporting_cost: int = 0

    _point_path_source: Optional["PointPath"] = field(default=None, repr=False,)

    def __init__(
        self,
        x: float,
        y: float,
        identifier: str,
        end_x: Optional[float] = None,
        end_y: Optional[float] = None,
        can_waypoint_teleport_to: bool = True,
        is_optional: bool = False,
        walking_distance: float = 0,
        teleporting_cost: int = 0,

    ):
        self.x = x
        self.y = y
        self.identifier = identifier
        self.is_optional = is_optional

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
    # from_portal_info
    #
    # A helper function to convert from PortalInfo into a Point.
    # TODO: When PortalInfo is depricated/removed this function should follow
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

        flag = 0
        if self.can_waypoint_teleport_to:
            flag |= (1 << 0)
        if self.is_optional:
            flag |= (1 << 1)

        return [
            position,
            "{}:{}".format(self.walking_distance, self.teleporting_cost),
            str(flag),
            self.identifier,
        ]


################################################################################
# PointPath
#
# A helper class that contains a list of points, and the weights the sum of
# those points have.
################################################################################
@dataclass
class PointPath():
    walking_distance: float
    teleporting_cost: int
    points: List[Point]
