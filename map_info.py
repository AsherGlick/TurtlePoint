from dataclasses import dataclass
from typing import List

@dataclass
class MapInfo():
    # the id of the map
    i: int
    # the name of the map
    n: str


# MAP LIST
class M():
    AMNYTAS = MapInfo(i=1517, n="Amnytas")
    ARBORSTONE = MapInfo(i=1428, n="Arborstone")
    AURIC_BASIN = MapInfo(i=1043, n="Auric Basin")
    BITTERFROST_FRONTIER = MapInfo(i=1178, n="Bitterfrost Frontier")
    BJORA_MARCHES = MapInfo(i=1343, n="Bjora Marches")
    BLACK_CITADEL = MapInfo(i=218, n="Black Citadel")
    BLAZERIDGE_STEPPES = MapInfo(i=20, n="Blazeridge Steppes")
    BLOODSTONE_FEN = MapInfo(i=1165, n="Bloodstone Fen")
    BLOODTIDE_COAST = MapInfo(i=73, n="Bloodtide Coast")
    BRISBAN_WILDLANDS = MapInfo(i=54, n="Brisban Wildlands")
    CALEDON_FOREST = MapInfo(i=34, n="Caledon Forest")
    CELESTIAL_CHALLENGE = MapInfo(i=1353, n="Celestial Challenge")
    CLAW_ISLAND = MapInfo(i=335, n="Claw Island")
    CRYSTAL_OASIS = MapInfo(i=1210, n="Crystal Oasis")
    CURSED_SHORE = MapInfo(i=62, n="Cursed Shore")
    DESERT_HIGHLANDS = MapInfo(i=1211, n="Desert Highlands")
    DIESSA_PLATEAU = MapInfo(i=32, n="Diessa Plateau")
    DIVINITYS_REACH = MapInfo(i=18, n="Divinity's Reach")
    DOMAIN_OF_ISTAN = MapInfo(i=1263, n="Domain of Istan")
    DOMAIN_OF_KOURNA = MapInfo(i=1288, n="Domain of Kourna")
    DOMAIN_OF_VABBI = MapInfo(i=1248, n="Domain of Vabbi")
    DRACONIS_MONS = MapInfo(i=1195, n="Draconis Mons")
    DRAGON_BASH_ARENA = MapInfo(i=1326, n="Dragon Bash Arena")
    DRAGONFALL = MapInfo(i=1317, n="Dragonfall")
    DRAGONS_END = MapInfo(i=1422, n="Dragon's End")
    DRAGONS_STAND = MapInfo(i=1041, n="Dragon's Stand")
    DREDGEHAUNT_CLIFFS = MapInfo(i=26, n="Dredgehaunt Cliffs")
    DRIZZLEWOOD_COAST = MapInfo(i=1371, n="Drizzlewood Coast")
    DRY_TOP = MapInfo(i=988, n="Dry Top")
    ELON_RIVERLANDS = MapInfo(i=1228, n="Elon Riverlands")
    EMBER_BAY = MapInfo(i=1175, n="Ember Bay")
    EYE_OF_THE_NORTH = MapInfo(i=1370, n="Eye of the North")
    FIELDS_OF_RUIN = MapInfo(i=21, n="Fields of Ruin")
    FIREHEART_RISE = MapInfo(i=22, n="Fireheart Rise")
    FROSTGORGE_SOUND = MapInfo(i=30, n="Frostgorge Sound")
    GENDARRAN_FIELDS = MapInfo(i=24, n="Gendarran Fields")
    GROTHMAR_VALLEY = MapInfo(i=1330, n="Grothmar Valley")
    GYALA_DELVE = MapInfo(i=1490, n="Gyala Delve")
    HARATHI_HINTERLANDS = MapInfo(i=17, n="Harathi Hinterlands")
    HEART_OF_THE_MISTS = MapInfo(i=350, n="Heart of the Mists")
    HOELBRAK = MapInfo(i=326, n="Hoelbrak")
    IRON_MARCHES = MapInfo(i=25, n="Iron Marches")
    JAHAI_BLUFFS = MapInfo(i=1301, n="Jahai Bluffs")
    KESSEX_HILLS = MapInfo(i=23, n="Kessex Hills")
    LABYRINTHINE_CLIFFS = MapInfo(i=922, n="Labyrinthine Cliffs")
    LAKE_DORIC = MapInfo(i=1185, n="Lake Doric")
    LIONS_ARCH = MapInfo(i=50, n="Lion's Arch")
    LIONS_ARCH_AERODROME = MapInfo(i=1155, n="Lion's Arch Aerodrome")
    LORNARS_PASS = MapInfo(i=27, n="Lornar's Pass")
    MAD_KINGS_LABYRINTH = MapInfo(i=866, n="Mad King's Labyrinth")
    MAD_KINGS_RACEWAY = MapInfo(i=1304, n="Mad King's Raceway")
    MALCHORS_LEAP = MapInfo(i=65, n="Malchor's Leap")
    MEMORY_OF_OLD_LIONS_ARCH = MapInfo(i=1483, n="Memory of Old Lion's Arch")
    METRICA_PROVINCE = MapInfo(i=35, n="Metrica Province")
    MISTLOCK_SANCTUARY = MapInfo(i=1206, n="Mistlock Sanctuary")
    MISTS_RIFT = MapInfo(i=1316, n="Mists Rift")
    MOUNT_MAELSTROM = MapInfo(i=39, n="Mount Maelstrom")
    NEW_KAINENG_CITY = MapInfo(i=1438, n="New Kaineng City")
    NOBLES_FOLLY = MapInfo(i=1158, n="Noble's Folly")
    PLAINS_OF_ASHFORD = MapInfo(i=19, n="Plains of Ashford")
    QUEENSDALE = MapInfo(i=15, n="Queensdale")
    RATA_SUM = MapInfo(i=139, n="Rata Sum")
    SANDSWEPT_ISLES = MapInfo(i=1271, n="Sandswept Isles")
    SEITUNG_PROVINCE = MapInfo(i=1442, n="Seitung Province")
    SIRENS_LANDING = MapInfo(i=1203, n="Siren's Landing")
    SKYWATCH_ARCHIPELAGO = MapInfo(i=1510, n="Skywatch Archipelago")
    SNOWDEN_DRIFTS = MapInfo(i=31, n="Snowden Drifts")
    SOUTHSUN_COVE = MapInfo(i=873, n="Southsun Cove")
    SPARKFLY_FEN = MapInfo(i=53, n="Sparkfly Fen")
    SPIRIT_VALE = MapInfo(i=1147, n="Spirit Vale")
    STRAITS_OF_DEVASTATION = MapInfo(i=51, n="Straits of Devastation")
    SUPER_ADVENTURE_BOX = MapInfo(i=935, n="Super Adventure Box")
    TANGLED_DEPTHS = MapInfo(i=1045, n="Tangled Depths")
    THE_CROWN_PAVILION = MapInfo(i=929, n="The Crown Pavilion")
    THE_DESOLATION = MapInfo(i=1226, n="The Desolation")
    THE_ECHOVALD_WILDS = MapInfo(i=1452, n="The Echovald Wilds")
    THE_GROVE = MapInfo(i=91, n="The Grove")
    THE_SILVERWASTES = MapInfo(i=1015, n="The Silverwastes")
    THE_WIZARDS_TOWER = MapInfo(i=1509, n="The Wizard's Tower")
    THOUSAND_SEAS_PAVILION = MapInfo(i=1465, n="Thousand Seas Pavilion")
    THUNDERHEAD_PEAKS = MapInfo(i=1310, n="Thunderhead Peaks")
    TIMBERLINE_FALLS = MapInfo(i=29, n="Timberline Falls")
    VERDANT_BRINK = MapInfo(i=1052, n="Verdant Brink")
    WAYFARER_FOOTHILLS = MapInfo(i=28, n="Wayfarer Foothills")
    WINDSWEPT_HAVEN = MapInfo(i=1215, n="Windswept Haven")


