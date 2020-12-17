from ygoprodeck import YGOPro

ygo = YGOPro()

cards = ygo.get_cards()["data"]

series = {
    "Duel Terminal": [
        "Gem-Knight",
        "Laval",
        "Gishki",
        "Gusto",
        "Tellarknight",
        "Shaddoll",
        "Zefra",
        "Nekroz",
        "Steelswarm",
        "Evilswarm",
        "Dragunity",
        "Ice Barrier",
        "Flamvell",
        "Ally of Justice",
        "Genex",
        "Yang Zing",
        "Mist Valley",
        "Ritual Beast",
        "Fabled",
        "Jurrac",
        "X-Saber"
    ], 
    "True Draco" : [
        "True Draco",
        "True King",
        "Dracoslayer",
        "Dracoverlord",
        "Igknight",
        "Dinomist",
        "Majespecter",
        "Amorphage",
        "Metalfoes",
        "Crystron",
        "Zoodiac",
    ],
    "World Legacy": [
        "World Legacy",
        "World Chalice",
        "Krawler",
        "Mekk-Knight",
        "Orcust",
        "Guardragon",
        "Crusadia",
        "Knightmare",
    ],
}

names = {
    serie: {
        archetype: [
            card["name"]
            for card in cards
            if "Monster" in card["type"]
            and archetype.lower() in card["name"].lower()
        ] for archetype in sorted(series[serie])
    } for serie in sorted(series)
} 

print(names)
