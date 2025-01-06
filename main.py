import sys

while True:
    print("seleziona verbo:")
    print("1) essere")
    print("2) avere")
    print("3) amare")
    print("4) sentire")
    print("5) temere")
    print("q) uscita")

    input_verbo = input("numero del verbo: ")

    is_ausiliare = False

    if input_verbo == "1":
        import essere as def_verbo
        verbo = "essere"
        is_ausiliare = True
        #input = "io sono"
    elif input_verbo == "2":
        import avere as def_verbo
        verbo = "avere"
        is_ausiliare = True
        #input = "io ho"
    elif input_verbo == "3":
        import amare as def_verbo
        verbo = "amare"
        #input = "io ho"
        #print("WIP")
    elif input_verbo == "4":
        import sentire as def_verbo
        verbo = "sentire"
        #input = "io ho"
        #print("WIP")
    elif input_verbo == "5":
        import temere as def_verbo
        verbo = "temere"
        #input = "io ho"
        #print("WIP")
    elif input_verbo == "q":
        sys.exit(0)
    else:
        print("input e invalido")
        continue

    input_question = input("verbo: ")

    parts = input_question.split(" ")

    is_congiuntivo = False

    is_compound_indefiniti = False

    if parts[0] == "che":
        input_question = input_question.replace("che ", "")
        parts = input_question.split(" ")
        is_congiuntivo = True

    pronoun = parts[0]

    if len(parts) > 1:
        verb = parts[1]
    else:
        verb = parts[0]

    is_compound = False

    if len(parts) > 2:
        is_compound = True

    if len(parts) > 2 and is_ausiliare == False:
        is_compound = True
        import avere as def_verbo

    if len(parts) > 1:
        is_compound_indefiniti = True

    print(parts)

    print(pronoun)

    print(verb)

    modo = "indicativo"

    tempo = "presente"

    if is_compound:
        tempo = "passato prossimo"

    #from essere import def_essere_indicativo_presente

    indicativo_presente = def_verbo.def_indicativo_presente(verbo, modo, tempo)

    tempo = "imperfetto"

    if is_compound:
        tempo = "trapassato prossimo"

    indicativo_imperfetto = def_verbo.def_indicativo_imperfetto(verbo, modo, tempo)

    tempo = "passato remoto"

    if is_compound:
        tempo = "trapassato remoto"

    indicativo_passato_remoto = def_verbo.def_indicativo_passato_remoto(verbo, modo, tempo)

    tempo = "futuro semplice"

    if is_compound:
        tempo = "futuro anteriore"

    indicativo_futuro_semplice = def_verbo.def_indicativo_futuro_semplice(verbo, modo, tempo)

    modo = "congiuntivo"

    tempo = "presente"

    if is_compound:
        tempo = "passato"

    congiuntivo_presente = def_verbo.def_congiuntivo_presente(verbo, modo, tempo)

    modo = "congiuntivo"

    tempo = "imperfetto"

    if is_compound:
        tempo = "trapassato"

    congiuntivo_imperfetto = def_verbo.def_congiuntivo_imperfetto(verbo, modo, tempo)

    modo = "condizionale"

    tempo = "presente"

    if is_compound:
        tempo = "passato"

    condizionale_presente = def_verbo.def_condizionale_presente(verbo, modo, tempo)

    modo = "imperativo"

    tempo = "presente"

    imperativo_presente = def_verbo.def_imperativo_presente(verbo, modo, tempo)

    modo = "infinito"

    tempo = "presente"

    if is_compound_indefiniti:
        tempo = "passato"

    infinito_presente = def_verbo.def_infinito_presente(verbo, modo, tempo)

    modo = "participio"

    tempo = "presente"

    participio_presente = def_verbo.def_participio_presente(verbo, modo, tempo)

    modo = "participio"

    tempo = "passato"

    participio_passato = def_verbo.def_participio_passato(verbo, modo, tempo)

    modo = "gerundio"

    tempo = "presente"

    if is_compound_indefiniti:
        tempo = "passato"

    gerundio_presente = def_verbo.def_gerundio_presente(verbo, modo, tempo)

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

    imperativo_presente_pronome = def_verbo.def_imperativo_presente_pronome(verbo, modo, tempo)

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

    if input_question == ("let's cook") or input_question == ("we need to cook") or input_question == ("jesse, we need to cook"):
        print(waltuh)

    input_fine = input("continua o esci? ")

    if input_fine == "esci":
        sys.exit(0)
