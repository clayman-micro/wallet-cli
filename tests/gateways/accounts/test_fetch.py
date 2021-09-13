from http import HTTPStatus

import pytest

from wallet.core.entities.accounts import Account
from wallet.gateways import BadRequest
from wallet.gateways.accounts import AccountHTTPGateway


@pytest.mark.unit
async def test_success(create_response) -> None:
    create_response({"accounts": [{"id": 1, "name": "Foo"}]})
    gateway = AccountHTTPGateway(host="foo", token="bar")

    result = await gateway.fetch()

    assert result == [Account(key=1, name="Foo")]


@pytest.mark.unit
async def test_bad_request(create_response) -> None:
    create_response({}, HTTPStatus.BAD_REQUEST)
    gateway = AccountHTTPGateway(host="foo", token="bar")

    with pytest.raises(BadRequest):
        await gateway.fetch()
