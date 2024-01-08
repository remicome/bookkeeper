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
        * weights: optional ratios of the debt which should be paid by each member
        * indebted: the group members for which the transaction was issued.
    """

    value: float
    payer: Member
    indebted: typing.Set[Member]
    description: str = ""
    weights: None | typing.Mapping[Member, float] = dataclasses.field(default=None)
    date: datetime.date = dataclasses.field(default_factory=datetime.date.today)

    def __post_init__(self):
        if self.weights is None:
            self.weights = {member: 1.0 for member in self.indebted}
