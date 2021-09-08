Aantalcroissantjes = 17
Aantalstokbroden = 2
Aantalkortingsbonnen = 3

croissantjes = 0.39
print("croissantjes 0.39")
croissant = int(input("geef aantal stuks")) 
print(croissant * croissantjes)

stokbroden  =  2.78
print("stokbroden 2.78")
stokbrodenstuks  =  int(input("geef aantal stuks"))
print(stokbrodenstuks * stokbroden) 

korting = 0.50
print("kortingsbonnen 0.50")
kortingsbonnen = int(input("geef aantal stuks"))
print(kortingsbonnen * korting) 

print("tottal")
print(stokbrodenstuks * stokbroden + croissant * croissantjes - kortingsbonnen * korting )


print("De feestlunch kost je bij de bakker 10.69 euro voor de 17 croissantjes en de 2 stokbroden als de 3 kortingsbonnen nog geldig zijn!")