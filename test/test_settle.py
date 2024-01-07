from bookkeeper.definitions import Member, Transaction
from bookkeeper.settle import settle


def test_settle():
    """Settle a single transaction."""
    members = [
        Member(name="first"),
        Member(name="second"),
    ]
    transactions = [
        Transaction(
            value=100,
            payer=members[0],
            indebted=members,
        )
    ]
    paiements = settle(transactions)
    assert (
        len(paiements) == 1
        and paiements[0].sender.name == members[1].name
        and paiements[0].recipient.name == members[0].name
    )
