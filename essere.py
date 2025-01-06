def def_indicativo_presente(verbo, modo, tempo):
    return {
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

def def_indicativo_imperfetto(verbo, modo, tempo): 
    return {
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

def def_indicativo_passato_remoto(verbo, modo, tempo): 
    return {
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

def def_indicativo_futuro_semplice(verbo, modo, tempo): 
    return {
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

def def_congiuntivo_presente(verbo, modo, tempo): 
    return {
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

def def_congiuntivo_imperfetto (verbo, modo, tempo):
    return {
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

def def_condizionale_presente(verbo, modo, tempo):
    return {
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
        "essere": {
            "verbo": verbo,
            "modo": modo,
            "tempo": tempo,
        },
    }

def def_participio_presente(verbo, modo, tempo): 
    return {
        "ente": {
            "verbo": verbo,
            "modo": modo,
            "tempo": tempo,
        },
    }

def def_participio_passato(verbo, modo, tempo): 
    return {
        "stato": {
            "verbo": verbo,
            "modo": modo,
            "tempo": tempo,
        },
    }

def def_gerundio_presente(verbo, modo, tempo): 
    return {
        "essendo": {
            "verbo": verbo,
            "modo": modo,
            "tempo": tempo,
        },
    }

def def_imperativo_presente_pronome(verbo, modo, tempo): 
    return {
        "sii": "2a singolare",
        "sia": "3a singolare",
        "siamo": "1a plurale",
        "siate": "2a plurale",
        "siano": "3a plurale",
    }