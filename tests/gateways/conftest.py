from http import HTTPStatus
from typing import Any, Callable, Dict

import pytest


class FakeResponse:
    def __init__(self, body, status):
        self._body = body
        self.status = status
        self.headers = {"Content-Type": "application/json"}

    async def json(self):
        return self._body

    async def __aexit__(self, exc_type, exc, tb):
        pass

    async def __aenter__(self):
        return self


@pytest.fixture(scope="function")
def create_response(mocker) -> Callable[[Dict[str, Any], HTTPStatus], FakeResponse]:
    def builder(body: Dict[str, Any], status_code: HTTPStatus = HTTPStatus.OK) -> FakeResponse:
        response = FakeResponse(body=body, status=status_code)

        mocker.patch("aiohttp.ClientSession.request", return_value=response)

        return response

    return builder
