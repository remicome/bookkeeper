import typing

from ._member import Member
from ._transaction import Transaction


def balance(transactions: typing.List[Transaction]) -> typing.Mapping[Member, float]:
    """Compute each member's balance."""
    balances: typing.Dict[Member, float] = {}

    for transaction in transactions:
        balances[transaction.payer] = (
            balances.get(transaction.payer, 0) + transaction.value
        )
        value_per_member = transaction.value / len(transaction.indebted)

        for member in transaction.indebted:
            balances[member] = balances.get(member, 0) - value_per_member

    return balances
