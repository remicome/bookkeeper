import dataclasses
import enum


class Discount(enum.Enum):
    """Self-declared discount on special items (food and housing)."""

    P1 = 0.75
    P2 = 1
    P3 = 1.25


@dataclasses.dataclass(frozen=True)
class Member:
    """A member of the group whose expenses should be shared."""

    name: str
    discount: Discount = dataclasses.field(hash=False, default=Discount.P2)
    drinks_alcohol: bool = dataclasses.field(hash=False, default=False)
