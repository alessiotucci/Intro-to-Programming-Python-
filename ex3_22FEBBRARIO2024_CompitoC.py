def calcola_produzione(file, d):
    magazzino = {}  # Dizionario per memorizzare le informazioni del magazzino

    # Leggiamo il file e popoliamo il dizionario del magazzino
    with open(file, 'r') as f:
        next(f)
        for riga in f:
            # Splittiamo ogni riga in NomeComponente, quantità e prezzo
            componente, quantita, prezzo = riga.strip().split(',')
            magazzino[componente] = {'quantita': int(quantita), 'prezzo': int(prezzo)}

    # Variabili per il calcolo del numero massimo di copie e del costo
    max_copie = float('inf')  # Valore molto grande inizialmente, verrà ridotto
    costo_totale = 0

    # Iteriamo su ogni componente richiesto dal dizionario d
    for componente, numero_richiesto in d.items():
        # Controlliamo se il componente esiste nel magazzino
        if componente in magazzino:
            disponibilita = magazzino[componente]['quantita']
            prezzo_unita = magazzino[componente]['prezzo']
            
            # Calcoliamo quante copie massime possiamo costruire con questo componente
            copie_possibili = disponibilita // numero_richiesto
            
            # Aggiorniamo il numero massimo di copie prendendo il minimo tra i componenti
            max_copie = min(max_copie, copie_possibili)
            
            # Aggiungiamo al costo totale il costo di questo componente per una singola copia
            costo_totale += numero_richiesto * prezzo_unita
        else:
            # Se manca un componente, non possiamo costruire l'oggetto
            return (0, 0)

    # Restituiamo il numero massimo di copie e il costo di una singola copia
    return (max_copie, costo_totale)

# Esempio di utilizzo
file = 'componenti.txt'
d = {'gambeCorte': 2, 'gambeLunghe': 2, 'viti': 8, 'seduta': 1}

print(calcola_produzione(file, d))
