import asyncio
import aiohttp

import weakref

class Route:

    BASE_URL = "https://{region}.api.riotgames.com/lol"

    def __init__(self, method, region, endpoint, path, **kwargs):
        self.method = method
        self.region = region
        self.endpoint = endpoint
        self.path = path

        self.url = self.BASE_URL + self.endpoint + self.path
        
        url_params = re.findall(r"{(\w*)}", self.url)
        if "" in url_params:
            raise ValueError("Parameters with no name are unsupported.")
        self._url_params = url_params
        self._query_params = kwargs.keys()

    def __call__(self, **kwargs):
        for req_param in self._url_params:
            if req_param not in kwargs:
                raise ValueError('Parameter "{}" is required!'.format(req_param))

        query_params = {
            key: value for key, value in kwargs.items() if key in self._query_params
        }

        return (self.url.format(**kwargs), query_params)

    @property
    def bucket(self):
        # the bucket is region + endpoint + path w/ major parameters
        return '{0.region}:{0.endpoint}:{0.path}'.format(self)

    async def _raw_request(self, **kwargs):
        return self.http.request(self, **kwargsS)

class HTTPClient():
    def __init__(self, loop, api_key):
        self.loop = asyncio.get_event_loop() if loop is None else loop
        self._key = api_key
        self._session = aiohttp.ClientSession(loop=self.loop)
        self._locks = weakref.WeakValueDictionary()

    async def request(self, route, **kwargs):
        # Unpack route into raw variables.
        region = route.region
        bucket = route.bucket
        method = route.method
        url = route.url
        print(url)

        # One lock per bucket.
        lock = self._locks.get(bucket)
        if lock is None:
            lock = asyncio.Lock(loop=self.loop)
            if bucket is not None:
                self._locks[bucket] = lock

        headers = {
            "X-Riot-Token": self._key
        }
        async with lock:
            async with self._session.request(method, url, **kwargs) as r:
                json = await r.json()
        return json

