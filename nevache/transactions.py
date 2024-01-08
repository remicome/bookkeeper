from bookkeeper.definitions import Discount, Food, Housing, Member, Transaction

alice = Member(name="Alice", discount=Discount.P2, stay_duration=3)
anouk = Member(name="Anouk", discount=Discount.P2, stay_duration=6)
antoine = Member(name="Antoine", discount=Discount.P3, stay_duration=7)
aurore = Member(name="Aurore", discount=Discount.P3, stay_duration=6)
claire = Member(name="Claire", discount=Discount.P2, stay_duration=7)
corentin = Member(name="Corentin", discount=Discount.P3, stay_duration=7)
delphin = Member(name="Delphin", discount=Discount.P2, stay_duration=6)
emilie = Member(name="Émilie", discount=Discount.P2, stay_duration=7)
francois = Member(name="François", discount=Discount.P1, stay_duration=7)
julie = Member(name="Julie", discount=Discount.P2, stay_duration=7)
lea = Member(name="Léa", discount=Discount.P3, stay_duration=6)
marylou = Member(name="Marylou", discount=Discount.P3, stay_duration=4)
oceane = Member(name="Océane", discount=Discount.P2, stay_duration=7)
olivier = Member(name="Olivier", discount=Discount.P2, stay_duration=6)
raph = Member(name="Raphaël", discount=Discount.P3, stay_duration=7)
remi = Member(name="Rémi", discount=Discount.P2, stay_duration=7)
sam = Member(name="Sam", discount=Discount.P3, stay_duration=4)
sophie = Member(name="Sophie", discount=Discount.P2, stay_duration=7)
thomas = Member(name="Thomas", discount=Discount.P3, stay_duration=7)
vincent = Member(name="Vincent", discount=Discount.P3, stay_duration=6)
virgile = Member(name="Virgile", discount=Discount.P3, stay_duration=6)
yael = Member(name="Yaël", discount=Discount.P1, stay_duration=7)

members = {
    alice,
    anouk,
    antoine,
    aurore,
    claire,
    corentin,
    delphin,
    emilie,
    francois,
    julie,
    lea,
    marylou,
    oceane,
    olivier,
    raph,
    remi,
    sam,
    sophie,
    thomas,
    vincent,
    virgile,
    yael,
}

days_skiing = {
    anouk: 3,
    olivier: 5,
    alice: 0,
    remi: 2,
    sophie: 4,
    francois: 3,
    thomas: 2,
    emilie: 3,
    corentin: 3,
    antoine: 2,
    lea: 0,
    virgile: 0,
    aurore: 0,
    vincent: 1,
    raph: 4,
    marylou: 4,
    claire: 2,
    yael: 4,
    oceane: 1,
    julie: 2,
    sam: 0,
    delphin: 3,
}


transactions = [
    Transaction(
        value=436,
        payer=francois,
        description="forfaits ski",
        members=days_skiing.keys(),
        weights=days_skiing,
    ),
    Transaction(
        value=44,
        payer=marylou,
        description="forfaits ski",
        members=days_skiing.keys(),
        weights=days_skiing,
    ),
    Transaction(
        value=16,
        payer=sophie,
        members={sophie, francois, remi},
        description="trajet retour",
    ),
    Transaction(
        value=16,
        description="trajet aller",
        payer=sophie,
        members={oceane, sophie, francois, remi},
    ),
    Transaction(
        value=24,
        description="Tarte Myrtilles refiuges",
        payer=oceane,
        members={yael, emilie, delphin, sophie},
    ),
    Transaction(
        value=150,
        description="Sauna Hammam Bien-être",
        payer=oceane,
        members={oceane, lea, aurore, delphin, anouk, sophie, claire, remi},
    ),
    Transaction(
        value=12,
        description="Tarte",
        payer=claire,
        members={yael, oceane, claire},
    ),
    Transaction(
        value=45,
        description="Chaussures",
        payer=francois,
        members={yael},
    ),
    Food(
        description="Vin",
        value=285,
        payer=antoine,
        members={
            oceane,
            corentin,
            lea,
            virgile,
            aurore,
            vincent,
            marylou,
            raph,
            delphin,
            thomas,
            sophie,
            sam,
            julie,
            claire,
            antoine,
            remi,
        },
    ),
    Transaction(
        description="Navette retour",
        value=13.2,
        payer=raph,
        members={raph, thomas, julie, claire},
    ),
    Food(
        description="Deuxième courses",
        value=339.25,
        payer=raph,
        members=members,
    ),
    Food(
        description="Pain",
        value=165.5,
        payer=sophie,
        members=members,
    ),
    Food(
        description="courses",
        value=17.8,
        payer=alice,
        members=members,
    ),
    Transaction(
        description="loc ski",
        value=12,
        payer=alice,
        members={claire},
    ),
    Transaction(
        description="Vacances Trièves",
        value=48.29,
        payer=remi,
        members={delphin},
    ),
    Transaction(
        description="Col du Lautaret",
        value=89.3,
        payer=emilie,
        members={emilie, corentin, antoine},
    ),
    Transaction(
        description="ski skting 02/01",
        value=15,
        payer=emilie,
        members={claire},
    ),
    Transaction(
        description="Comptes",
        value=20,
        payer=alice,
        members={delphin},
    ),
    Transaction(
        description="Comptes",
        value=40,
        payer=alice,
        members={anouk, olivier},
    ),
    Transaction(
        description="Cartes postales",
        value=5,
        payer=delphin,
        members={anouk, olivier},
    ),
    Transaction(
        description="cours de ski",
        value=98,
        payer=marylou,
        members={emilie, marylou, raph},
    ),
    Transaction(
        description="Location skis",
        value=30,
        payer=remi,
        members={julie, remi},
    ),
    Transaction(
        description="repas au Brec",
        value=39,
        payer=aurore,
        members={aurore, delphin},
    ),
    Food(
        description="drive carrefour",
        value=653,
        payer=aurore,
        members=members,
    ),
    Transaction(
        description="Emprunt Julie-Vincent", value=134, payer=vincent, members={julie}
    ),
    Food(
        description="Fromage",
        value=106,
        payer=vincent,
        members=members,
    ),
    Transaction(
        description="Bilets bus Delphin-Aurore-Vincent",
        value=30,
        payer=vincent,
        members={aurore, vincent, delphin},
    ),
    Housing(
        description="Taxe d'habitation",
        value=126,
        payer=vincent,
        members=members,
    ),
    Housing(
        description="Loyer",
        value=2964,
        payer=vincent,
        members=members,
    ),
    Food(
        description="Fromages",
        value=34,
        payer=remi,
        members=members,
    ),
    Food(
        description="Légumes",
        value=64,
        payer=remi,
        members=members,
    ),
]
