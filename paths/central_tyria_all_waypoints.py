from typing import List
from map_info import M
from build_waypoint_data import get_waypoint_data
from segment import Segment

origin = M.METRICA_PROVINCE

# The segments
segments: List[Segment] = [
    # Start
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
    # End
]

waypoint_data = get_waypoint_data(
    ignored_waypoints=[]
)
