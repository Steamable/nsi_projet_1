choix = int(input("choisis un nombre\n"))

def entier_vers_egypt(entier):
    chiffres = [(1000000, "☺"),
            (100000, "♪"),
            (10000, "⌠"),
            (1000, "֍"),
            (100, "φ"),
            (10, "∩"),
            (1, "I")]

    list_egypt = []

    for number, symbol in chiffres:
        while entier >= number:
            entier -= number
            list_egypt.append(symbol)

    return " ".join(list_egypt)

print(entier_vers_egypt(choix))
