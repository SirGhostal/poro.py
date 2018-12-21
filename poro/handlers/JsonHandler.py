from . import Handler


class JsonHandler(Handler):

    async def after_request(self, region, endpoint_name, method_name, url, response):
        return await response.json()
