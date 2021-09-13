from wallet.core.entities.accounts import Account, AccountFilters, AccountPayload
from wallet.core.gateways import Gateway


class AccountGateway(Gateway[Account, AccountFilters, AccountPayload]):
    ...
