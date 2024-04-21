import re

def count_syllables(input_string):
    """The function takes a string as input and gives the number of syllables as output.

    Provided that the string is in Polish, of course.
    It is rule-based and works with a simple regex expression
    It is good enough rather than perfect.
    It is obviously wrong with some words.
    It counts all vowel except for the "i" that is followed by another vowel.
    For example, for "kiedy", it returns 2 ("e" and "y").
    For "bocian" also 2 ("o" and "a").
    Furthermore, it returns:
    # 3 for auto (wrong)
    # 3 for nauka (right)
    # 3 for mamma mia (wrong)
    # 7 for semiautomatyczny (incidentally right)
    # 5 for Guantanamo (wrong)
    # 5 for Nikaragua (right)
    # 6 for Baudelaire (guess it yourself)"""
    syllabic_vowels_pattern = r"(?i)(?!i[aeiouyóąę])[aeiouyóąę]"
    syllabic_vowels = re.finditer(syllabic_vowels_pattern, input_string)
    syllable_count = len(list(syllabic_vowels))
    return syllable_count

input_string = """Panno święta, co Jasnej bronisz Częstochowy
I w Ostrej świecisz Bramie! Ty, co gród zamkowy
Nowogródzki ochraniasz z jego wiernym ludem!
Jak mnie dziecko do zdrowia powróciłaś cudem
(Gdy od płaczącej matki, pod Twoją opiekę
Ofiarowany, martwą podniosłem powiekę;
I zaraz mogłem pieszo, do Twych świątyń progu
Iść za wrócone życie podziękować Bogu),
Tak nas powrócisz cudem na Ojczyzny łono.
Tymczasem przenoś moją duszę utęsknioną
Do tych pagórków leśnych, do tych łąk zielonych,
Szeroko nad błękitnym Niemnem rozciągnionych;
Do tych pól malowanych zbożem rozmaitem,
Wyzłacanych pszenicą, posrebrzanych żytem;
Gdzie bursztynowy świerzop, gryka jak śnieg biała,
Gdzie panieńskim rumieńcem dzięcielina pała,
A wszystko przepasane jakby wstęgą, miedzą
Zieloną, na niej z rzadka ciche grusze siedzą.

Wlazł kotek na płotek i mruga
Ładna to piosenka niedługa
Niedługa niekrótka lecz w sam raz
Zaśpiewaj koteczku jeszcze raz"""

split_string = input_string.split("\n")

for line in split_string:
    count = count_syllables(line)
    print("Number of syllables:", count)

l = ["guantanamo", "Baudelaire", "stroik"]

for e in l:
    count = count_syllables(e)
    print(f"Number of syllables: {count} :)")

