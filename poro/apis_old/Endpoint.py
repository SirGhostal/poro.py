
class Endpoint:
    def __init__(self, http, url):
        self.http = http
        self.url = url

    async def _raw_request(self, route):
        return await self.http.request(route)