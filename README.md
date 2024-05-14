# Chiffre_de_cesar
code python permettant d'effectuer le chiffrement de Cesar . 
Le chiffrement de Cesar est un chiffrement monoalphabetique
Il es classé dans la caégorie des chiffrement symetrique en cryptographie.
Le fonctionnement générale est le suivant: 
Etant donné un alphabet et une clé K ;
Soit un texte T(n) :
Le processus de chiffrement consiste a :
Pour tout caractere de T(n) on effectue un decallage en fonction de lq position et de la cle K. La formule est C(n)= (indice + k)%26 
Si on considere l'alphabet francaise, indice represente la position de l'element dans l'alphabet.
Exemple T(n)= bonjour k=3 , l'alphabet est francaise.
Pour B on a C(b)= (1 +3)%26=4 d'ou le noveau indice de b devient 4 donc b->e.
