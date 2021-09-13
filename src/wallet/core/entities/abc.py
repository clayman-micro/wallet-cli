from typing import TypeVar

from pydantic import BaseModel as Model
from pydantic.dataclasses import dataclass


class Entity(Model):
    key: int


@dataclass
class Filters:
    ...


@dataclass
class Payload:
    ...


ET = TypeVar("ET", bound=Entity)
FT = TypeVar("FT", bound=Filters)
PT = TypeVar("PT", bound=Payload)
