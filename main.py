notes=[]
effectifs=[]
val_eff=[]
nombre=20
n=0
i=0
while n<=20:
  n=input("veuillez  saisir une valeur  ou écrire une valeur négatif pour arréter le programme: \n")
  if n!=0:
    n= float(n)
    notes.append(n)
    for i in range (len(notes)) :
      print("entrer l'effectif correspondant à la notes[i]")
      n=int(input())
      effectifs.append(n)
      for i in range (len(notes)) :
        val_eff.append(notes[i]*effectifs[i])
        m= sum(val_eff)/sum(effectifs )
        print("la liste des notes des éléves est:",notes)
        print("le nombre de note de cette liste est:",nombre)
        print("la note minimale de la liste est:",min(notes))
        print("la note maximale de la liste est:",max(notes))
        print("la moyenne est",m)