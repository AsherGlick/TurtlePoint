from map_info import M
from typing import Dict, Tuple, List
from dataclasses import dataclass
from map_info import MapInfo
from dict_diff import dict_diff
import json


ContinentCoordinatePreEODOffset = (+32768, +16384)


@dataclass
class Portal():
	identifier: str

	westmost_map: MapInfo
	westmost_portal_position: Tuple[float, float]

	eastmost_map: MapInfo
	eastmost_portal_position: Tuple[float, float]

	pre_eod: bool = False

	def fixed_westmost_portal_position(self) -> Tuple[float, float]:
		return self.westmost_portal_position

	def fixed_eastmost_portal_position(self) -> Tuple[float, float]:
		return self.fixed_portal_position(self.eastmost_portal_position)

	def fixed_portal_position(self, position: Tuple[float,float]) -> Tuple[float, float]:
		if self.pre_eod:
			return (
				position[0] + ContinentCoordinatePreEODOffset[0],
				position[1] + ContinentCoordinatePreEODOffset[1],
			)
		return position

def eod_fix(x: float, y: float) -> Tuple[float, float]:
	return (
		x + ContinentCoordinatePreEODOffset[0],
		y + ContinentCoordinatePreEODOffset[1],
	)

raw_portals: List[Portal] = [
	Portal("001", M.AURIC_BASIN, eod_fix(790, 16219), M.VERDANT_BRINK, (877, 16061), pre_eod=True),
	Portal("002", M.AURIC_BASIN, eod_fix(2394, 18790), M.TANGLED_DEPTHS, (2915, 18296), pre_eod=True),
	Portal("003", M.TANGLED_DEPTHS, eod_fix(2902, 19509), M.DRAGONS_STAND, (3776, 19771), pre_eod=True),
	Portal("004", M.VERDANT_BRINK, eod_fix(3750, 15250), M.THE_SILVERWASTES, (4155, 15495), pre_eod=True),
	Portal("005", M.THE_SILVERWASTES, eod_fix(5865, 15283), M.BRISBAN_WILDLANDS, (5974, 15604), pre_eod=True),
	Portal("006", M.DRY_TOP, eod_fix(5559, 16744), M.BRISBAN_WILDLANDS, (6039, 17105), pre_eod=True),
	Portal("007", M.BRISBAN_WILDLANDS, eod_fix(8011, 17021), M.METRICA_PROVINCE, (8082, 17270), pre_eod=True),
	Portal("008", M.BRISBAN_WILDLANDS, eod_fix(9218, 14666), M.KESSEX_HILLS, (9492, 14615), pre_eod=True),
	Portal("009", M.BRISBAN_WILDLANDS, eod_fix(9244, 16368), M.CALEDON_FOREST, (9443, 16316), pre_eod=True),
	Portal("010", M.CALEDON_FOREST, eod_fix(9926, 20038), M.THE_GROVE, (10229, 20633), pre_eod=True),
	Portal("011", M.METRICA_PROVINCE, eod_fix(9130, 17658), M.CALEDON_FOREST, (9435, 17664), pre_eod=True),
	Portal("012", M.CALEDON_FOREST, eod_fix(11061, 16191), M.KESSEX_HILLS, (11090, 16023), pre_eod=True),
	Portal("013", M.QUEENSDALE, eod_fix(12232, 14028), M.KESSEX_HILLS, (12234, 14141), pre_eod=True),
	Portal("014", M.KESSEX_HILLS, eod_fix(10301, 14182), M.QUEENSDALE, (10476, 13932), pre_eod=True),
	Portal("015", M.KESSEX_HILLS, eod_fix(13353, 14230), M.GENDARRAN_FIELDS, (13561, 14110), pre_eod=True),
	Portal("016", M.DIVINITYS_REACH, eod_fix(11900, 10461), M.LAKE_DORIC, (12217, 10587), pre_eod=True),
	Portal("017", M.LAKE_DORIC, eod_fix(13385, 10069), M.HARATHI_HINTERLANDS, (13623, 10120), pre_eod=True),
	Portal("018", M.QUEENSDALE, eod_fix(11021, 11934), M.DIVINITYS_REACH, (11245, 11602), pre_eod=True),
	Portal("019", M.QUEENSDALE, eod_fix(13327, 12613), M.GENDARRAN_FIELDS, (13523, 12681), pre_eod=True),
	Portal("020", M.HARATHI_HINTERLANDS, eod_fix(14341, 12140), M.GENDARRAN_FIELDS, (14344, 12335), pre_eod=True),
	Portal("021", M.GENDARRAN_FIELDS, eod_fix(15718, 12361), M.HARATHI_HINTERLANDS, (15749, 12195), pre_eod=True),
	Portal("022", M.GENDARRAN_FIELDS, eod_fix(17487, 13631), M.LORNARS_PASS, (17758, 13600), pre_eod=True),
	Portal("023", M.GENDARRAN_FIELDS, eod_fix(17544, 12749), M.SNOWDEN_DRIFTS, (17780, 12754), pre_eod=True),
	Portal("024", M.GENDARRAN_FIELDS, eod_fix(15879, 14217), M.LIONS_ARCH, (16119, 14380), pre_eod=True),
	Portal("025", M.BLOODTIDE_COAST, eod_fix(16767, 15921), M.LIONS_ARCH, (16823, 15764), pre_eod=True),
	Portal("026", M.LIONS_ARCH, eod_fix(17448, 15031), M.LORNARS_PASS, (17786, 15120), pre_eod=True),
	Portal("027", M.BLOODTIDE_COAST, eod_fix(17545, 16082), M.LORNARS_PASS, (17784, 16001), pre_eod=True),
	Portal("028", M.BLOODTIDE_COAST, eod_fix(17602, 17798), M.LORNARS_PASS, (17795, 17828), pre_eod=True),
	Portal("029", M.SPARKFLY_FEN, eod_fix(15529, 19192), M.BLOODTIDE_COAST, (15542, 18835), pre_eod=True),
	Portal("030", M.LORNARS_PASS, eod_fix(19344, 16580), M.DREDGEHAUNT_CLIFFS, (19618, 16380), pre_eod=True),
	Portal("031", M.LORNARS_PASS, eod_fix(19035, 18066), M.TIMBERLINE_FALLS, (19184, 18273), pre_eod=True),
	Portal("032", M.TIMBERLINE_FALLS, eod_fix(20618, 18243), M.DREDGEHAUNT_CLIFFS, (20665, 17971), pre_eod=True),
	Portal("033", M.LORNARS_PASS, eod_fix(19107, 13401), M.SNOWDEN_DRIFTS, (19178, 13188), pre_eod=True),
	Portal("034", M.SNOWDEN_DRIFTS, eod_fix(21645, 11577), M.WAYFARER_FOOTHILLS, (22032, 11797), pre_eod=True),
	Portal("035", M.SNOWDEN_DRIFTS, eod_fix(20977, 11386), M.FROSTGORGE_SOUND, (21044, 11204), pre_eod=True),
	Portal("036", M.HOELBRAK, eod_fix(21428, 14519), M.WAYFARER_FOOTHILLS, (22148, 14491), pre_eod=True),
	Portal("037", M.DREDGEHAUNT_CLIFFS, eod_fix(20942, 15114), M.HOELBRAK, (21086, 14721), pre_eod=True),
	Portal("038", M.FROSTGORGE_SOUND, eod_fix(23061, 11163), M.WAYFARER_FOOTHILLS, (23110, 11450), pre_eod=True),
	Portal("039", M.WAYFARER_FOOTHILLS, eod_fix(23356, 11968), M.DIESSA_PLATEAU, (23680, 11995), pre_eod=True),
	Portal("040", M.FROSTGORGE_SOUND, eod_fix(23706, 9704), M.FIREHEART_RISE, (23993, 9741), pre_eod=True),
	Portal("041", M.FROSTGORGE_SOUND, eod_fix(21330, 8244), M.BITTERFROST_FRONTIER, (21380, 8046), pre_eod=True),
	Portal("042", M.DIESSA_PLATEAU, eod_fix(24090, 13465), M.BLACK_CITADEL, (24301, 13685), pre_eod=True),
	Portal("043", M.BLACK_CITADEL, eod_fix(25049, 14227), M.PLAINS_OF_ASHFORD, (25270, 14411), pre_eod=True),
	Portal("044", M.PLAINS_OF_ASHFORD, eod_fix(26719, 13660), M.DIESSA_PLATEAU, (26847, 13506), pre_eod=True),
	Portal("045", M.PLAINS_OF_ASHFORD, eod_fix(29104, 14842), M.BLAZERIDGE_STEPPES, (29269, 14884), pre_eod=True),
	Portal("046", M.IRON_MARCHES, eod_fix(28194, 13489), M.PLAINS_OF_ASHFORD, (28217, 13642), pre_eod=True),
	Portal("047", M.BLAZERIDGE_STEPPES, eod_fix(30928, 16180), M.FIELDS_OF_RUIN, (30932, 16429), pre_eod=True),
	Portal("048", M.IRON_MARCHES, eod_fix(29103, 12452), M.BLAZERIDGE_STEPPES, (29314, 12615), pre_eod=True),
	Portal("049", M.FIREHEART_RISE, eod_fix(27059, 10748), M.IRON_MARCHES, (27235, 10757), pre_eod=True),
	Portal("050", M.TIMBERLINE_FALLS, eod_fix(19532, 21222), M.MOUNT_MAELSTROM, (19583, 21431), pre_eod=True),
	Portal("051", M.SPARKFLY_FEN, eod_fix(17643, 21789), M.MOUNT_MAELSTROM, (17882, 21744), pre_eod=True),
	Portal("052", M.SPARKFLY_FEN, eod_fix(16978, 22219), M.STRAITS_OF_DEVASTATION, (16980, 22547), pre_eod=True),
	Portal("053", M.STRAITS_OF_DEVASTATION, eod_fix(17679, 23537), M.MOUNT_MAELSTROM, (17870, 23464), pre_eod=True),
	Portal("054", M.MALCHORS_LEAP, eod_fix(14352, 24600), M.STRAITS_OF_DEVASTATION, (14575, 24541), pre_eod=True),
	Portal("055", M.CURSED_SHORE, eod_fix(11731, 25347), M.MALCHORS_LEAP, (11926, 25129), pre_eod=True),
	Portal("056", M.RATA_SUM, eod_fix(6114, 20837), M.METRICA_PROVINCE, (7281, 20046), pre_eod=True),
	Portal("057", M.SOUTHSUN_COVE, eod_fix(13872, 20331), M.LIONS_ARCH, (16646, 14662), pre_eod=True),
	Portal("058", M.LIONS_ARCH, eod_fix(16680, 14699), M.HOELBRAK, (20501, 14271), pre_eod=True),
	Portal("059", M.LIONS_ARCH, eod_fix(16663, 14799), M.BLACK_CITADEL, (24051, 14060), pre_eod=True),
	Portal("060", M.THE_GROVE, eod_fix(10450, 20912), M.LIONS_ARCH, (16621, 14815), pre_eod=True),
	Portal("061", M.RATA_SUM, eod_fix(6003, 20530), M.LIONS_ARCH, (16550, 14759), pre_eod=True),
	Portal("062", M.DIVINITYS_REACH, eod_fix(11341, 11005), M.LIONS_ARCH, (16592, 14666), pre_eod=True),
	Portal("063", M.DIVINITYS_REACH, eod_fix(11937, 10966), M.FIELDS_OF_RUIN, (29065, 18418), pre_eod=True),
	Portal("064", M.GENDARRAN_FIELDS, eod_fix(16706, 12619), M.STRAITS_OF_DEVASTATION, (17390, 23393), pre_eod=True),
	# Chantry of Secrets is too complicated for us right now
	# Portal("065", M.BLOODTIDE_COAST, (16672, 16653), M.STRAITS_OF_DEVASTATION, (17418, 23392), pre_eod=True),
	Portal("066", M.STRAITS_OF_DEVASTATION, eod_fix(17442, 23401), M.LORNARS_PASS, (17815, 15000), pre_eod=True),
	Portal("067", M.BLOODTIDE_COAST, eod_fix(17253, 18918), M.SPARKFLY_FEN, (17355, 19216), pre_eod=True),
	Portal("068", M.FIELDS_OF_RUIN, eod_fix(29438, 16347), M.BLAZERIDGE_STEPPES, (29480, 16146), pre_eod=True),
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




def within_bounds(point: Tuple[float, float], bounds: Tuple[Tuple[float, float], Tuple[float, float]]):
	return bounds[0][0] < point[0] and point[0] < bounds[1][0] and bounds[0][1] < point[1] and point[1] < bounds[1][1]


if __name__ == "__main__":
	for portal in raw_portals:
		if portal.westmost_portal_position[0] > portal.eastmost_portal_position[0]:
			print("Flipped Portals in id", portal.identifier)

		if not within_bounds(portal.fixed_westmost_portal_position(), portal.westmost_map.bounding_box):
			print("Westmost portal in id {} is outside of map bounds. {}".format(portal.identifier, portal.westmost_map.n))
			print(portal.fixed_westmost_portal_position(), portal.westmost_map.bounding_box)
		if not within_bounds(portal.fixed_eastmost_portal_position(), portal.eastmost_map.bounding_box):
			print("Eastmost portal in id {} is outside of map bounds. {}".format(portal.identifier, portal.eastmost_map.n))
			print(portal.fixed_eastmost_portal_position(), portal.eastmost_map.bounding_box)

	from wiki_request import get_portal_counts
	from map_info import central_tyria_map_ids
	wiki_portal_counts = get_portal_counts()


	local_portal_counts = {}

	for portal in raw_portals:
		# skip any portals leading out of central tyria
		if portal.westmost_map.i not in central_tyria_map_ids or portal.eastmost_map.i not in central_tyria_map_ids:
			continue

		if portal.westmost_map.n not in local_portal_counts:
			local_portal_counts[portal.westmost_map.n] = {}
		if portal.eastmost_map.n not in local_portal_counts:
			local_portal_counts[portal.eastmost_map.n] = {}


		if portal.eastmost_map.n not in local_portal_counts[portal.westmost_map.n]:
			local_portal_counts[portal.westmost_map.n][portal.eastmost_map.n] = 0
		if portal.westmost_map.n not in local_portal_counts[portal.eastmost_map.n]:
			local_portal_counts[portal.eastmost_map.n][portal.westmost_map.n] = 0

		local_portal_counts[portal.westmost_map.n][portal.eastmost_map.n] += 1
		local_portal_counts[portal.eastmost_map.n][portal.westmost_map.n] += 1


	difflines = dict_diff(local_portal_counts, wiki_portal_counts)
	if len(difflines) > 0:
		print("Found diff between local data and Wiki Data")
	for line in difflines:
		print(line)
