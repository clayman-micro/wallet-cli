from wallet.core.entities.accounts import Accounts
from wallet.core.gateways.accounts import AccountGateway


class AccountService:
    gateway: AccountGateway

    def __init__(self, gateway: AccountGateway) -> None:
        self.gateway = gateway

    async def get_accounts(self) -> Accounts:
        return await self.gateway.fetch()
