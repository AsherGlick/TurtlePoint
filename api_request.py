import os
import hashlib
import json
from urllib.request import urlopen

################################################################################
# get_api_json
#
# Call a JSON api and cache the results in `api_cache/`. Future calls to the 
# same API will be read from the cache. To expire the cache, delete the file.
################################################################################
def get_api_json(url: str):
    if not os.path.exists("api_cache"):
        os.makedirs("api_cache")

    url_hash = hashlib.new('sha256')
    url_hash.update(url.encode())
    url_cache = os.path.join("api_cache", url_hash.hexdigest() + ".json")

    if os.path.exists(url_cache):
        with open(url_cache, "r") as f:
            return json.load(f)

    try:
        response = urlopen(url).read().decode("utf-8")
    except Exception as e:
        print(url)
        raise e

    with open(url_cache, "w") as f:
        f.write(response)
    return json.loads(response)
