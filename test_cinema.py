sexe_personne = str(input(print("quel est votre sexe?(male,female)")))
age_personne = int(input(print("quel est votre age")))
if age_personne >= 18 :
    prix_total = int(12)
    print("votre place coute", prix_total,"€")
else :
    prix_total = int(7)
    print("votre place coute", prix_total,"€")
pop_corn = input(print("voulez vous du popcorn ?(oui , non)"))
if (pop_corn == "oui") :
    prix_total += int(5)


if sexe_personne  == "male" :
    if age_personne >= 18 :
        print("votre place coute", prix_total,"€ monsieur")
    else :
        print("votre place coute" , prix_total,"€ jeune homme")
else:
    if age_personne >= 18 :
        print("votre place coute", prix_total,"€ madame")
    else :
        print("votre place coute", prix_total,"€ jeune femme")