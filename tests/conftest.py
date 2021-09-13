import asyncio

import pytest

from wallet.app import AppConfig


@pytest.fixture(scope="session")
def config():
    return AppConfig()


@pytest.fixture(scope="function")
def fake_coroutine(mocker):
    def coro(result):
        future = asyncio.Future()
        future.set_result(result)

        return mocker.MagicMock(return_value=future)

    return coro
