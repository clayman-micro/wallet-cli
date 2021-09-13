from http import HTTPStatus
from typing import Any, Dict, Optional

from aiohttp import ClientSession
from yarl import URL


class BadRequest(Exception):
    def __init__(self, url: str, payload: Optional[Dict[str, str]] = None) -> None:
        self._url = url
        self._payload = payload

    @property
    def url(self) -> str:
        return self._url

    @property
    def payload(self) -> Optional[Dict[str, str]]:
        return self._payload


class HTTPGateway:
    def __init__(self, host: str, token: str) -> None:
        self._host = URL(host)
        self._token = token

    async def execute(
        self,
        method: str,
        path: str,
        query: Optional[Dict[str, str]] = None,
        payload: Optional[Dict[str, str]] = None,
        json: bool = False,
    ) -> Dict[str, Any]:
        url = self._host / path

        if query:
            url = url % query

        cookies = {"session": self._token}

        params = {}
        if payload:
            if json:
                params["json"] = payload
            else:
                params["data"] = payload

        async with ClientSession(cookies=cookies) as session:
            async with session.request(method, url, **params) as resp:
                if resp.status == HTTPStatus.OK:
                    if "application/json" in resp.headers["Content-Type"]:
                        result = await resp.json()
                    else:
                        result = await resp.text()
                else:
                    raise BadRequest(url=str(url), payload=payload)

        return result
