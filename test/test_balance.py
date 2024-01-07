from bookkeeper.balance import balance
from bookkeeper.definitions import Member, Transaction


def test_balance():
    """Compute a simple balance."""
    first = Member(name="first")
    second = Member(name="second")
    transactions = [
        Transaction(
            value=100,
            payer=first,
            indebted=[first, second],
        )
    ]
    balances = balance(transactions)
    assert balances[first] == 50 and balances[second] == -50
