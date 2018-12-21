
from .Http import Route
from .Endpoint import Endpoint

class ChampionApiV3Urls(object):

    def rotations():
        return ("GET", "/champion-rotations")


class ChampionApiV3(Endpoint):
    def __init__(self, http):
        super().__init__(http, "/platform/v3")

    async def rotations(self, region):
        method, path = ChampionApiV3Urls.rotations()
        return await self._raw_request(Route(method=method, region=region, endpoint=self.url, path=path))