central_tyria_map_ids: List[int]= [
    M.TIMBERLINE_FALLS.i,   M.CALEDON_FOREST.i,   M.LORNARS_PASS.i,   M.DRY_TOP.i,
    M.FROSTGORGE_SOUND.i,   M.FIELDS_OF_RUIN.i,   M.CURSED_SHORE.i,   M.RATA_SUM.i,
    M.METRICA_PROVINCE.i,   M.FIREHEART_RISE.i,   M.SPARKFLY_FEN.i,   M.HOELBRAK.i,
    M.BRISBAN_WILDLANDS.i,  M.DIVINITYS_REACH.i,  M.MALCHORS_LEAP.i,  M.THE_GROVE.i,
    M.PLAINS_OF_ASHFORD.i,  M.MOUNT_MAELSTROM.i,  M.BLACK_CITADEL.i,  M.LIONS_ARCH.i,
    M.BLAZERIDGE_STEPPES.i, M.BLOODTIDE_COAST.i,  M.SOUTHSUN_COVE.i,  M.QUEENSDALE.i,
    M.DREDGEHAUNT_CLIFFS.i, M.GENDARRAN_FIELDS.i, M.SNOWDEN_DRIFTS.i, M.KESSEX_HILLS.i,
    M.WAYFARER_FOOTHILLS.i, M.THE_SILVERWASTES.i, M.DIESSA_PLATEAU.i, M.IRON_MARCHES.i,
    M.HARATHI_HINTERLANDS.i, M.STRAITS_OF_DEVASTATION.i
]




def _build_the_map_list():
    from api_request import get_api_json

    maps = get_api_json("https://api.guildwars2.com/v2/maps?ids=all")

    for map_data in maps:

        if map_data["type"] in ["Instance", "Pvp", "Unknown", "RedHome", "EdgeOfTheMists", "JumpPuzzle", "Tutorial", "BlueHome", "GreenHome", "Center"]:
            continue

        if map_data["name"].endswith("(Public)"):
            continue

        if map_data["id"] in [
            1095, # Dragons Stand Heart of Thorns
            1042, # Duplicate Verdant Bringk
        ]:
            continue

        name = map_data["name"].upper()
        name = name.replace(' ', '_')
        name = ''.join([char for char in name if char.isupper() or char == '_'])

        print("{slug} = MapInfo(i={map_id}, n=\"{map_name}\")".format(
            slug=name,
            map_id=map_data["id"],
            map_name=map_data["name"],
        ))

if __name__ == "__main__":
    _build_the_map_list()