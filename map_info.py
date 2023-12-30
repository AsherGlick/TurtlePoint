from dataclasses import dataclass
from typing import List, Tuple, Dict, Optional


@dataclass
class MapInfo():
    # The id of the map.
    i: int
    # The name of the map
    n: str
    # The continent coordinate bounderies of the map
    bounding_box: Tuple[Tuple[float, float], Tuple[float, float]]


# Map List
class M():
    AMNYTAS = MapInfo(i=1517, n="Amnytas", bounding_box=((22614, 18938), (25558, 21882)))
    ARBORSTONE = MapInfo(i=1428, n="Arborstone", bounding_box=((29185, 100890), (33025, 103450)))
    AURIC_BASIN = MapInfo(i=1043, n="Auric Basin", bounding_box=((33280, 32512), (35328, 35328)))
    BITTERFROST_FRONTIER = MapInfo(i=1178, n="Bitterfrost Frontier", bounding_box=((53504, 23040), (56576, 24576)))
    BJORA_MARCHES = MapInfo(i=1343, n="Bjora Marches", bounding_box=((54911, 16972), (59391, 19148)))
    BLACK_CITADEL = MapInfo(i=218, n="Black Citadel", bounding_box=((56320, 29952), (57856, 32000)))
    BLAZERIDGE_STEPPES = MapInfo(i=20, n="Blazeridge Steppes", bounding_box=((61952, 28544), (64000, 32640)))
    BLOODSTONE_FEN = MapInfo(i=1165, n="Bloodstone Fen", bounding_box=((34816, 30338), (36352, 30978)))
    BLOODTIDE_COAST = MapInfo(i=73, n="Bloodtide Coast", bounding_box=((48000, 32256), (50432, 35456)))
    BRISBAN_WILDLANDS = MapInfo(i=54, n="Brisban Wildlands", bounding_box=((38656, 30848), (42112, 33536)))
    CALEDON_FOREST = MapInfo(i=34, n="Caledon Forest", bounding_box=((42112, 32512), (44032, 36480)))
    CELESTIAL_CHALLENGE = MapInfo(i=1353, n="Celestial Challenge", bounding_box=((43008, 26240), (44928, 28032)))
    CLAW_ISLAND = MapInfo(i=335, n="Claw Island", bounding_box=((46720, 32256), (48256, 33792)))
    CRYSTAL_OASIS = MapInfo(i=1210, n="Crystal Oasis", bounding_box=((57256, 42304), (62376, 44864)))
    CURSED_SHORE = MapInfo(i=62, n="Cursed Shore", bounding_box=((42880, 41600), (44928, 45696)))
    DESERT_HIGHLANDS = MapInfo(i=1211, n="Desert Highlands", bounding_box=((57256, 39744), (62376, 42304)))
    DIESSA_PLATEAU = MapInfo(i=32, n="Diessa Plateau", bounding_box=((56320, 27648), (59904, 29952)))
    DIVINITYS_REACH = MapInfo(i=18, n="Divinity's Reach", bounding_box=((43008, 26240), (44928, 28032)))
    DOMAIN_OF_ISTAN = MapInfo(i=1263, n="Domain of Istan", bounding_box=((55318, 59916), (59158, 63756)))
    DOMAIN_OF_KOURNA = MapInfo(i=1288, n="Domain of Kourna", bounding_box=((63624, 59572), (67720, 64308)))
    DOMAIN_OF_VABBI = MapInfo(i=1248, n="Domain of Vabbi", bounding_box=((63616, 52352), (68480, 55552)))
    DRACONIS_MONS = MapInfo(i=1195, n="Draconis Mons", bounding_box=((34718, 39284), (38558, 43124)))
    DRAGON_BASH_ARENA = MapInfo(i=1326, n="Dragon Bash Arena", bounding_box=((52224, 29696), (54528, 31360)))
    DRAGONFALL = MapInfo(i=1317, n="Dragonfall", bounding_box=((43968, 48384), (47424, 51200)))
    DRAGONS_END = MapInfo(i=1422, n="Dragon's End", bounding_box=((33126, 101838), (35302, 105550)))
    DRAGONS_STAND = MapInfo(i=1041, n="Dragon's Stand", bounding_box=((34048, 36096), (37120, 38784)))
    DREDGEHAUNT_CLIFFS = MapInfo(i=26, n="Dredgehaunt Cliffs", bounding_box=((52224, 31360), (54528, 34560)))
    DRIZZLEWOOD_COAST = MapInfo(i=1371, n="Drizzlewood Coast", bounding_box=((50128, 17809), (52304, 22289)))
    DRY_TOP = MapInfo(i=988, n="Dry Top", bounding_box=((36608, 30976), (38656, 33536)))
    ELON_RIVERLANDS = MapInfo(i=1228, n="Elon Riverlands", bounding_box=((58240, 44736), (61824, 48192)))
    EMBER_BAY = MapInfo(i=1175, n="Ember Bay", bounding_box=((37374, 43518), (41214, 47358)))
    EYE_OF_THE_NORTH = MapInfo(i=1370, n="Eye of the North", bounding_box=((57344, 21248), (58624, 22528)))
    FIELDS_OF_RUIN = MapInfo(i=21, n="Fields of Ruin", bounding_box=((61440, 32640), (64512, 35712)))
    FIREHEART_RISE = MapInfo(i=22, n="Fireheart Rise", bounding_box=((56576, 24832), (59904, 27648)))
    FROSTGORGE_SOUND = MapInfo(i=30, n="Frostgorge Sound", bounding_box=((53504, 24576), (56576, 27648)))
    GENDARRAN_FIELDS = MapInfo(i=24, n="Gendarran Fields", bounding_box=((46208, 28672), (50432, 30720)))
    GROTHMAR_VALLEY = MapInfo(i=1330, n="Grothmar Valley", bounding_box=((59392, 17504), (62592, 20064)))
    GYALA_DELVE = MapInfo(i=1490, n="Gyala Delve", bounding_box=((36677, 100479), (38853, 104191)))
    HARATHI_HINTERLANDS = MapInfo(i=17, n="Harathi Hinterlands", bounding_box=((46208, 25856), (49408, 28672)))
    HEART_OF_THE_MISTS = MapInfo(i=350, n="Heart of the Mists", bounding_box=((4865, 6398), (6145, 7678)))
    HOELBRAK = MapInfo(i=326, n="Hoelbrak", bounding_box=((52224, 29696), (54528, 31360)))
    IRON_MARCHES = MapInfo(i=25, n="Iron Marches", bounding_box=((59904, 25856), (61952, 29952)))
    JAHAI_BLUFFS = MapInfo(i=1301, n="Jahai Bluffs", bounding_box=((63316, 56376), (67412, 59576)))
    KESSEX_HILLS = MapInfo(i=23, n="Kessex Hills", bounding_box=((42112, 30464), (46208, 32512)))
    LABYRINTHINE_CLIFFS = MapInfo(i=922, n="Labyrinthine Cliffs", bounding_box=((54958, 38648), (56494, 40184)))
    LAKE_DORIC = MapInfo(i=1185, n="Lake Doric", bounding_box=((44928, 25472), (46208, 28032)))
    LIONS_ARCH = MapInfo(i=50, n="Lion's Arch", bounding_box=((48000, 30720), (50432, 32256)))
    LIONS_ARCH_AERODROME = MapInfo(i=1155, n="Lion's Arch Aerodrome", bounding_box=((47964, 30806), (50396, 32342)))
    LORNARS_PASS = MapInfo(i=27, n="Lornar's Pass", bounding_box=((50432, 29696), (52224, 34560)))
    MAD_KINGS_LABYRINTH = MapInfo(i=866, n="Mad King's Labyrinth", bounding_box=((1792, 13696), (2560, 14464)))
    MAD_KINGS_RACEWAY = MapInfo(i=1304, n="Mad King's Raceway", bounding_box=((2944, 13440), (3712, 14208)))
    MALCHORS_LEAP = MapInfo(i=65, n="Malchor's Leap", bounding_box=((43136, 39552), (47232, 41600)))
    MEMORY_OF_OLD_LIONS_ARCH = MapInfo(i=1483, n="Memory of Old Lion's Arch", bounding_box=((15232, 14336), (17664, 15872)))
    METRICA_PROVINCE = MapInfo(i=35, n="Metrica Province", bounding_box=((39936, 33536), (42112, 36864)))
    MISTLOCK_SANCTUARY = MapInfo(i=1206, n="Mistlock Sanctuary", bounding_box=((46368, 33520), (48416, 35568)))
    MOUNT_MAELSTROM = MapInfo(i=39, n="Mount Maelstrom", bounding_box=((50560, 37760), (54400, 40192)))
    NEW_KAINENG_CITY = MapInfo(i=1438, n="New Kaineng City", bounding_box=((25000, 98100), (28840, 100660)))
    NOBLES_FOLLY = MapInfo(i=1158, n="Noble's Folly", bounding_box=((33408, 30976), (36608, 32512)))
    PLAINS_OF_ASHFORD = MapInfo(i=19, n="Plains of Ashford", bounding_box=((57856, 29952), (61952, 32000)))
    QUEENSDALE = MapInfo(i=15, n="Queensdale", bounding_box=((42624, 28032), (46208, 30464)))
    RATA_SUM = MapInfo(i=139, n="Rata Sum", bounding_box=((37376, 36094), (39936, 38654)))
    SANDSWEPT_ISLES = MapInfo(i=1271, n="Sandswept Isles", bounding_box=((51994, 55402), (55194, 59754)))
    SEITUNG_PROVINCE = MapInfo(i=1442, n="Seitung Province", bounding_box=((21159, 100457), (24999, 103145)))
    SIRENS_LANDING = MapInfo(i=1203, n="Siren's Landing", bounding_box=((47002, 41600), (50330, 42880)))
    SKYWATCH_ARCHIPELAGO = MapInfo(i=1510, n="Skywatch Archipelago", bounding_box=((23590, 22650), (27302, 24826)))
    SNOWDEN_DRIFTS = MapInfo(i=31, n="Snowden Drifts", bounding_box=((50432, 27648), (54528, 29696)))
    SOUTHSUN_COVE = MapInfo(i=873, n="Southsun Cove", bounding_box=((44288, 35328), (46976, 37120)))
    SPARKFLY_FEN = MapInfo(i=53, n="Sparkfly Fen", bounding_box=((48000, 35456), (50560, 38784)))
    SPIRIT_VALE = MapInfo(i=1147, n="Spirit Vale", bounding_box=((36224, 27396), (37504, 30596)))
    STRAITS_OF_DEVASTATION = MapInfo(i=51, n="Straits of Devastation", bounding_box=((47232, 38784), (50560, 41600)))
    SUPER_ADVENTURE_BOX = MapInfo(i=935, n="Super Adventure Box", bounding_box=((1574, 5972), (2854, 8532)))
    TANGLED_DEPTHS = MapInfo(i=1045, n="Tangled Depths", bounding_box=((35328, 33792), (38656, 36096)))
    THE_CROWN_PAVILION = MapInfo(i=929, n="The Crown Pavilion", bounding_box=((43034, 26880), (43802, 27648)))
    THE_DESOLATION = MapInfo(i=1226, n="The Desolation", bounding_box=((58240, 48192), (61824, 53312)))
    THE_ECHOVALD_WILDS = MapInfo(i=1452, n="The Echovald Wilds", bounding_box=((29185, 100890), (33025, 103450)))
    THE_GROVE = MapInfo(i=91, n="The Grove", bounding_box=((42496, 36480), (43904, 38528)))
    THE_SILVERWASTES = MapInfo(i=1015, n="The Silverwastes", bounding_box=((36608, 30592), (38656, 32128)))
    THE_WIZARDS_TOWER = MapInfo(i=1509, n="The Wizard's Tower", bounding_box=((23399, 21882), (24807, 22650)))
    THOUSAND_SEAS_PAVILION = MapInfo(i=1465, n="Thousand Seas Pavilion", bounding_box=((20900, 98125), (22180, 99405)))
    THUNDERHEAD_PEAKS = MapInfo(i=1310, n="Thunderhead Peaks", bounding_box=((55820, 34936), (59148, 38648)))
    TIMBERLINE_FALLS = MapInfo(i=29, n="Timberline Falls", bounding_box=((51712, 34560), (54016, 37760)))
    VERDANT_BRINK = MapInfo(i=1052, n="Verdant Brink", bounding_box=((33408, 30976), (36608, 32512)))
    WAYFARER_FOOTHILLS = MapInfo(i=28, n="Wayfarer Foothills", bounding_box=((54528, 27648), (56320, 32256)))
    WINDSWEPT_HAVEN = MapInfo(i=1215, n="Windswept Haven", bounding_box=((64016, 51072), (65296, 52352)))


