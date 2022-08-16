print('Digite o tipo de figura que deseja calcular a area:')
tipo_figura = int(input("1 Quadrado -- 2 Circulo -- 3 Triangulo"))


if tipo_figura == 1:
     lado = int(input("lado: "))
     result = lado * lado
     print(result)
elif tipo_figura == 2:
     raio = float(input('raio: '))
     circresultado = 3.14 * raio ** 2
     print(circresultado)
else:
     b = int(input("base:"))
     h = int(input("altura:"))
     triresultado = b * h /2


