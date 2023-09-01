# Imports
import os
from league_matches_scraper import league_matches_scraper
from league_results_scraper import league_results_scraper
from average_stats_calculator import average_stats_calculator
from upcoming_matches_scraper import upcoming_matches_scraper


def main(pais, liga, cant_omitir):
    # Lectura de parámetros
    link_liga = "https://www.flashscore.co/futbol/{}/{}".format(pais, liga)

    # Lectura de versión
    version = 0

    # Especificación de la ruta con los datos
    if not os.path.exists(f'data/{pais}_{liga}'):
        os.mkdir(os.path.abspath(os.getcwd()).replace("\\", "/") + "/" + f'data/{pais}_{liga}')

    path = f'data/{pais}_{liga}/version{version}'
    if not os.path.exists(path):
        os.mkdir(os.path.abspath(os.getcwd()).replace("\\", "/") + "/" + path)

    # Ejecución del programa
    print("-------------------- Parte 1 de 3 --------------------")
    print("Recolectando estadísticas anteriores")
    print()
    #league_matches_scraper(link_liga + "-2022-2023/resultados/", path + "/resultados_anteriores.xlsx", cant_omitir)
    #league_matches_scraper(link_liga + "/resultados/", path + "/resultados_anteriores.xlsx", cant_omitir)
    league_results_scraper(link_liga + "-2022-2023/resultados/", path + f"/{pais}_{liga}.xlsx", cant_omitir)
    league_results_scraper(link_liga + "/resultados/", path + f"/{pais}_{liga}_23-24.xlsx", cant_omitir)

    print("-------------------- Parte 2 de 3 --------------------")
    print("Calculando estadísticas promedio")
    print()
    #average_stats_calculator(path + "/resultados_anteriores.xlsx")

    print("-------------------- Parte 3 de 3 --------------------")
    print("Obteniendo lista de próximos partidos")
    print()
    #upcoming_matches_scraper(link_liga + "/partidos/", path + "/proximos_partidos_prueba.xlsx")


#--main("belgica", "jupiler-pro-league", 0) 
#----main("espana", "laliga-ea-sports", 0)
#main("francia", "ligue-1", 0)
#----main("inglaterra", "premier-league", 0)
#----main("italia", "serie-a", 0)
#main("paises-bajos", "eredivisie", 0)
#--main("portugal", "liga-portugal", 0)
#--main("turquia", "super-lig", 0)

#main("belgica", "challenger-pro-league", 0)
#main("espana", "laliga-hypermotion", 0)
#----main("francia", "ligue-2", 0)
#----main("inglaterra", "championship", 0)
#----main("italia", "serie-b", 0)
#--main("paises-bajos", "keuken-kampioen-divisie", 0)
#----main("portugal", "liga-portugal-2", 0)
#----main("turquia", "1-lig", 0)


#main("colombia", "primera-a", 226)  # 0 / 226
#main("brasil", "brasileirao-serie-a", 0)

#main("colombia", "primera-b", 154)  # 0 / 154


#main("alemania", "bundesliga", 0)
#main("austria", "bundesliga", 0)
#main("croacia", "hnl", 0)
#main("dinamarca", "superliga", 0)
#main("escocia", "premiership", 0)
#main("grecia", "superliga", 0)
main("polonia", "ekstraklasa", 0)
main("republica-checa", "fortuna-liga", 0)
main("rumania", "liga-1", 0)
main("rusia", "premier-league", 0)
main("suiza", "super-league", 0)
main("ucrania", "premier-league", 0)


main("alemania", "2-bundesliga", 0)
main("austria", "2-liga", 0)
main("croacia", "prva-nl", 0)
main("dinamarca", "1-division", 0)
main("escocia", "championship", 0)
main("grecia", "super-league-2", 0)
main("polonia", "division-1", 0)
main("republica-checa", "fnl", 0)
main("rumania", "liga-2", 0)
main("rusia", "fnl", 0)
main("suiza", "challenge-league", 0)
main("ucrania", "persha-liga", 0)