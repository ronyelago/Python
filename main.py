texto = open(r"C:\Workspace\Python\Python\arqs-06\arq4.in").readlines()

r = int(texto[0])
texto.pop(0)

assassinos = []
vitimas = []
detetives = []

i = 0
while i < r :
    a, v, d = texto[i].split()
    assassinos.append(a)
    vitimas.append(v)
    detetives.append(d)
    i += 1

todomundo = assassinos + vitimas + detetives
todomundo = list(set(todomundo))
todomundo.sort()

for p in todomundo :
    print(60 * "-")
    if p in vitimas :
        p += (" (in memorian):")
    if p in detetives:
        p += (": detetive")

    print(p)
