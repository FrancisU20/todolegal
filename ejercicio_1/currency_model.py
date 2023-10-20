from dataclasses import dataclass
from datetime import datetime
from typing import Any, TypeVar, Type, cast
import dateutil.parser


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Currency:
    currency: str
    date: datetime
    value: float

    @staticmethod
    def from_dict(obj: Any) -> 'Currency':
        assert isinstance(obj, dict)
        currency = from_str(obj.get("currency"))
        date = from_datetime(obj.get("date"))
        value = from_float(obj.get("value"))
        return Currency(currency, date, value)

    def to_dict(self) -> dict:
        result: dict = {}
        result["currency"] = from_str(self.currency)
        result["date"] = self.date.isoformat()
        result["value"] = to_float(self.value)
        return result


def currency_from_dict(s: Any) -> Currency:
    return Currency.from_dict(s)


def currency_to_dict(x: Currency) -> Any:
    return to_class(Currency, x)
