# import modules
import requests
import requests_cache
import time

# define function to pull data from API about geo information.


def ip_geo_retrieve(ip_address):

    # define the caching function to cache the request.
    requests_cache.install_cache(cache_name='geo_cache')

    # url to receive geo data from API server.
    url = "http://ip-api.com/json/{ip}".format(ip=ip_address)

    # return the respond and save to the variable.
    respond = requests.get(url)

    # check if the respond is coming from the cache if not delay to protect from overflow.
    if respond.__class__.__name__ != "CachedResponse":
        time.sleep(0.3)

    # save data to variable in json format.
    data = respond.json()
    return data
