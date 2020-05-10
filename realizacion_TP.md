#======================
# Para correr el jupyter lab:
#======================
$ jupyter lab


#======================

Los archivos TSP_completo de la cátedra están pensados para resolverlos por Aestrella debido a que el archivo de salida esperable contiene "nodos abiertos"

Por ello, voy a proceder, en primera instancia, a pasar dicho algoritmo a python y resolver este ejemplo básico (que figura en dicho documento):

Entrada TSP_IN_01.txt:
5;
5;15;17;7;6;19;20;7;21;5;

Salida esperada TSP_OUT_01_GIA.txt:
1;2;3;4;5;1;
30;
10;
03:22;

Es importante destacar que segun la documentación la entrada significa:
1) se tienen 5 ciudades
2) Los costos entre ciudades son (es una matriz simetrica, los costos de ida y vuelta son iguales):
        Ciudad1 Ciudad2 Ciudad3 Ciudad4 Ciudad5
Ciudad1     -      5      15      17       7
Ciudad2     -      -       6      19      20
Ciudad3     -      -       -       7      21
Ciudad4     -      -       -       -       5
Ciudad5     -      -       -       -       -

En base a esto estaría bueno poder graficar estas ciudades tomando como punto de partida el de la ciudad inicial (1)


TSPLIB95 is a library of sample instances for the TSP (and related problems) from various sources and of various types.

# En github:
## TSPLIB-python-parser: https://github.com/tsartsaris/TSPLIB-python-parser
This is a parser to read tsplib problems data into python list and dict so from a file like
```
NAME: ulysses16.tsp TYPE: TSP COMMENT: Odyssey of Ulysses (Groetschel/Padberg) DIMENSION: 16 EDGE_WEIGHT_TYPE: GEO DISPLAY_DATA_TYPE: COORD_DISPLAY NODE_COORD_SECTION 1 38.24 20.42 2 39.57 26.15 3 40.56 25.32 4 36.26 23.12 5 33.48 10.54 6 37.56 12.19 7 38.42 13.11 8 37.52 20.44 9 41.23 9.10 10 41.17 13.05 11 36.08 -5.21 12 38.47 15.13 13 38.15 15.35 14 37.51 15.17 15 35.49 14.32 16 39.36 19.56 EOF
```

you will end up having a dict like
```
[(1, ('38.24', '20.42')), (2, ('39.57', '26.15')), (3, ('40.56', '25.32')), (4, ('36.26', '23.12')), (5, ('33.48', '10.54')), (6, ('37.56', '12.19')), (7, ('38.42', '13.11')), (8, ('37.52', '20.44')), (9, ('41.23', '9.10')), (10, ('41.17', '13.05')), (11, ('36.08', '-5.21')), (12, ('38.47', '15.13')), (13, ('38.15', '15.35')), (14, ('37.51', '15.17')), (15, ('35.49', '14.32')), (16, ('39.36', '19.56'))]
```
As an addon you plot the cities with matplotlib and the current rout

## https://github.com/violet4/python-salesman
