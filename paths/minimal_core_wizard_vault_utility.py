from typing import List
from map_info import M
from build_waypoint_data import get_waypoint_data, WaypointData
from segment import Segment



origin = M.RATA_SUM
segments: List[Segment] =[
    # # Start
    Segment(M.METRICA_PROVINCE), # 1
    Segment(M.CALEDON_FOREST), # 3
    Segment(M.KESSEX_HILLS), # 1
    Segment(M.QUEENSDALE), # 2
    Segment(M.GENDARRAN_FIELDS), # 1
    Segment(M.HARATHI_HINTERLANDS), # 1
]

# origin = M.HOELBRAK
# segments: List[Segment] =[
#     # (Waypoint)
#     Segment(M.WAYFARER_FOOTHILLS), # 2
#     Segment(M.FROSTGORGE_SOUND), # 2
#     Segment(M.FIREHEART_RISE), # 1
#     Segment(M.IRON_MARCHES), # 1
#     Segment(M.BLAZERIDGE_STEPPES), # 3
#     Segment(M.FIELDS_OF_RUIN), # 2
# ]

# origin = M.BLACK_CITADEL
# segments: List[Segment] =[
#     # # (Waypoint)
#     Segment(M.PLAINS_OF_ASHFORD), # 1
#     Segment(M.DIESSA_PLATEAU), # 2
# ]

# origin = M.GENDARRAN_FIELDS
# segments: List[Segment] =[
#     # (Mistwarp)
#     Segment(M.LIONS_ARCH, [ # 5
#         [Segment(M.SOUTHSUN_COVE)], # 1
#     ]),
#     Segment(M.BLOODTIDE_COAST), # 1
#     Segment(M.LORNARS_PASS), # None
#     Segment(M.DREDGEHAUNT_CLIFFS), # 1
#     Segment(M.TIMBERLINE_FALLS), # 1
#     Segment(M.MOUNT_MAELSTROM), # 3
#     Segment(M.STRAITS_OF_DEVASTATION), # None
#     Segment(M.MALCHORS_LEAP), # 2
#     # End
# ]


required_points = set([
    "[&BEcAAAA=]", # Metrica Province
    "[&BDcBAAA=]", # Caledon Forest
    "[&BDUBAAA=]", # Caledon Forest
    "[&BEEFAAA=]", # Caledon Forest
    "[&BBIAAAA=]", # Kessex Hills
    "[&BPMAAAA=]", # Queensdale
    "[&BPwAAAA=]", # Queensdale
    "[&BOEAAAA=]", # Gendarran Fields
    "[&BMMAAAA=]", # Harathi Hinterlands
    "[&BA4EAAA=]", # Lion's Arch
    "[&BDAEAAA=]", # Lion's Arch
    "[&BDMEAAA=]", # Lion's Arch
    "[&BA4EAAA=]", # Lion's Arch
    "[&BNAGAAA=]", # Southsun Cove
    "[&BMcDAAA=]", # Plains of Ashford
    "[&BMYDAAA=]", # Diessa Plateau
    "[&BNoAAAA=]", # Diessa Plateau
    "[&BH4BAAA=]", # Wayfarer Foothills
    "[&BMIDAAA=]", # Wayfarer Foothills
    "[&BD8FAAA=]", # Dredgehaunt Cliffs
    "[&BEYCAAA=]", # Timberline Falls
    "[&BH4CAAA=]", # Frostgorge Sound
    "[&BHoCAAA=]", # Frostgorge Sound
    "[&BBcCAAA=]", # Fireheart Rise
    "[&BOQBAAA=]", # Iron Marches
    "[&BE4DAAA=]", # Blazeridge Steppes
    "[&BP0BAAA=]", # Blazeridge Steppes
    "[&BPwBAAA=]", # Blazeridge Steppes
    "[&BEsBAAA=]", # Fields of Ruin
    "[&BNcAAAA=]", # Fields of Ruin
    "[&BKQBAAA=]", # Bloodtide Coast
    "[&BM0CAAA=]", # Mount Maelstrom
    "[&BM8CAAA=]", # Mount Maelstrom
    "[&BNQCAAA=]", # Mount Maelstrom
    "[&BKkCAAA=]", # Malchor's Leap
    "[&BKYCAAA=]", # Malchor's Leap
])

messed_up_points ={
    x.lower():x for x in required_points
}

waypoint_data = get_waypoint_data()
for map_id in waypoint_data:
    for waypoint in waypoint_data[map_id]:
        if waypoint["chat_link"] not in required_points:
            waypoint["optional"] = True
        if waypoint["chat_link"].lower() in messed_up_points:
            if waypoint["chat_link"] != messed_up_points[waypoint["chat_link"].lower()]:
                print("Found {}, but it might be {}".format(waypoint["chat_link"], messed_up_points[waypoint["chat_link"].lower()]))
