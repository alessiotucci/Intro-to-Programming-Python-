def check_anagram(s1, s2):
	sorted1 = sorted(s1.lower().replace(" ", ""));
	sorted2 = sorted(s2.lower().replace(" ", ""));
	return (sorted1 == sorted2)

string1 = "silent"
string2 = "listEn"
string3 = "fake"
print(check_anagram(string1, string2))
print("* * *")
print(check_anagram(string1, string3))


ex1 = "Tom Marvolo Riddle"
ex2 = "I am Lord Voldemort"
print(check_anagram(ex1, ex2))