from abc import abstractmethod
from typing import AsyncGenerator, AsyncIterator, Generic, List

from wallet.core.entities.abc import ET, FT, PT


class Gateway(Generic[ET, FT, PT]):
    @abstractmethod
    async def fetch(self) -> List[ET]:
        ...

    @abstractmethod
    async def fetch_by_key(self, key: int) -> ET:
        ...

    @abstractmethod
    async def add(self, payload: PT) -> ET:
        ...

    @abstractmethod
    async def remove(self, entity: ET) -> None:
        ...
