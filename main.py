# Imports
import os
from league_matches_scraper import league_matches_scraper
from average_stats_calculator import average_stats_calculator
from upcoming_matches_scraper import upcoming_matches_scraper

# Lectura de parámetros
pais = "espana"
liga = "laliga"
cant_omitir = 0
link_liga = "https://www.flashscore.co/futbol/{}/{}/".format(pais, liga)

# Lectura de versión
file = open("versiones/{}_{}.txt".format(pais, liga), "r")
version = int(file.read())
file.close()

file = open("versiones/{}_{}.txt".format(pais, liga), "w")
file.write("{}\n".format(version+1))
file.close()

# Creación de carpeta de datos
path = f'data/{pais}_{liga}/version{version}'
os.mkdir(os.path.abspath(os.getcwd()).replace("\\", "/") + "/" + path)

# Ejecución del programa
print("-------------------- Parte 1 de 3 --------------------")
print("Recolectando estadísticas anteriores")
print()
league_matches_scraper(link_liga + "resultados/", path + "/resultados_anteriores.xlsx", cant_omitir)

print("-------------------- Parte 2 de 3 --------------------")
print("Calculando estadísticas promedio")
print()
average_stats_calculator(path + "/resultados_anteriores.xlsx")

print("-------------------- Parte 3 de 3 --------------------")
print("Obteniendo lista de próximos partidos")
print()
upcoming_matches_scraper(link_liga + "partidos/", path + "/proximos_partidos.xlsx")
