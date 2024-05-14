def chiffrement_cesar(texte, decalage, alphabet):
    texte_chiffre = ""
    taille_alphabet= len(alphabet)

    for char in texte : 
        if char in alphabet :
            indice= alphabet.index(char)
            new_indice = (indice + decalage) % taille_alphabet
            texte_chiffre += alphabet[new_indice]
        else :
            texte_chiffre += char
    return texte_chiffre

alphabet_fancais="abcdefghijklmnopqrstuvwxyz"
texte= input("entrer le texte a chiffrer")
decalage= int(input("entrer la taile du decalage"))

texte_chiffre= chiffrement_cesar(texte, decalage, alphabet_fancais)
print("le texte chiffre est ", texte_chiffre)
