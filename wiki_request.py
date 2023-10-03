from typing import TypedDict, List, Dict, Optional
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import hashlib
import json
import os
import re
import urllib.request
import urllib.parse
import wikitextparser as wtp

from map_info import map_info_from_name, map_info_from_id, central_tyria_map_ids



def get_portal_counts() -> Dict[str, Dict[str, int]]:
    portal_count: Dict[str, Dict[str, int]] = {}

    for map_id in central_tyria_map_ids:
        map_info = map_info_from_id(map_id)
        if map_info is None:
            raise ValueError("We have to make central_tyria_map_ids not be map ids, there is a desync bug")

        if map_info.n not in portal_count:
            portal_count[map_info.n] = {}

        connections = get_gw2_map_connections(
            map_info.n,
            get_wikitext_source(
                "https://wiki.guildwars2.com/wiki/{}".format(
                    urllib.parse.quote(map_info.n, safe='')
                )
            )
        )
        # print(map_info.n)
        

        for connection in connections:
            # Chantry of Secrets might not need to be on this list, but because this is all for the
            # turtle path stuff we might as well ignore it?
            if connection["link"] in ["Citadel of Flame", "Tower of Nightmares", "Chantry of Secrets"]:
                continue

            connection_info = map_info_from_name(connection["link"])
            if connection_info is None:
                print("    Unknown connection", connection)
                continue

            # Ignore connections to maps outside of central tyria
            if connection_info.i not in central_tyria_map_ids:
                continue

            count: int
            if connection["directions"] is None:
                count = 1
            else:
                count = len(connection["directions"].split(","))

            if connection_info.n not in portal_count[map_info.n]:
                portal_count[map_info.n][connection_info.n] = 0                

            portal_count[map_info.n][connection_info.n] += count


    return portal_count






link = re.compile(r"^\[\[(?P<link>.*)\]\](?: \((?P<directions>.*)\))?$")
# link = re.compile(r"\[\[(.*)\]\] \((.*)\)")


# Special matches to keep the regex simple
special_matches = {
    "Labyrinthine Cliffs": {
        "Lion's Arch": {
            "link": "Lion's Arch",
            "directions": None
        }
    },
    "Kessex Hills": {
        "<s>[[Tower of Nightmares (zone)|Tower of Nightmares]]</s>": {
            "link": "Tower of Nightmares",
            "directions": None,
        }
    },
    "Skywatch Archipelago": {
        "[[The Wizard's Tower]] (SE)<!-- the portal to the wizard's tower outpost is actually by the beacon of ages -->": {
            "link": "The Wizard's Tower",
            "directions": None,
        }
    }
}

class MatchGroups(TypedDict):
    link: str
    directions: Optional[str]

def get_gw2_map_connections(map_name: str, wikitext: str) -> List[MatchGroups]:
    connections = []
    parsed_wikitext = wtp.parse(wikitext)
    for template in parsed_wikitext.templates:
        if(template.name.strip() == "Location infobox"):
            for argument in template.arguments:
                if argument.name.strip() == "connections":
                    for connection in argument.value.strip().replace('<br />','<br>').replace('<br \\>','<br>').split("<br>"):
                        if map_name in special_matches and connection in special_matches[map_name]:
                            connections.append(special_matches[map_name][connection])
                        elif match := link.match(connection.strip()):
                            connections.append(match.groupdict())
                        else:
                            print("   No match found", connection)
    return connections


################################################################################
# get_wikitext_source
#
# Extracts the mediawiki source of the page
################################################################################
def get_wikitext_source(page_url: str) -> str:
    edit_page_url = get_edit_page_url(page_url)

    html = get_page(edit_page_url)
    soup = BeautifulSoup(html, features='html.parser')

    elements = soup.findAll("textarea", id="wpTextbox1")

    if len(elements) == 1:
        return elements[0].text

    raise LookupError("Cannot find the wiki page source")


################################################################################
# get_edit_page_url
#
# Searches for an edit page link on the page url presented. Some pages wont have
# edit but will instead have "view source" in this case that url is returned instead.
################################################################################
def get_edit_page_url(page_url: str) -> str:
    html = get_page(page_url)
    soup = BeautifulSoup(html, features='html.parser')

    # Attempt to find a single element with the id "ca-edit"
    elements = soup.findAll(id="ca-edit")
    if len(elements) == 1:
        if elements[0].name == "a":
            return urljoin(page_url, elements[0].attrs["href"])

        links = elements[0].findAll('a', href=re.compile(r'.*action=edit.*'))
        if len(links) == 1:
            return urljoin(page_url, links[0].attrs["href"])

    # Attempt to find a single element with the id "ca-viewsource"
    elements = soup.findAll(id="ca-viewsource")
    if len(elements) == 1:
        if elements[0].name == "a":
            return urljoin(page_url, elements[0].attrs["href"])

        links = elements[0].findAll('a', href=re.compile(r'.*action=edit.*'))
        if len(links) == 1:
            return urljoin(page_url, links[0].attrs["href"])

    raise LookupError("Cannot find an edit page link")


################################################################################
# get_page
#
# A simple wrapper to provide uniform html request headers and a simple but
# optional caching layer to prevent from hitting endpoints repeatedly while
# testing.
################################################################################
def get_page(page_url: str) -> str:
    haslib_sha = hashlib.new('sha256')
    haslib_sha.update(page_url.encode())
    sha = haslib_sha.hexdigest()

    cached_page_location = os.path.join("wiki_cache", sha+".json")
    if os.path.exists(cached_page_location):
        with open(cached_page_location) as f:
            return json.load(f)["html"]

    headers = { 'User-Agent' : 'Mozilla/5.0' }
    html = urllib.request.urlopen(urllib.request.Request(page_url, None, headers)).read().decode("utf-8")


    with open(cached_page_location, 'w') as f:
        json.dump({"url": page_url, "html": html}, f)

    return html
