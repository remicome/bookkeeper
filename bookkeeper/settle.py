import dataclasses
import typing

from ._member import Member
from ._transaction import Transaction
from .balance import balance


@dataclasses.dataclass
class Paiement:
    """A paiement to be issued.

    Args:
        * sender: issuer of the paiement
        * recipient: recipient of the paiement
        * value: currency value of the paiement
    """

    sender: Member
    recipient: Member
    value: float


def settle(transactions: typing.List[Transaction]) -> typing.List[Paiement]:
    """Settle a set of transaction by issuing a list of paiements to be made.

    This is the algorithm used by splittypie: the person with the lowest balance pays
    all it cans to the one with the highest balance, until we reach equilibrium.
    """
    paiements = []
    balances = balance(transactions)

    # Avoid precision issues by rounding everything
    balances = {member: round(value, 2) for member, value in balances.items()}
    precision = 0.01

    while any(abs(value) > 2 * precision for value in balances.values()):
        member_with_lowest_balance = min(balances, key=lambda k: balances[k])
        member_with_highest_balance = max(balances, key=lambda k: balances[k])

        lowest_balance = balances[member_with_lowest_balance]
        highest_balance = balances[member_with_highest_balance]
        if lowest_balance > 0 or highest_balance < 0:
            raise RuntimeError

        paiement_value = min(-lowest_balance, highest_balance)

        paiements.append(
            Paiement(
                sender=member_with_lowest_balance,
                recipient=member_with_highest_balance,
                value=paiement_value,
            )
        )
        balances[member_with_lowest_balance] += paiement_value
        balances[member_with_highest_balance] -= paiement_value

    return paiements