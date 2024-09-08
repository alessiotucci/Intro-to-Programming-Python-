def f(filename):
    count = 0  # Contatore per le righe valide
    
    # Funzione di supporto per ottenere il carattere precedente e successivo in ordine alfabetico (Unicode)
    def char_before(c):
        return chr(ord(c) - 1)
    
    def char_after(c):
        return chr(ord(c) + 1)

    # Apriamo il file in modalità lettura
    with open(filename, 'r') as f:
        # Iteriamo su ogni riga
        for line in f:
            words = line.split()  # Dividiamo la riga in parole
            # Iteriamo su ogni sequenza di 3 parole consecutive
            for i in range(len(words) - 2):
                word1 = words[i]
                word2 = words[i + 1]
                word3 = words[i + 2]
                
                # Controllo se la seconda parola inizia con il carattere che precede l'ultima della prima parola
                if word2[0].lower() == char_before(word1[-1].lower()):
                    # Controllo se la seconda parola finisce con il carattere che segue la prima della terza parola
                    if word2[-1].lower() == char_after(word3[0].lower()):
                        count += 1  # Incrementiamo il contatore se la condizione è soddisfatta
                        break  # Uscita dal ciclo interno perché abbiamo trovato una sequenza valida in questa riga
    
    return count

# Eseguiamo la funzione con un file di esempio
file = 'test3.txt'
print(f(file))
