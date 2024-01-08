from bookkeeper.definitions import Discount, Food, Member


def test_food():
    alice = Member(name="alice", discount=Discount.P1, stay_duration=1)
    bob = Member(name="bob", discount=Discount.P2, stay_duration=2)

    transaction = Food(
        value=100,
        payer=alice,
        indebted=[alice, bob],
    )
    assert 2 * transaction.weights[alice] == 0.75 * transaction.weights[bob]
