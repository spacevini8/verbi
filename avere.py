def def_indicativo_presente(verbo, modo, tempo):
    return {
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

def def_indicativo_imperfetto(verbo, modo, tempo): 
    return {
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

def def_indicativo_passato_remoto(verbo, modo, tempo): 
    return {
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

def def_indicativo_futuro_semplice(verbo, modo, tempo): 
    return {
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

def def_congiuntivo_presente(verbo, modo, tempo): 
    return {
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

def def_congiuntivo_imperfetto (verbo, modo, tempo):
    return {
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

def def_condizionale_presente(verbo, modo, tempo):
    return {
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

def def_imperativo_presente(verbo, modo, tempo): 
    return {
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

def def_infinito_presente(verbo, modo, tempo): 
    return {
        "avere": {
            "verbo": verbo,
            "modo": modo,
            "tempo": tempo,
        },
    }

def def_participio_presente(verbo, modo, tempo): 
    return {
        "avente": {
            "verbo": verbo,
            "modo": modo,
            "tempo": tempo,
        },
    }

def def_participio_passato(verbo, modo, tempo): 
    return {
        "avuto": {
            "verbo": verbo,
            "modo": modo,
            "tempo": tempo,
        },
    }

def def_gerundio_presente(verbo, modo, tempo): 
    return {
        "avendo": {
            "verbo": verbo,
            "modo": modo,
            "tempo": tempo,
        },
    }

def def_imperativo_presente_pronome(verbo, modo, tempo): 
    return {
        "abbi": "2a singolare",
        "abbia": "3a singolare",
        "abbiamo": "1a plurale",
        "abbiate": "2a plurale",
        "abbiano": "3a plurale",
    }