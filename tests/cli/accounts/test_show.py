import pytest
from click.testing import CliRunner

from wallet.cli import cli
from wallet.core.entities.accounts import Account
from wallet.gateways.accounts import AccountHTTPGateway


@pytest.mark.integration
def test_success(mocker, fake_coroutine) -> None:
    mocked_fetch = mocker.patch.object(
        AccountHTTPGateway, "fetch", return_value=fake_coroutine(Account(key=1, name="Foo"))
    )
    runner = CliRunner()

    result = runner.invoke(cli, ["--debug", "accounts", "show"], obj={})

    assert result.exit_code == 0
    mocked_fetch.assert_called_once()
