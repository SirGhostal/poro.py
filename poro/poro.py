import asyncio
import aiohttp

from .apis import (
    HTTPClient,
    DataDragonApi,
    ChampionApiV3,
    ChampionMasteryApiV3,
    LeagueApiV3,
    LolStatusApiV3,
    MatchApiV3,
    SpectatorApiV3,
    SummonerApiV3,
    ThirdPartyCodeApiV3
)

from .handlers import TypeCorrectorHandler, ThrowOnErrorHandler, JsonHandler
from .handlers.RateLimit import RateLimitHandler


class Poro:
    def __init__(self, api_key, connector=None, loop=None,
                 early_handlers=None, late_handlers=None, rate_limit_handler=None):
        self.api_key = api_key
        self.loop = asyncio.get_event_loop() if loop is None else loop

        if not early_handlers:
            early_handlers = self.default_early_handlers
        if not late_handlers:
            late_handlers = self.default_late_handlers

        if not rate_limit_handler:
            limiter = RateLimitHandler(loop=self.loop)
            early_handlers.append(limiter)
            late_handlers.insert(0, limiter)

        self._http_client = HTTPClient(
            api_key, connector=connector, loop=self.loop,
            early_handlers=early_handlers, late_handlers=late_handlers
        )
        self._champion = ChampionApiV3(self._http_client)
        self._champion_mastery = ChampionMasteryApiV3(self._http_client)
        self._league = LeagueApiV3(self._http_client)
        self._lol_status = LolStatusApiV3(self._http_client)
        self._match = MatchApiV3(self._http_client)
        self._spectator = SpectatorApiV3(self._http_client)
        self._data_dragon = DataDragonApi(self._http_client)
        self._summoner = SummonerApiV3(self._http_client)
        self._third_party_code = ThirdPartyCodeApiV3(self._http_client)
        # TODO: tournament-stub
        # TODO: tournament

    @property
    def default_early_handlers(self):
        return [
            TypeCorrectorHandler(loop=self.loop),
        ]
    
    @property
    def default_late_handlers(self):
        return [
            ThrowOnErrorHandler(loop=self.loop),
            JsonHandler(loop=self.loop)
        ]

    @property
    def champion_mastery(self):
        """
        Interface to the ChampionMastery Endpoint
        :rtype: ChampionMasteryApiV3
        """
        return self._champion_mastery

    @property
    def champion(self):
        """
        Interface to the Champion Endpoint
        :rtype: ChampionApiV3
        """
        return self._champion

    @property
    def league(self):
        """
        Interface to the League Endpoint
        :rtype: LeagueApiV3
        """
        return self._league

    @property
    def lol_status(self):
        """
        Interface to the LoLStatus Endpoint
        :rtype: LolStatusApiV3
        """
        return self._lol_status

    @property
    def match(self):
        """
        Interface to the Match Endpoint
        :rtype: MatchApiV3
        """
        return self._match

    @property
    def spectator(self):
        """
        Interface to the Spectator Endpoint
        :rtype: SpectatorApiV3
        """
        return self._spectator

    @property
    def data_dragon(self):
        """
        Interface to the DataDragon Endpoint
        :rtype: DataDragonApi
        """
        return self._data_dragon

    @property
    def summoner(self):
        """
        Interface to the Summoner Endpoint
        :rtype: SummonerApiV3
        """
        return self._summoner

    @property
    def third_party_code(self):
        """
        Interface to the Third Party Code Endpoint
        :rtype: ThirdPartyCodeApiV3
        """
        return self._third_party_code
