# Link Enunciado https://www.hackerrank.com/challenges/find-angle/problem?isFullScreen=true

import math

cateto1 = 10
cateto2 = 10

# Sabendo que a reta do ponto b ao ponto medio da hipotenusa formara um trianaulo
# isoceles, dado que a nova reta tera a mesma medida que metade da hipotenusa
# podemos dizer que o angulo de cbm sera o mesmo de bcm, portanto é so 
# calcular a tg de bca

grau = round(math.degrees(math.atan2(cateto1,cateto2)),0)
print(f"{grau:.0f}\u00b0")


