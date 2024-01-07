import dataclasses
import datetime
import typing

from ._member import Member


@dataclasses.dataclass
class Transaction:
    """A transaction paid by one member for one or more other members of the group.

    Args:
        * value: the currency value of this transaction
        * description: a human-readable description
        * date: the date of the transaction
        * payer: the group member who actually paid
        * indebted: the group members for which the transaction was issued.
    """

    value: float
    payer: Member
    indebted: typing.Set[Member]
    description: str = ""
    date: datetime.date = dataclasses.field(default_factory=datetime.date.today)
