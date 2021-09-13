import pytest

from wallet.core.entities.accounts import Account, AccountPayload, Accounts
from wallet.core.gateways.accounts import AccountGateway
from wallet.core.services.accounts import AccountService


class FakeAccountsGateway(AccountGateway):
    async def fetch(self) -> Accounts:
        return []

    async def fetch_by_key(self, key: int) -> Account:
        raise NotImplementedError()

    async def add(self, payload: AccountPayload) -> Account:
        raise NotImplementedError()

    async def remove(self, entity: Account) -> None:
        raise NotImplementedError()


@pytest.mark.unit
async def test_success() -> None:
    fake_gateway = FakeAccountsGateway()
    service = AccountService(gateway=fake_gateway)

    result = await service.get_accounts()

    assert result == []