central_tyria_map_ids: List[int] = [
    M.TIMBERLINE_FALLS.i,   M.CALEDON_FOREST.i,   M.LORNARS_PASS.i,   M.DRY_TOP.i,  # noqa: E241
    M.FROSTGORGE_SOUND.i,   M.FIELDS_OF_RUIN.i,   M.CURSED_SHORE.i,   M.RATA_SUM.i,  # noqa: E241
    M.METRICA_PROVINCE.i,   M.FIREHEART_RISE.i,   M.SPARKFLY_FEN.i,   M.HOELBRAK.i,  # noqa: E241
    M.BRISBAN_WILDLANDS.i,  M.DIVINITYS_REACH.i,  M.MALCHORS_LEAP.i,  M.THE_GROVE.i,  # noqa: E241
    M.PLAINS_OF_ASHFORD.i,  M.MOUNT_MAELSTROM.i,  M.BLACK_CITADEL.i,  M.LIONS_ARCH.i,  # noqa: E241
    M.BLAZERIDGE_STEPPES.i, M.BLOODTIDE_COAST.i,  M.SOUTHSUN_COVE.i,  M.QUEENSDALE.i,  # noqa: E241
    M.DREDGEHAUNT_CLIFFS.i, M.GENDARRAN_FIELDS.i, M.SNOWDEN_DRIFTS.i, M.KESSEX_HILLS.i,  # noqa: E241
    M.WAYFARER_FOOTHILLS.i, M.THE_SILVERWASTES.i, M.DIESSA_PLATEAU.i, M.IRON_MARCHES.i,  # noqa: E241
    M.HARATHI_HINTERLANDS.i, M.STRAITS_OF_DEVASTATION.i  # noqa: E241
]


