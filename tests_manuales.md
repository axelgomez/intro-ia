Matriz de costos
1  2  3  4  5
0  5 15 17  7 
   0  6 19 20
      0  7 21
         0  5


Para la primera iteración los resultados esperados son
Abre el nodo (2, 'ciudad2')
6 ciudad3:
	1 a 2 = 5
	2 a 3 = 6 => Gn tiene que ser 11
5 ciudad5:
	1 a 5 = 7 => Gn tiene que ser 7
3 ciudad3:
	1 a 3 = 15 => Gn tiene que ser 15
4 ciudad4:
	1 a 4 = 17 => Gn tiene que ser 17
7 ciudad4:
	1 a 2 = 5
	2 a 4 = 19 => Gn tiene que ser 24
8 ciudad5
	1 a 2 = 5
	2 a 5 = 20 => Gn tiene que ser 25 

Hn:
5 ciudad5: 30 - 7 => Hn tiene que ser 23
	(7 es uno de los 5 menores costos del vector)
6 ciudad3: 7 + 7 + 5 => Hn tiene que ser 19
	Estos valores salen de remover el 5 (1 a 2) y el 6 (2 a 3) del vector de costos, ordenarlo ascendemente y sacar los 3 primeros
3 ciudad3: Paso a paso
	5, 15, 17, 7, 6, 19, 20, 7, 21, 5
	5, 17, 7, 6, 19, 20, 7, 21, 5 <- se remueve el 15 (1 a 3)
	5, 5, 6, 7, 7, 19, 20, 21 <- se ordena
	5 + 5 + 6 + 7 = 23 <- se sacan los 4 primeros y se los suma
	Hn tiene que ser 23
4 ciudad4:
	idem 3 ciudad3 con mismo resultado
	Hn tiene que ser 23
7 ciudad4: paso a paso
	5, 15, 17, 7, 6, 19, 20, 7, 21, 5
	15, 17, 7, 6, 20, 7, 21, 5 <- se remueve el 5 (1 a 2) y el 19 (2 a 4)
	5, 6, 7, 7, 15, 17, 20, 21 <- se ordena
	5 + 6 + 7 <- se sacan los 3 primeros y se los suma 
 	Hn tiene que ser 18
8 ciudad5:
	idem 7 ciudad4 con mismo resultado
	Hn tiene que ser 18

Segunda iteración:
Abre el nodo (5, 'ciudad5')

Tercer iteración:
Abre el nodo (6, 'ciudad3')

Cuarta iteración:
Abre el nodo (11, 'ciudad4')

Quinta iteración:
Abre el nodo (12, 'ciudad4')

Sexta iteración:
Abre el nodo (15, 'ciudad3')

Séptima iteración:
Abre el nodo (16, 'ciudad5')

FINAL
1 a 2 = 
2 a 3 = 
3 a 4 = 
4 a 5 = 
5 a 1 = 