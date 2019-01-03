# coding=utf-8
compte = open('fichier.rtf', 'r')
lst = []
for lig in compte :
    lst.append(int(lig))
argent = lst[0]
print ('bienvenue dans votre banque')
print ('choisissez votre mode')
print ("1-entrée d'argent")
print ("2-sortie d'argent")
mode = int(input())
if mode == 1:
    print('combien avez vous gagner?')
    entree = int(input())
    argent = argent + entree
elif mode == 2:
    print('combien avez vous depensé?')
    sortie = int(input())
    argent = argent - sortie
else:
    print('sortie du programe')
print('vous avez actuellement ', argent)
compte.close()
compte = open('fichier.rtf', 'w')
compte.write(str(argent))
compte.close()