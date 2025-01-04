input = "dinglebob"

#input = input("prompt: ")

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

verbo = "avere"

modo = "indicativo"

tempo = "presente"

if is_compound:
    tempo = "passato prossimo"

avere_indicativo_presente = {
    "ho": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "hai": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "ha": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "abbiamo": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "avete": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "hanno": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
}

tempo = "imperfetto"

if is_compound:
    tempo = "trapassato prossimo"

avere_indicativo_imperfetto = {
    "avevo": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "avevi": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "aveva": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "avevamo": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "avevate": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "avevano": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
}

tempo = "passato remoto"

if is_compound:
    tempo = "trapassato remoto"

avere_indicativo_passato_remoto = {
    "ebbi": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "avesti": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "ebbe": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "avemmo": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "aveste": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "ebbero": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
}

tempo = "futuro semplice"

if is_compound:
    tempo = "futuro anteriore"

avere_indicativo_futuro_semplice = {
    "avró": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "avrai": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "avrá": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "avremo": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "avrete": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "avranno": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
}

modo = "congiuntivo"

tempo = "presente"

if is_compound:
    tempo = "passato"

avere_congiuntivo_presente = {
    "abbia": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "abbia": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "abbia": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "abbiamo": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "abbiate": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "abbiano": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
}

modo = "congiuntivo"

tempo = "imperfetto"

if is_compound:
    tempo = "trapassato"

avere_congiuntivo_imperfetto = {
    "avessi": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "avessi": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "avesse": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "avessimo": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "aveste": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "avessero": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
}

modo = "condizionale"

tempo = "presente"

if is_compound:
    tempo = "passato"

avere_condizionale_presente = {
    "avrei": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "avresti": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "avrebbe": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "avremmo": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "avreste": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
    "avrebbero": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
}

modo = "imperativo"

tempo = "presente"

