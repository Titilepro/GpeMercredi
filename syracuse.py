def longueur_vol(n):
        '''retourne le nombre d'étapes avaant d'arriver à 1 dans la suite de syracuse'''
        assert type (n) == int and n >= 1
        compteur = 0
        while n >1 :
                print(n)
                if n % 2 == 0:
                        n = n // 2
                else:
                        n = 3 * n + 1
                compteur +=1
        print(n)
        return compteur

# Tests
assert longueur_vol(3) == 7 
#assert longueur_vol(7) == 16
#assert longueur_vol(1) == 0
print("bvo")
