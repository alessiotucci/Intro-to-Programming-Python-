def f(s, l):
    if not s:  # Se la stringa è vuota, restituiamo la lista vuota
        return []
    parole_tratteggiate = s.split('-')  # Separiamo la stringa in parole
    indici = []  # Lista per memorizzare gli indici delle parole in 'l'
    for parola in parole_tratteggiate:
        # Convertiamo la prima lettera in minuscolo per confrontarla con le parole nella lista 'l'
        parola_minuscola = parola[0].lower() + parola[1:]
        if parola_minuscola in l:
            # Se la parola esiste nella lista, ne salviamo l'indice
            indici.append(l.index(parola_minuscola))
        else:
            # Se non troviamo la parola, restituiamo "Impossibile"
            return "Impossibile"
    
    return indici

# Test
s = 'Canto-Piano-Tacco'
l = ['canto', 'conta', 'piano', 'tacco']
print(f(s, l))  # Output: [0, 2, 2]
