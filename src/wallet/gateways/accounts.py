from wallet.core.entities.accounts import Account, AccountPayload, Accounts
from wallet.core.gateways.accounts import AccountGateway
from wallet.gateways import HTTPGateway


class AccountHTTPGateway(HTTPGateway, AccountGateway):
    async def fetch(self) -> Accounts:
        result = await self.execute(method="GET", path="api/accounts")

        return [Account(key=raw["id"], name=raw["name"]) for raw in result["accounts"]]

    async def fetch_by_key(self, key: int) -> Account:
        raise NotImplementedError()

    async def add(self, payload: AccountPayload) -> Account:
        raise NotImplementedError()

    async def remove(self, entity: Account) -> None:
        raise NotImplementedError()
