from map_info import M
from typing import Dict, Tuple, List
from dataclasses import dataclass
from map_info import MapInfo
from dict_diff import dict_diff
import json


@dataclass
class Portal():
	identifier: str

	westmost_map: MapInfo
	westmost_portal_position: Tuple[float, float]

	eastmost_map: MapInfo
	eastmost_portal_position: Tuple[float, float]


def eod_fix(x: float, y: float) -> Tuple[float, float]:
	return (
		x + 32768,
		y + 16384,
	)

raw_portals: List[Portal] = [
	Portal("001", M.AURIC_BASIN, eod_fix(790, 16219), M.VERDANT_BRINK, eod_fix(877, 16061)),
	Portal("002", M.AURIC_BASIN, eod_fix(2394, 18790), M.TANGLED_DEPTHS, eod_fix(2915, 18296)),
	Portal("003", M.TANGLED_DEPTHS, eod_fix(2902, 19509), M.DRAGONS_STAND, eod_fix(3776, 19771)),
	Portal("004", M.VERDANT_BRINK, eod_fix(3750, 15250), M.THE_SILVERWASTES, eod_fix(4155, 15495)),
	Portal("005", M.THE_SILVERWASTES, eod_fix(5865, 15283), M.BRISBAN_WILDLANDS, eod_fix(5974, 15604)),
	Portal("006", M.DRY_TOP, eod_fix(5559, 16744), M.BRISBAN_WILDLANDS, eod_fix(6039, 17105)),
	Portal("007", M.BRISBAN_WILDLANDS, eod_fix(8011, 17021), M.METRICA_PROVINCE, eod_fix(8082, 17270)),
	Portal("008", M.BRISBAN_WILDLANDS, eod_fix(9218, 14666), M.KESSEX_HILLS, eod_fix(9492, 14615)),
	Portal("009", M.BRISBAN_WILDLANDS, eod_fix(9244, 16368), M.CALEDON_FOREST, eod_fix(9443, 16316)),
	Portal("010", M.CALEDON_FOREST, eod_fix(9926, 20038), M.THE_GROVE, eod_fix(10229, 20633)),
	Portal("011", M.METRICA_PROVINCE, eod_fix(9130, 17658), M.CALEDON_FOREST, eod_fix(9435, 17664)),
	Portal("012", M.CALEDON_FOREST, eod_fix(11061, 16191), M.KESSEX_HILLS, eod_fix(11090, 16023)),
	Portal("013", M.QUEENSDALE, eod_fix(12232, 14028), M.KESSEX_HILLS, eod_fix(12234, 14141)),
	Portal("014", M.KESSEX_HILLS, eod_fix(10301, 14182), M.QUEENSDALE, eod_fix(10476, 13932)),
	Portal("015", M.KESSEX_HILLS, eod_fix(13353, 14230), M.GENDARRAN_FIELDS, eod_fix(13561, 14110)),
	Portal("016", M.DIVINITYS_REACH, eod_fix(11900, 10461), M.LAKE_DORIC, eod_fix(12217, 10587)),
	Portal("017", M.LAKE_DORIC, eod_fix(13385, 10069), M.HARATHI_HINTERLANDS, eod_fix(13623, 10120)),
	Portal("018", M.QUEENSDALE, eod_fix(11021, 11934), M.DIVINITYS_REACH, eod_fix(11245, 11602)),
	Portal("019", M.QUEENSDALE, eod_fix(13327, 12613), M.GENDARRAN_FIELDS, eod_fix(13523, 12681)),
	Portal("020", M.HARATHI_HINTERLANDS, eod_fix(14341, 12140), M.GENDARRAN_FIELDS, eod_fix(14344, 12335)),
	Portal("021", M.GENDARRAN_FIELDS, eod_fix(15718, 12361), M.HARATHI_HINTERLANDS, eod_fix(15749, 12195)),
	Portal("022", M.GENDARRAN_FIELDS, eod_fix(17487, 13631), M.LORNARS_PASS, eod_fix(17758, 13600)),
	Portal("023", M.GENDARRAN_FIELDS, eod_fix(17544, 12749), M.SNOWDEN_DRIFTS, eod_fix(17780, 12754)),
	Portal("024", M.GENDARRAN_FIELDS, eod_fix(15879, 14217), M.LIONS_ARCH, eod_fix(16119, 14380)),
	Portal("025", M.BLOODTIDE_COAST, eod_fix(16767, 15921), M.LIONS_ARCH, eod_fix(16823, 15764)),
	Portal("026", M.LIONS_ARCH, eod_fix(17448, 15031), M.LORNARS_PASS, eod_fix(17786, 15120)),
	Portal("027", M.BLOODTIDE_COAST, eod_fix(17545, 16082), M.LORNARS_PASS, eod_fix(17784, 16001)),
	Portal("028", M.BLOODTIDE_COAST, eod_fix(17602, 17798), M.LORNARS_PASS, eod_fix(17795, 17828)),
	Portal("029", M.SPARKFLY_FEN, eod_fix(15529, 19192), M.BLOODTIDE_COAST, eod_fix(15542, 18835)),
	Portal("030", M.LORNARS_PASS, eod_fix(19344, 16580), M.DREDGEHAUNT_CLIFFS, eod_fix(19618, 16380)),
	Portal("031", M.LORNARS_PASS, eod_fix(19035, 18066), M.TIMBERLINE_FALLS, eod_fix(19184, 18273)),
	Portal("032", M.TIMBERLINE_FALLS, eod_fix(20618, 18243), M.DREDGEHAUNT_CLIFFS, eod_fix(20665, 17971)),
	Portal("033", M.LORNARS_PASS, eod_fix(19107, 13401), M.SNOWDEN_DRIFTS, eod_fix(19178, 13188)),
	Portal("034", M.SNOWDEN_DRIFTS, eod_fix(21645, 11577), M.WAYFARER_FOOTHILLS, eod_fix(22032, 11797)),
	Portal("035", M.SNOWDEN_DRIFTS, eod_fix(20977, 11386), M.FROSTGORGE_SOUND, eod_fix(21044, 11204)),
	Portal("036", M.HOELBRAK, eod_fix(21428, 14519), M.WAYFARER_FOOTHILLS, eod_fix(22148, 14491)),
	Portal("037", M.DREDGEHAUNT_CLIFFS, eod_fix(20942, 15114), M.HOELBRAK, eod_fix(21086, 14721)),
	Portal("038", M.FROSTGORGE_SOUND, eod_fix(23061, 11163), M.WAYFARER_FOOTHILLS, eod_fix(23110, 11450)),
	Portal("039", M.WAYFARER_FOOTHILLS, eod_fix(23356, 11968), M.DIESSA_PLATEAU, eod_fix(23680, 11995)),
	Portal("040", M.FROSTGORGE_SOUND, eod_fix(23706, 9704), M.FIREHEART_RISE, eod_fix(23993, 9741)),
	Portal("041", M.FROSTGORGE_SOUND, eod_fix(21330, 8244), M.BITTERFROST_FRONTIER, eod_fix(21380, 8046)),
	Portal("042", M.DIESSA_PLATEAU, eod_fix(24090, 13465), M.BLACK_CITADEL, eod_fix(24301, 13685)),
	Portal("043", M.BLACK_CITADEL, eod_fix(25049, 14227), M.PLAINS_OF_ASHFORD, eod_fix(25270, 14411)),
	Portal("044", M.PLAINS_OF_ASHFORD, eod_fix(26719, 13660), M.DIESSA_PLATEAU, eod_fix(26847, 13506)),
	Portal("045", M.PLAINS_OF_ASHFORD, eod_fix(29104, 14842), M.BLAZERIDGE_STEPPES, eod_fix(29269, 14884)),
	Portal("046", M.IRON_MARCHES, eod_fix(28194, 13489), M.PLAINS_OF_ASHFORD, eod_fix(28217, 13642)),
	Portal("047", M.BLAZERIDGE_STEPPES, eod_fix(30928, 16180), M.FIELDS_OF_RUIN, eod_fix(30932, 16429)),
	Portal("048", M.IRON_MARCHES, eod_fix(29103, 12452), M.BLAZERIDGE_STEPPES, eod_fix(29314, 12615)),
	Portal("049", M.FIREHEART_RISE, eod_fix(27059, 10748), M.IRON_MARCHES, eod_fix(27235, 10757)),
	Portal("050", M.TIMBERLINE_FALLS, eod_fix(19532, 21222), M.MOUNT_MAELSTROM, eod_fix(19583, 21431)),
	Portal("051", M.SPARKFLY_FEN, eod_fix(17643, 21789), M.MOUNT_MAELSTROM, eod_fix(17882, 21744)),
	Portal("052", M.SPARKFLY_FEN, eod_fix(16978, 22219), M.STRAITS_OF_DEVASTATION, eod_fix(16980, 22547)),
	Portal("053", M.STRAITS_OF_DEVASTATION, eod_fix(17679, 23537), M.MOUNT_MAELSTROM, eod_fix(17870, 23464)),
	Portal("054", M.MALCHORS_LEAP, eod_fix(14352, 24600), M.STRAITS_OF_DEVASTATION, eod_fix(14575, 24541)),
	Portal("055", M.CURSED_SHORE, eod_fix(11731, 25347), M.MALCHORS_LEAP, eod_fix(11926, 25129)),
	Portal("056", M.RATA_SUM, eod_fix(6114, 20837), M.METRICA_PROVINCE, eod_fix(7281, 20046)),
	Portal("057", M.SOUTHSUN_COVE, eod_fix(13872, 20331), M.LIONS_ARCH, eod_fix(16646, 14662)),
	Portal("058", M.LIONS_ARCH, eod_fix(16680, 14699), M.HOELBRAK, eod_fix(20501, 14271)),
	Portal("059", M.LIONS_ARCH, eod_fix(16663, 14799), M.BLACK_CITADEL, eod_fix(24051, 14060)),
	Portal("060", M.THE_GROVE, eod_fix(10450, 20912), M.LIONS_ARCH, eod_fix(16621, 14815)),
	Portal("061", M.RATA_SUM, eod_fix(6003, 20530), M.LIONS_ARCH, eod_fix(16550, 14759)),
	Portal("062", M.DIVINITYS_REACH, eod_fix(11341, 11005), M.LIONS_ARCH, eod_fix(16592, 14666)),
	Portal("063", M.DIVINITYS_REACH, eod_fix(11937, 10966), M.FIELDS_OF_RUIN, eod_fix(29065, 18418)),
	Portal("064", M.GENDARRAN_FIELDS, eod_fix(16706, 12619), M.STRAITS_OF_DEVASTATION, eod_fix(17390, 23393)),
	# Chantry of Secrets is too complicated for us right now
	# Portal("065", M.BLOODTIDE_COAST, (16672, 16653), M.STRAITS_OF_DEVASTATION, (17418, 23392)),
	Portal("066", M.STRAITS_OF_DEVASTATION, eod_fix(17442, 23401), M.LORNARS_PASS, eod_fix(17815, 15000)),
	Portal("067", M.BLOODTIDE_COAST, eod_fix(17253, 18918), M.SPARKFLY_FEN, eod_fix(17355, 19216)),
	Portal("068", M.FIELDS_OF_RUIN, eod_fix(29438, 16347), M.BLAZERIDGE_STEPPES, eod_fix(29480, 16146)),
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

			portals[map_id].append(PortalInfo(
				uid=portal.identifier,
				location=point
			))
	return portals





################################################################################
# within_bounds
#
# A helper function used to determine if a specific point is within the bounds
# of a box defined by two a top left corner and a bottom right corner point.
################################################################################
def within_bounds(
	point: Tuple[float, float],
	bounds: Tuple[Tuple[float, float], Tuple[float, float]]
):
	return (
		bounds[0][0] < point[0]
		and point[0] < bounds[1][0]
		and bounds[0][1] < point[1]
		and point[1] < bounds[1][1]
	)


################################################################################
# sanity_check_portals
#
# A wrapper function to call the various sanity checkers on the portal data.
# This is done because there is no source of truth for the portal data in the
# api. So these checks are done to allow us to be as certian as we can be about
# the location and existance of portals given the information we have access
# to query.
################################################################################
def sanity_check_portals():
	sanity_check_eastmost_westmost_portal_location()
	sanity_check_portals_within_map_bounding_box()
	sanity_check_portal_quantity_and_destination_map_from_connectsto_wiki_data()


################################################################################
# sanity_check_eastmost_westmost_portal_location
#
# A simple check to make sure the westmost portal is actually the most west of
# the two portals, and the eastmost is the most east.
################################################################################
def sanity_check_eastmost_westmost_portal_location():
	for portal in raw_portals:
		if portal.westmost_portal_position[0] > portal.eastmost_portal_position[0]:
			print("Flipped Portals in id", portal.identifier)


################################################################################
# sanity_check_portals_within_map_bounding_box
#
# Sanity checks that for each end of a portal, that portal's location is
# actually in the map it says it is a part of
################################################################################
def sanity_check_portals_within_map_bounding_box():
	for portal in raw_portals:
		if not within_bounds(portal.westmost_portal_position, portal.westmost_map.bounding_box):
			print("Westmost portal in id {} is outside of map bounds. {}".format(portal.identifier, portal.westmost_map.n))
			print(portal.westmost_portal_position, portal.westmost_map.bounding_box)
		if not within_bounds(portal.eastmost_portal_position, portal.eastmost_map.bounding_box):
			print("Eastmost portal in id {} is outside of map bounds. {}".format(portal.identifier, portal.eastmost_map.n))
			print(portal.eastmost_portal_position, portal.eastmost_map.bounding_box)


################################################################################
# sanity_check_portal_quantity_and_destination_map
#
# Queries data out of the gw2 wiki, and validates that it lines up with the
# data we have. The wiki has a field called "Connects To" which contains the
# information about which maps this map connects to via portals. This validates
# that the data we have for which maps connect to what other maps, and how many
# times, lines up with the data on the wiki.
################################################################################
def sanity_check_portal_quantity_and_destination_map_from_connectsto_wiki_data():
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


if __name__ == "__main__":
	sanity_check_portals()
