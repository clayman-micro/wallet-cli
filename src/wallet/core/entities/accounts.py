from typing import AsyncGenerator, List

from pydantic.dataclasses import dataclass

from wallet.core.entities.abc import Entity, Filters, Payload


# @dataclass
class Account(Entity):
    name: str


@dataclass
class AccountFilters(Filters):
    ...


@dataclass
class AccountPayload(Payload):
    name: str


AccountStream = AsyncGenerator[Account, None]
Accounts = List[Account]
