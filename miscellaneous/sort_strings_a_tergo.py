longstring = """Bałkany
Bielice
Burbonowie
Czejeni
Drzewianie
Gidle
Herby
Jedlicze
Karpaty
Komi
Kujbyszewe
Łazy
Melchici
Mosty
Obodryci
Pardubice
Podole
Pyrzyce
Rychliki
Siedlce
Soleczniki
Szawle
Tomaszewski"""

a_tergo_sorted_list = longstring.split("\n")

a_tergo_sorted_list.sort(key=lambda x: x[::-1])

for e in a_tergo_sorted_list:
    print(e)

# output:
#    Pardubice
#    Bielice
#    Siedlce
#    Pyrzyce
#    Drzewianie
#    Burbonowie
#    Gidle
#    Podole
#    Szawle
#    Kujbyszewe
#    Jedlicze
#    Melchici
#    Obodryci
#    Rychliki
#    Soleczniki
#    Tomaszewski
#    Komi
#    Czejeni
#    Herby
#    Bałkany
#    Karpaty
#    Mosty
#    Łazy