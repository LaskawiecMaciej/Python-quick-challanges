#PL Załóżmy że istnieje Kwadrat w który wpisany jest okrąg, w ten okrąg zaś, wpisany jest kolejny kwadrat - mniejszy. 
# Ten program oblicza różnicę miedzy polem mniejszego i większego kwadratu z podanej danej - promienia okręgu

# EN Suppose there is a Square in which a circle is inscribed, and in this circle another square is inscribed - a smaller one.
# This program calculates the difference between the area of ​​the smaller and larger square from the given data - the radius of the circle

import math
r=int(input("Podaj promień okręgu: "))
BigquareSide=(2 * r)
BigquareField=(BigquareSide ** 2)

SmallSquareDiagonal=(2 * r)
SmallSquareSide=(SmallSquareDiagonal / math.sqrt(2))
SmallSquareField=(SmallSquareSide ** 2)
print(f"Pole dużego kwadratu to: {BigquareField}, Pole małego kwadratu to: {SmallSquareField}")
print(f"Różnica między ich polami to: {BigquareField - SmallSquareField}")


