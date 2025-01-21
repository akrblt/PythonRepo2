

a=[1,2,3,4,5,6,7,8,9,0,1,2,3,4,5]

somme=0
for i in range(len(a)):
    print(a[i])
    numero = a[i]

    if(len(a)-i)%2 == 0:
        numero=numero*2
        if numero > 9:
            numero=numero-9
    somme=somme+numero
print(somme)

dernier_chiffre=10-somme%10
print("Derneier ciffre = ",dernier_chiffre)



