def f(l):
    if not l:
        return -1

    x = 0
    for index in range(len(l) - 1):
        # Controllo l[i] == l[i+1]
        if l[index] == l[index + 1]:
            x += 1
        # Controllo l[i] == l[i+1] + l[i+2], assicurandosi che ci sia un l[i+2]
        if index < (len(l) - 2) and l[index] == l[index + 1] + l[index + 2]:
            x += 1

    return x

# Test
test = [352, 300, 52, 49, 1, 2, 2]
print("Il risultato della funzione è:", f(test))
