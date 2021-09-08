
#voornaam: Abdullah
#achternaam: Al Kathiry
#opdracht: Pizza calculator


SmallPizaMargrita = 10
MediumPizaMargrita = 15
BigPizaMargrita = 18

print("Pizza calculator")
print("................")
print("Small pizza margrita 25 cm = 10 euro ")
print("Medium pizza margrita 35 cm = 15 euro ")
print("Big pizza margrita 45 cm = 18 euro ")
print("................")


AantalSmallPizaMargrita = int(input("Aantal small pizza"))
totalsmall = AantalSmallPizaMargrita * SmallPizaMargrita
print(AantalSmallPizaMargrita * SmallPizaMargrita)
print(".................")

AantalMediumPizaMargrita = int(input("Aantal medium pizza"))
totalmedium = AantalMediumPizaMargrita * MediumPizaMargrita
print(AantalMediumPizaMargrita * MediumPizaMargrita)
print(".................")

AantalBigPizaMargrita = int(input("Aantal big pizza"))
totalbig = AantalBigPizaMargrita * BigPizaMargrita
print(".................")
print(AantalBigPizaMargrita * BigPizaMargrita)

print(".........")
print("total")
print(totalsmall + totalmedium + totalbig )
print(".........")
