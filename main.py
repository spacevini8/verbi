input = "essendo"  # input("prompt: ")

parts = input.split(" ")

is_congiuntivo = False

is_compound_indefiniti = False

if parts[0] == "che":
    input = input.replace("che ", "")
    parts = input.split(" ")
    is_congiuntivo = True

pronoun = parts[0]

if len(parts) > 1:
    verb = parts[1]
else:
    verb = parts[0]

is_compound = False

if len(parts) > 2:
    is_compound = True

if len(parts) > 1:
    is_compound_indefiniti = True

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

modo = "congiuntivo"

tempo = "presente"

if is_compound:
    tempo = "passato"

essere_congiuntivo_presente = {
    "sia": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "sia": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "sia": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "siamo": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "siate": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "siano": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
}

modo = "congiuntivo"

tempo = "imperfetto"

if is_compound:
    tempo = "trapassato"

essere_congiuntivo_imperfetto = {
    "fossi": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "fossi": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "fosse": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "fossimo": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "foste": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "fossero": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
}

modo = "condizionale"

tempo = "presente"

if is_compound:
    tempo = "passato"

essere_condizionale_presente = {
    "sarei": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "saresti": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "sarebbe": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "saremmo": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "sareste": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "sarebbero": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
}

modo = "imperativo"

tempo = "presente"

essere_imperativo_presente = {
    "sarei": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "tu": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "egli": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "noi": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "voi": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "essi": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
}

modo = "infinito"

tempo = "presente"

if is_compound_indefiniti:
    tempo = "passato"

essere_infinito_presente = {
    "essere": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
}

modo = "participio"

tempo = "presente"

essere_participio_presente = {
    "ente": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
}

modo = "participio"

tempo = "passato"

essere_participio_passato = {
    "stato": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
}

modo = "gerundio"

tempo = "presente"

if is_compound_indefiniti:
    tempo = "passato"

essere_gerundio_presente = {
    "essendo": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
}

if verb in essere_indicativo_presente and is_congiuntivo == False:
    print("verbo:", essere_indicativo_presente[verb]["verbo"])
    print("modo:", essere_indicativo_presente[verb]["modo"])
    print("tempo:", essere_indicativo_presente[verb]["tempo"])
elif verb in essere_indicativo_imperfetto and is_congiuntivo == False:
    print("verbo:", essere_indicativo_imperfetto[verb]["verbo"])
    print("modo:", essere_indicativo_imperfetto[verb]["modo"])
    print("tempo:", essere_indicativo_imperfetto[verb]["tempo"])
elif verb in essere_indicativo_passato_remoto and is_congiuntivo == False:
    print("verbo:", essere_indicativo_passato_remoto[verb]["verbo"])
    print("modo:", essere_indicativo_passato_remoto[verb]["modo"])
    print("tempo:", essere_indicativo_passato_remoto[verb]["tempo"])
elif verb in essere_indicativo_futuro_semplice and is_congiuntivo == False:
    print("verbo:", essere_indicativo_futuro_semplice[verb]["verbo"])
    print("modo:", essere_indicativo_futuro_semplice[verb]["modo"])
    print("tempo:", essere_indicativo_futuro_semplice[verb]["tempo"])
elif verb in essere_congiuntivo_presente and is_congiuntivo == True:
    print("verbo:", essere_congiuntivo_presente[verb]["verbo"])
    print("modo:", essere_congiuntivo_presente[verb]["modo"])
    print("tempo:", essere_congiuntivo_presente[verb]["tempo"])
elif verb in essere_congiuntivo_imperfetto and is_congiuntivo == True:
    print("verbo:", essere_congiuntivo_imperfetto[verb]["verbo"])
    print("modo:", essere_congiuntivo_imperfetto[verb]["modo"])
    print("tempo:", essere_congiuntivo_imperfetto[verb]["tempo"])
elif verb in essere_condizionale_presente and is_congiuntivo == False:
    print("verbo:", essere_condizionale_presente[verb]["verbo"])
    print("modo:", essere_condizionale_presente[verb]["modo"])
    print("tempo:", essere_condizionale_presente[verb]["tempo"])
elif verb in essere_imperativo_presente and is_congiuntivo == False:
    print("verbo:", essere_imperativo_presente[verb]["verbo"])
    print("modo:", essere_imperativo_presente[verb]["modo"])
    print("tempo:", essere_imperativo_presente[verb]["tempo"])
elif pronoun in essere_infinito_presente and is_congiuntivo == False:
    print("verbo:", essere_infinito_presente[pronoun]["verbo"])
    print("modo:", essere_infinito_presente[pronoun]["modo"])
    print("tempo:", essere_infinito_presente[pronoun]["tempo"])
elif verb in essere_participio_presente and is_congiuntivo == False:
    print("verbo:", essere_participio_presente[verb]["verbo"])
    print("modo:", essere_participio_presente[verb]["modo"])
    print("tempo:", essere_participio_presente[verb]["tempo"])
elif verb in essere_participio_passato and is_congiuntivo == False:
    print("verbo:", essere_participio_passato[verb]["verbo"])
    print("modo:", essere_participio_passato[verb]["modo"])
    print("tempo:", essere_participio_passato[verb]["tempo"])
elif verb in essere_gerundio_presente and is_congiuntivo == False:
    print("verbo:", essere_gerundio_presente[verb]["verbo"])
    print("modo:", essere_gerundio_presente[verb]["modo"])
    print("tempo:", essere_gerundio_presente[verb]["tempo"])
else:
    print("errore_verbo")

essere_indicativo_presente_pronome = {
    "io": "1a singolare",
    "tu": "2a singolare",
    "egli": "3a singolare",
    "noi": "1a plurale",
    "voi": "2a plurale",
    "essi": "3a plurale",
}

essere_imperativo_presente_pronome = {
    "sii": "2a singolare",
    "sia": "3a singolare",
    "siamo": "1a plurale",
    "siate": "2a plurale",
    "siano": "3a plurale",
}

if pronoun in essere_indicativo_presente_pronome:
    print(f"persona: {essere_indicativo_presente_pronome[pronoun]}")
elif pronoun in essere_imperativo_presente_pronome:
    print(f"persona: {essere_imperativo_presente_pronome[pronoun]}")
elif modo == "infinito" or modo == "participio" or modo == "gerundio":
    print("persona: 1a singolare")
else:
    print("errore_pronome")