input = "io saró stato"  # input("prompt: ")

parts = input.split(" ")

pronoun = parts[0]

verb = parts[1]

is_compound = False

if len(parts) > 2:
    is_compound = True

print(parts)

print(pronoun)

print(verb)

verbo = "essere"

modo = "indicativo"

tempo = "presente"

if is_compound:
    tempo = "passato prossimo"

essere_indicativo_presente = {
    "sono": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "sei": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "é": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "siamo": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "siete": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "sono": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
}

tempo = "imperfetto"

if is_compound:
    tempo = "trapassato prossimo"

essere_indicativo_imperfetto = {
    "ero": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "eri": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "era": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "eravamo": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "eravate": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "erano": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
}

tempo = "passato remoto"

if is_compound:
    tempo = "trapassato remoto"

essere_indicativo_passato_remoto = {
    "fui": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "fosti": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "fu": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "fummo": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "foste": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "furono": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
}

tempo = "futuro semplice"

if is_compound:
    tempo = "futuro anteriore"

essere_indicativo_futuro_semplice = {
    "saró": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "sarai": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "sará": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "saremo": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "sarete": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "saranno": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
}

if verb in essere_indicativo_presente:
    print("verbo:", essere_indicativo_presente[verb]["verbo"])
    print("modo:", essere_indicativo_presente[verb]["modo"])
    print("tempo:", essere_indicativo_presente[verb]["tempo"])
elif verb in essere_indicativo_imperfetto:
    print("verbo:", essere_indicativo_imperfetto[verb]["verbo"])
    print("modo:", essere_indicativo_imperfetto[verb]["modo"])
    print("tempo:", essere_indicativo_imperfetto[verb]["tempo"])
elif verb in essere_indicativo_passato_remoto:
    print("verbo:", essere_indicativo_passato_remoto[verb]["verbo"])
    print("modo:", essere_indicativo_passato_remoto[verb]["modo"])
    print("tempo:", essere_indicativo_passato_remoto[verb]["tempo"])
elif verb in essere_indicativo_futuro_semplice:
    print("verbo:", essere_indicativo_futuro_semplice[verb]["verbo"])
    print("modo:", essere_indicativo_futuro_semplice[verb]["modo"])
    print("tempo:", essere_indicativo_futuro_semplice[verb]["tempo"])
else:
    print("pee pee poo poo time")

essere_indicativo_presente_pronome = {
    "io": "1a singolare",
    "tu": "2a singolare",
    "egli": "3a singolare",
    "noi": "1a plurale",
    "voi": "2a plurale",
    "essi": "3a plurale",
}

if pronoun in essere_indicativo_presente_pronome:
    print(f"persona: {essere_indicativo_presente_pronome[pronoun]}")
else:
    print("pee pee shart")