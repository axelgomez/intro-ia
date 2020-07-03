import cProfile
from a_estrella_listas import AEstrella

if __name__ == '__main__':
	# Codigo que solo se ejecutara si este archivo fuese llamado desde el interprete y no importado desde otro .py
	# Si hubiese sido importado, este codigo no se ejecutara
	algoritmo = AEstrella(sem_control=False)
	algoritmo.Procesar('TSP/AGD_TSP_IN_04.txt')

	# Para realizar un profile del algoritmo
	#cProfile.run('algoritmo = AEstrella(sem_control=False); algoritmo.Procesar("TSP/TSP_IN_06.txt")')