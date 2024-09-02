def longest_sequence(l):
    if not l:
        return 0
    if len(l) == 1:
        return 1
# first thing, the return if the condition are not satisfied;
    max_length = 1
    current_length = 1
# here is the syntax to loop throught the list;
    for i in range(1, len(l)):
        if l[i-1][1] == l[i][0]:
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 1

    return max_length

# Esempio di utilizzo
l = [(4,1),(1,2),(3,3),(3,5),(5,1),(1,4),(5,2),(2,1),(1,7)]
l2 = []
l3 = [(3,3)]
print("First test")
print(longest_sequence(l))  # Output: 4
print("Second test")
print(longest_sequence(l2))
print("Third test")
print(longest_sequence(l3))