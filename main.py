import essere

input = "io ero stato"

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

verbo = "essere"

modo = "indicativo"

tempo = "presente"

if is_compound:
    tempo = "passato prossimo"

#from essere import def_essere_indicativo_presente

indicativo_presente = essere.def_essere_indicativo_presente(verbo, modo, tempo)

tempo = "imperfetto"

if is_compound:
    tempo = "trapassato prossimo"

indicativo_imperfetto = essere.def_essere_indicativo_imperfetto(verbo, modo, tempo)

tempo = "passato remoto"

if is_compound:
    tempo = "trapassato remoto"

indicativo_passato_remoto = essere.def_essere_indicativo_passato_remoto(verbo, modo, tempo)

tempo = "futuro semplice"

if is_compound:
    tempo = "futuro anteriore"

indicativo_futuro_semplice = essere.def_essere_indicativo_futuro_semplice(verbo, modo, tempo)

modo = "congiuntivo"

tempo = "presente"

if is_compound:
    tempo = "passato"

congiuntivo_presente = essere.def_essere_congiuntivo_presente(verbo, modo, tempo)

modo = "congiuntivo"

tempo = "imperfetto"

if is_compound:
    tempo = "trapassato"

congiuntivo_imperfetto = essere.def_essere_congiuntivo_imperfetto(verbo, modo, tempo)

modo = "condizionale"

tempo = "presente"

if is_compound:
    tempo = "passato"

condizionale_presente = essere.def_essere_condizionale_presente(verbo, modo, tempo)

modo = "imperativo"

tempo = "presente"

imperativo_presente = essere.def_essere_imperativo_presente(verbo, modo, tempo)

modo = "infinito"

tempo = "presente"

if is_compound_indefiniti:
    tempo = "passato"

infinito_presente = essere.def_essere_infinito_presente(verbo, modo, tempo)

modo = "participio"

tempo = "presente"

participio_presente = essere.def_essere_participio_presente(verbo, modo, tempo)

modo = "participio"

tempo = "passato"

participio_passato = essere.def_essere_participio_passato(verbo, modo, tempo)

modo = "gerundio"

tempo = "presente"

if is_compound_indefiniti:
    tempo = "passato"

gerundio_presente = essere.def_essere_gerundio_presente(verbo, modo, tempo)

if verb in indicativo_presente and is_congiuntivo == False:
    print("verbo:", indicativo_presente[verb]["verbo"])
    print("modo:", indicativo_presente[verb]["modo"])
    print("tempo:", indicativo_presente[verb]["tempo"])
elif verb in indicativo_imperfetto and is_congiuntivo == False:
    print("verbo:", indicativo_imperfetto[verb]["verbo"])
    print("modo:", indicativo_imperfetto[verb]["modo"])
    print("tempo:", indicativo_imperfetto[verb]["tempo"])
elif verb in indicativo_passato_remoto and is_congiuntivo == False:
    print("verbo:", indicativo_passato_remoto[verb]["verbo"])
    print("modo:", indicativo_passato_remoto[verb]["modo"])
    print("tempo:", indicativo_passato_remoto[verb]["tempo"])
elif verb in indicativo_futuro_semplice and is_congiuntivo == False:
    print("verbo:", indicativo_futuro_semplice[verb]["verbo"])
    print("modo:", indicativo_futuro_semplice[verb]["modo"])
    print("tempo:", indicativo_futuro_semplice[verb]["tempo"])
elif verb in congiuntivo_presente and is_congiuntivo == True:
    print("verbo:", congiuntivo_presente[verb]["verbo"])
    print("modo:", congiuntivo_presente[verb]["modo"])
    print("tempo:", congiuntivo_presente[verb]["tempo"])
elif verb in congiuntivo_imperfetto and is_congiuntivo == True:
    print("verbo:", congiuntivo_imperfetto[verb]["verbo"])
    print("modo:", congiuntivo_imperfetto[verb]["modo"])
    print("tempo:", congiuntivo_imperfetto[verb]["tempo"])
elif verb in condizionale_presente and is_congiuntivo == False:
    print("verbo:", condizionale_presente[verb]["verbo"])
    print("modo:", condizionale_presente[verb]["modo"])
    print("tempo:", condizionale_presente[verb]["tempo"])
elif verb in imperativo_presente and is_congiuntivo == False:
    print("verbo:", imperativo_presente[verb]["verbo"])
    print("modo:", imperativo_presente[verb]["modo"])
    print("tempo:", imperativo_presente[verb]["tempo"])
elif pronoun in infinito_presente and is_congiuntivo == False:
    print("verbo:", infinito_presente[pronoun]["verbo"])
    print("modo:", infinito_presente[pronoun]["modo"])
    print("tempo:", infinito_presente[pronoun]["tempo"])
elif verb in participio_presente and is_congiuntivo == False:
    print("verbo:", participio_presente[verb]["verbo"])
    print("modo:", participio_presente[verb]["modo"])
    print("tempo:", participio_presente[verb]["tempo"])
elif verb in participio_passato and is_congiuntivo == False:
    print("verbo:", participio_passato[verb]["verbo"])
    print("modo:", participio_passato[verb]["modo"])
    print("tempo:", participio_passato[verb]["tempo"])
elif verb in gerundio_presente and is_congiuntivo == False:
    print("verbo:", gerundio_presente[verb]["verbo"])
    print("modo:", gerundio_presente[verb]["modo"])
    print("tempo:", gerundio_presente[verb]["tempo"])
else:
    print("errore_verbo")

pronome = {
    "io": "1a singolare",
    "tu": "2a singolare",
    "egli": "3a singolare",
    "noi": "1a plurale",
    "voi": "2a plurale",
    "essi": "3a plurale",
}

imperativo_presente_pronome = essere.def_essere_imperativo_presente_pronome(verbo, modo, tempo)

if pronoun in pronome:
    print(f"persona: {pronome[pronoun]}")
elif pronoun in imperativo_presente_pronome:
    print(f"persona: {imperativo_presente_pronome[pronoun]}")
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

if input == ("let's cook") or input == ("we need to cook") or input == ("jesse, we need to cook"):
    print(waltuh)