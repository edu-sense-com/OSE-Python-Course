print("To jest pierwsza linia.")

# komentarz - nic nie wnosi, poza informacjami
# definiujemy zmienne różnego typu
language = "Python"
year_of_birth = 1991
version = 3.8
is_cool = True

print("Computer language named:", language, end=" ")
print("was born in", year_of_birth, end=". ")
print("Now we use version", version, sep=":", end=" - ")
print("it is cool, isn't it", is_cool, sep="?")

# dane dla obliczeń
a = 10.4
b = 44
r = 27
h = 8
pi = 3.1415927

rectangle_area = a * b
rectangle_circumferance = 2 * a + 2 * b
triangle_area = (a * h) / 2
circle_area = pi * r * r
circle_circumferance = 2 * pi * r

print("Prostokąt:")
print("Pole", rectangle_area, "Obwód", rectangle_circumferance, sep=";")
print("Koło", end="-->")
print("Pole", circle_area, "Obwód", circle_circumferance, sep="*", end="!")
print("Pole trójkąta:", triangle_area)