avere_imperativo_presente = {
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

avere_infinito_presente = {
    "avere": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
}

modo = "participio"

tempo = "presente"

avere_participio_presente = {
    "avente": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
}

modo = "participio"

tempo = "passato"

avere_participio_passato = {
    "avuto": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
}

modo = "gerundio"

tempo = "presente"

if is_compound_indefiniti:
    tempo = "passato"

avere_gerundio_presente = {
    "avendo": {
        "verbo": verbo,
        "modo": modo,
        "tempo": tempo,
    },
}

if verb in avere_indicativo_presente and is_congiuntivo == False:
    print("verbo:", avere_indicativo_presente[verb]["verbo"])
    print("modo:", avere_indicativo_presente[verb]["modo"])
    print("tempo:", avere_indicativo_presente[verb]["tempo"])
elif verb in avere_indicativo_imperfetto and is_congiuntivo == False:
    print("verbo:", avere_indicativo_imperfetto[verb]["verbo"])
    print("modo:", avere_indicativo_imperfetto[verb]["modo"])
    print("tempo:", avere_indicativo_imperfetto[verb]["tempo"])
elif verb in avere_indicativo_passato_remoto and is_congiuntivo == False:
    print("verbo:", avere_indicativo_passato_remoto[verb]["verbo"])
    print("modo:", avere_indicativo_passato_remoto[verb]["modo"])
    print("tempo:", avere_indicativo_passato_remoto[verb]["tempo"])
elif verb in avere_indicativo_futuro_semplice and is_congiuntivo == False:
    print("verbo:", avere_indicativo_futuro_semplice[verb]["verbo"])
    print("modo:", avere_indicativo_futuro_semplice[verb]["modo"])
    print("tempo:", avere_indicativo_futuro_semplice[verb]["tempo"])
elif verb in avere_congiuntivo_presente and is_congiuntivo == True:
    print("verbo:", avere_congiuntivo_presente[verb]["verbo"])
    print("modo:", avere_congiuntivo_presente[verb]["modo"])
    print("tempo:", avere_congiuntivo_presente[verb]["tempo"])
elif verb in avere_congiuntivo_imperfetto and is_congiuntivo == True:
    print("verbo:", avere_congiuntivo_imperfetto[verb]["verbo"])
    print("modo:", avere_congiuntivo_imperfetto[verb]["modo"])
    print("tempo:", avere_congiuntivo_imperfetto[verb]["tempo"])
elif verb in avere_condizionale_presente and is_congiuntivo == False:
    print("verbo:", avere_condizionale_presente[verb]["verbo"])
    print("modo:", avere_condizionale_presente[verb]["modo"])
    print("tempo:", avere_condizionale_presente[verb]["tempo"])
elif verb in avere_imperativo_presente and is_congiuntivo == False:
    print("verbo:", avere_imperativo_presente[verb]["verbo"])
    print("modo:", avere_imperativo_presente[verb]["modo"])
    print("tempo:", avere_imperativo_presente[verb]["tempo"])
elif pronoun in avere_infinito_presente and is_congiuntivo == False:
    print("verbo:", avere_infinito_presente[pronoun]["verbo"])
    print("modo:", avere_infinito_presente[pronoun]["modo"])
    print("tempo:", avere_infinito_presente[pronoun]["tempo"])
elif verb in avere_participio_presente and is_congiuntivo == False:
    print("verbo:", avere_participio_presente[verb]["verbo"])
    print("modo:", avere_participio_presente[verb]["modo"])
    print("tempo:", avere_participio_presente[verb]["tempo"])
elif verb in avere_participio_passato and is_congiuntivo == False:
    print("verbo:", avere_participio_passato[verb]["verbo"])
    print("modo:", avere_participio_passato[verb]["modo"])
    print("tempo:", avere_participio_passato[verb]["tempo"])
elif verb in avere_gerundio_presente and is_congiuntivo == False:
    print("verbo:", avere_gerundio_presente[verb]["verbo"])
    print("modo:", avere_gerundio_presente[verb]["modo"])
    print("tempo:", avere_gerundio_presente[verb]["tempo"])
else:
    print("errore_verbo")

avere_indicativo_presente_pronome = {
    "io": "1a singolare",
    "tu": "2a singolare",
    "egli": "3a singolare",
    "noi": "1a plurale",
    "voi": "2a plurale",
    "essi": "3a plurale",
}

avere_imperativo_presente_pronome = {
    "abbi": "2a singolare",
    "abbia": "3a singolare",
    "abbiamo": "1a plurale",
    "abbiate": "2a plurale",
    "abbiano": "3a plurale",
}

if pronoun in avere_indicativo_presente_pronome:
    print(f"persona: {avere_indicativo_presente_pronome[pronoun]}")
elif pronoun in avere_imperativo_presente_pronome:
    print(f"persona: {avere_imperativo_presente_pronome[pronoun]}")
elif modo == "infinito" or modo == "participio" or modo == "gerundio":
    print("persona: 1a singolare")
else:
    print("errore_pronome")

waltuh = """
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠆⠜⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⠿⠿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿⣿⣿⣿
⣿⣿⡏⠁⠀⠀⠀⠀⠀⣀⣠⣤⣤⣶⣶⣶⣶⣶⣦⣤⡄⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿
⣿⣿⣷⣄⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⡧⠇⢀⣤⣶⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣾⣮⣭⣿⡻⣽⣒⠀⣤⣜⣭⠐⢐⣒⠢⢰⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣏⣿⣿⣿⣿⣿⣿⡟⣾⣿⠂⢈⢿⣷⣞⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣷⣶⣾⡿⠿⣿⠗⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠻⠋⠉⠑⠀⠀⢘⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡿⠟⢹⣿⣿⡇⢀⣶⣶⠴⠶⠀⠀⢽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡿⠀⠀⢸⣿⣿⠀⠀⠣⠀⠀⠀⠀⠀⡟⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⡿⠟⠋⠀⠀⠀⠀⠹⣿⣧⣀⠀⠀⠀⠀⡀⣴⠁⢘⡙⢿⣿⣿⣿⣿⣿⣿⣿⣿
⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⠗⠂⠄⠀⣴⡟⠀⠀⡃⠀⠉⠉⠟⡿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢷⠾⠛⠂⢹⠀⠀⠀⢡⠀⠀⠀⠀⠀⠙⠛⠿⢿
"""

if input == ("let's cook"):
    print(waltuh)