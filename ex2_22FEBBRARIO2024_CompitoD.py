import re
def f(file):
    # Definiamo le vocali
    vocali = "aeiou"
    pattern = r'([aeiou]{2})'

    # Variabile per contare le righe valide
    righe_valide = 0

    # Apriamo il file in modalità lettura
    with open(file, 'r') as f:
        # Iteriamo su ogni riga del file
        for riga in f:
            new_list = re.findall(pattern, riga)
            
            # Dizionario per contare le occorrenze delle coppie di vocali
            new_dict = {}
            for coppia in new_list:
                new_dict[coppia] = new_dict.get(coppia, 0) + 1

            # Verifichiamo se una delle coppie appare esattamente 3 volte
            if any(count == 3 for count in new_dict.values()):
                righe_valide += 1  # Se sì, incrementiamo il contatore delle righe valide

    return righe_valide

# Esegui la funzione con un file di esempio
file = 'testo.txt'  # Sostituisci con il nome del tuo file
print(f(file))
