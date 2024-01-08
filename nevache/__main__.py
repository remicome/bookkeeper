import pprint

from bookkeeper.balance import balance
from bookkeeper.settle import settle

from .transactions import transactions

balances = balance(transactions)
paiements = settle(transactions)

# Checks
positive_balance = sum(value for value in balances.values() if value > 0)
negative_balance = sum(value for value in balances.values() if value < 0)

assert positive_balance + negative_balance < 1e-4
assert abs(sum(paiement.value for paiement in paiements) - positive_balance) < 1e-4

for paiement in paiements:
    print(paiement)
