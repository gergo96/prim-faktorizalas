def primSzam(number):
    for oszto in range(2,number):
        if number % oszto == 0:
            #print("Nem prím szám")
            return False

    #print("Prím szám")
    return True

print(primSzam(65))
print(primSzam(107))

def faktorizalas(number):
    primek = []
    oszto = 2
    while number > 1:
        if primSzam(oszto):
            if number % oszto == 0:
                number = number / oszto
                primek.append(oszto)
            else:
                oszto += 1
        else:
            oszto += 1
    return primek




primek = faktorizalas(461)
print(primek)






