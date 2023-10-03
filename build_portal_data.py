from map_info import M
from typing import Dict, Tuple, List
from dataclasses import dataclass
from map_info import MapInfo


ContinentCoordinatePreEODOffset = (+32768, +16384)


@dataclass
class Portal():
	identifier: str

	westmost_map: MapInfo
	westmost_portal_position: Tuple[float, float]

	eastmost_map: MapInfo
	eastmost_portal_position: Tuple[float, float]

	pre_eod: bool = False


raw_portals: List[Portal] = [
	Portal("001", M.AURIC_BASIN, (790, 16219), M.VERDANT_BRINK, (877, 16061), pre_eod=True),
	Portal("002", M.AURIC_BASIN, (2394, 18790), M.TANGLED_DEPTHS, (2915, 18296), pre_eod=True),
	Portal("003", M.TANGLED_DEPTHS, (2902, 19509), M.DRAGONS_STAND, (3776, 19771), pre_eod=True),
	Portal("004", M.VERDANT_BRINK, (3750, 15250), M.THE_SILVERWASTES, (4155, 15495), pre_eod=True),
	Portal("005", M.THE_SILVERWASTES, (5865, 15283), M.BRISBAN_WILDLANDS, (5974, 15604), pre_eod=True),
	Portal("006", M.HARATHI_HINTERLANDS, (5559, 16744), M.BRISBAN_WILDLANDS, (6039, 17105), pre_eod=True),
	Portal("007", M.METRICA_PROVINCE, (8011, 17021), M.BRISBAN_WILDLANDS, (8082, 17270), pre_eod=True),
	Portal("008", M.BRISBAN_WILDLANDS, (9218, 14666), M.KESSEX_HILLS, (9492, 14615), pre_eod=True),
	Portal("009", M.BRISBAN_WILDLANDS, (9244, 16368), M.CALEDON_FOREST, (9443, 16316), pre_eod=True),
	Portal("010", M.CALEDON_FOREST, (9926, 20038), M.THE_GROVE, (10229, 20633), pre_eod=True),
	Portal("011", M.METRICA_PROVINCE, (9130, 17658), M.CALEDON_FOREST, (9435, 17664), pre_eod=True),
	Portal("012", M.CALEDON_FOREST, (11061, 16191), M.KESSEX_HILLS, (11090, 16023), pre_eod=True),
	Portal("013", M.KESSEX_HILLS, (12232, 14028), M.QUEENSDALE, (12234, 14141), pre_eod=True),
	Portal("014", M.KESSEX_HILLS, (10301, 14182), M.QUEENSDALE, (10476, 13932), pre_eod=True),
	Portal("015", M.KESSEX_HILLS, (13353, 14230), M.GENDARRAN_FIELDS, (13561, 14110), pre_eod=True),
	Portal("016", M.DIVINITYS_REACH, (11900, 10461), M.LAKE_DORIC, (12217, 10587), pre_eod=True),
	Portal("017", M.LAKE_DORIC, (13385, 10069), M.HARATHI_HINTERLANDS, (13623, 10120), pre_eod=True),
	Portal("018", M.QUEENSDALE, (11021, 11934), M.DIVINITYS_REACH, (11245, 11602), pre_eod=True),
	Portal("019", M.QUEENSDALE, (13327, 12613), M.GENDARRAN_FIELDS, (13523, 12681), pre_eod=True),
	Portal("020", M.HARATHI_HINTERLANDS, (14341, 12140), M.GENDARRAN_FIELDS, (14344, 12335), pre_eod=True),
	Portal("021", M.GENDARRAN_FIELDS, (15718, 12361), M.HARATHI_HINTERLANDS, (15749, 12195), pre_eod=True),
	Portal("022", M.GENDARRAN_FIELDS, (17487, 13631), M.LORNARS_PASS, (17758, 13600), pre_eod=True),
	Portal("023", M.GENDARRAN_FIELDS, (17544, 12749), M.SNOWDEN_DRIFTS, (17780, 12754), pre_eod=True),
	Portal("024", M.GENDARRAN_FIELDS, (15879, 14217), M.LIONS_ARCH, (16119, 14380), pre_eod=True),
	Portal("025", M.BLOODTIDE_COAST, (16767, 15921), M.LIONS_ARCH, (16823, 15764), pre_eod=True),
	Portal("026", M.LIONS_ARCH, (17448, 15031), M.LORNARS_PASS, (17786, 15120), pre_eod=True),
	Portal("027", M.BLOODTIDE_COAST, (17545, 16082), M.LORNARS_PASS, (17784, 16001), pre_eod=True),
	Portal("028", M.BLOODTIDE_COAST, (17602, 17798), M.LORNARS_PASS, (17795, 17828), pre_eod=True),
	Portal("029", M.SPARKFLY_FEN, (15529, 19192), M.BLOODTIDE_COAST, (15542, 18835), pre_eod=True),
	Portal("030", M.LORNARS_PASS, (19344, 16580), M.DREDGEHAUNT_CLIFFS, (19618, 16380), pre_eod=True),
	Portal("031", M.LORNARS_PASS, (19035, 18066), M.TIMBERLINE_FALLS, (19184, 18273), pre_eod=True),
	Portal("032", M.TIMBERLINE_FALLS, (20618, 18243), M.DREDGEHAUNT_CLIFFS, (20665, 17971), pre_eod=True),
	Portal("033", M.SNOWDEN_DRIFTS, (19107, 13401), M.LORNARS_PASS, (19178, 13188), pre_eod=True),
	Portal("034", M.SNOWDEN_DRIFTS, (21645, 11577), M.WAYFARER_FOOTHILLS, (22032, 11797), pre_eod=True),
	Portal("035", M.SNOWDEN_DRIFTS, (20977, 11386), M.FROSTGORGE_SOUND, (21044, 11204), pre_eod=True),
	Portal("036", M.HOELBRAK, (21428, 14519), M.WAYFARER_FOOTHILLS, (22148, 14491), pre_eod=True),
	Portal("037", M.DREDGEHAUNT_CLIFFS, (20942, 15114), M.HOELBRAK, (21086, 14721), pre_eod=True),
	Portal("038", M.FROSTGORGE_SOUND, (23061, 11163), M.WAYFARER_FOOTHILLS, (23110, 11450), pre_eod=True),
	Portal("039", M.WAYFARER_FOOTHILLS, (23356, 11968), M.DIESSA_PLATEAU, (23680, 11995), pre_eod=True),
	Portal("040", M.FROSTGORGE_SOUND, (23706, 9704), M.FIREHEART_RISE, (23993, 9741), pre_eod=True),
	Portal("041", M.FROSTGORGE_SOUND, (21330, 8244), M.BITTERFROST_FRONTIER, (21380, 8046), pre_eod=True),
	Portal("042", M.DIESSA_PLATEAU, (24090, 13465), M.BLACK_CITADEL, (24301, 13685), pre_eod=True),
	Portal("043", M.BLACK_CITADEL, (25049, 14227), M.PLAINS_OF_ASHFORD, (25270, 14411), pre_eod=True),
	Portal("044", M.PLAINS_OF_ASHFORD, (26719, 13660), M.DIESSA_PLATEAU, (26847, 13506), pre_eod=True),
	Portal("045", M.PLAINS_OF_ASHFORD, (29104, 14842), M.BLAZERIDGE_STEPPES, (29269, 14884), pre_eod=True),
	Portal("046", M.IRON_MARCHES, (28194, 13489), M.PLAINS_OF_ASHFORD, (28217, 13642), pre_eod=True),
	Portal("047", M.BLAZERIDGE_STEPPES, (30928, 16180), M.FIELDS_OF_RUIN, (30932, 16429), pre_eod=True),
	Portal("048", M.IRON_MARCHES, (29103, 12452), M.BLAZERIDGE_STEPPES, (29314, 12615), pre_eod=True),
	Portal("049", M.FIREHEART_RISE, (27059, 10748), M.IRON_MARCHES, (27235, 10757), pre_eod=True),
	Portal("050", M.TIMBERLINE_FALLS, (19532, 21222), M.MOUNT_MAELSTROM, (19583, 21431), pre_eod=True),
	Portal("051", M.SPARKFLY_FEN, (17643, 21789), M.MOUNT_MAELSTROM, (17882, 21744), pre_eod=True),
	Portal("052", M.SPARKFLY_FEN, (16978, 22219), M.STRAITS_OF_DEVASTATION, (16980, 22547), pre_eod=True),
	Portal("053", M.STRAITS_OF_DEVASTATION, (17679, 23537), M.MOUNT_MAELSTROM, (17870, 23464), pre_eod=True),
	Portal("054", M.MALCHORS_LEAP, (14352, 24600), M.STRAITS_OF_DEVASTATION, (14575, 24541), pre_eod=True),
	Portal("055", M.CURSED_SHORE, (11731, 25347), M.MALCHORS_LEAP, (11926, 25129), pre_eod=True),
	Portal("056", M.RATA_SUM, (6114, 20837), M.METRICA_PROVINCE, (7281, 20046), pre_eod=True),
	Portal("057", M.SOUTHSUN_COVE, (13872, 20331), M.LIONS_ARCH, (16646, 14662), pre_eod=True),
	Portal("058", M.LIONS_ARCH, (16680, 14699), M.HOELBRAK, (20501, 14271), pre_eod=True),
	Portal("059", M.LIONS_ARCH, (16663, 14799), M.BLACK_CITADEL, (24051, 14060), pre_eod=True),
	Portal("060", M.THE_GROVE, (10450, 20912), M.LIONS_ARCH, (16621, 14815), pre_eod=True),
	Portal("061", M.RATA_SUM, (6003, 20530), M.LIONS_ARCH, (16550, 14759), pre_eod=True),
	Portal("062", M.DIVINITYS_REACH, (11341, 11005), M.LIONS_ARCH, (16592, 14666), pre_eod=True),
	Portal("063", M.DIVINITYS_REACH, (11937, 10966), M.FIELDS_OF_RUIN, (29065, 18418), pre_eod=True),
	Portal("064", M.GENDARRAN_FIELDS, (16706, 12619), M.STRAITS_OF_DEVASTATION, (17390, 23393), pre_eod=True),
	Portal("065", M.BLOODTIDE_COAST, (16672, 16653), M.STRAITS_OF_DEVASTATION, (17418, 23392), pre_eod=True),
	Portal("066", M.STRAITS_OF_DEVASTATION, (17442, 23401), M.LORNARS_PASS, (17815, 15000), pre_eod=True),
]


@dataclass
class PortalInfo:
	uid: str
	location: Tuple[float, float]


def get_portal_data() -> Dict[int, List[PortalInfo]]:
	portals: Dict[int, List[PortalInfo]] = {}
	for portal in raw_portals:

		portal_info = (
			(portal.westmost_map.i, portal.westmost_portal_position),
			(portal.eastmost_map.i, portal.eastmost_portal_position),
		)

		for map_id, point in portal_info:
			if map_id not in portals:
				portals[map_id] = []

			if portal.pre_eod:
				point = (
					point[0]+ContinentCoordinatePreEODOffset[0],
					point[1]+ContinentCoordinatePreEODOffset[1]
				)

			portals[map_id].append(PortalInfo(
				uid=portal.identifier,
				location=point
			))
	return portals


if __name__ == "__main__":
	for portal in raw_portals:
		if portal.westmost_portal_position[0] > portal.eastmost_portal_position[0]:
			print("Flipped Portals in id", portal.identifier)
