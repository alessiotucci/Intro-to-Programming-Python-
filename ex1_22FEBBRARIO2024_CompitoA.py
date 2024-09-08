def f(l):
    if not l:  # Se la lista è vuota, restituiamo -1
        return -1

    x = 0  # Contatore
    for index in range(len(l) - 1):
        # Primo controllo: l[i] == l[i+1]
        if l[index] == l[index + 1]:
            x += 1
        
        # Secondo controllo: l[i] == l[i+1].union(l[i+2]), controllando che ci sia un l[i+2]
        if index < len(l) - 2 and l[index] == l[index + 1].union(l[index + 2]):
            x += 1

    return x

# Test
test = [{5, 7, 2}, {5, 7}, {5, 2}, {5}, {5}, {2}, {5}, {7}]
print("Il risultato della funzione   è:", f(test))