_map_name_lookup: Dict[str, MapInfo] = {}
_map_id_lookup: Dict[int, MapInfo] = {}
for attr in dir(M):
    if callable(getattr(M, attr)):
        continue
    if attr.startswith("__"):
        continue
    map_info: MapInfo = getattr(M, attr)
    _map_name_lookup[map_info.n] = map_info
    _map_id_lookup[map_info.i] = map_info


def map_info_from_name(map_name: str) -> Optional[MapInfo]:
    return _map_name_lookup.get(map_name, None)


def map_info_from_id(map_id: int) -> Optional[MapInfo]:
    return _map_id_lookup.get(map_id, None)


def _build_the_map_list() -> None:
    from api_request import get_api_json

    maps = get_api_json("https://api.guildwars2.com/v2/maps?ids=all")

    for map_data in maps:

        if map_data["type"] in ["Instance", "Pvp", "Unknown", "RedHome", "EdgeOfTheMists", "JumpPuzzle", "Tutorial", "BlueHome", "GreenHome", "Center"]:
            continue

        if map_data["name"].endswith("(Public)"):
            continue

        if map_data["id"] in [
            1095,  # Dragons Stand Heart of Thorns
            1042,  # Duplicate Verdant Bringk
            1316,  # Mists Rifts, similar enough to instanced content probably
        ]:
            continue

        name = map_data["name"].upper()
        name = name.replace(' ', '_')
        name = ''.join([char for char in name if char.isupper() or char == '_'])

        print("{slug} = MapInfo(i={map_id}, n=\"{map_name}\", bounding_box=(({x1}, {y1}), ({x2}, {y2})))".format(
            slug=name,
            map_id=map_data["id"],
            map_name=map_data["name"],
            x1=map_data["continent_rect"][0][0],
            y1=map_data["continent_rect"][0][1],
            x2=map_data["continent_rect"][1][0],
            y2=map_data["continent_rect"][1][1],
        ))


if __name__ == "__main__":
    _build_the_map_list()
