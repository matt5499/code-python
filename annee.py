 # Programme qui retourne si une annee est bissextile ou non
annee = input("Saississez une annee : ")
annee = int(annee)
bissextile = False
if annee % 4 == 0:
  bissextile = True
elif annee % 100 == 0:
	bissextile = False
elif annee % 4 == 0:
	bissextile = True
else: 
	bissextile = False

if bissextile:
	print("L'annee est bissextile.")
else:
	print("L'annee n'est pas bissextile.")
