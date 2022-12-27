import csv
import pandas as pd

# Creacion de diccionarios con totales
estadisticas = ['G', 'P', 'TS', 'SI', 'SO', 'BS', 'FK', 'C', 'OFF', 'TI',
                'GS', 'F', 'RC', 'YC', 'TP', 'PC', 'T', 'A', 'DA']
dictHome = {}
dictAway = {}


def average_stats_calculator(db_location):
    data = pd.read_csv(db_location.split(".")[0] + ".csv", sep=',', encoding='utf-8', na_values='-')

    for i in range(len(data)):
        partido = data.loc[i]

        # Local
        name_home_team = data["HomeTeam"][i]
        if name_home_team not in dictHome:
            dictHome[name_home_team] = []

        stats = []
        for j in range(len(estadisticas)):
            stats.append(partido["H" + estadisticas[j]])
        dictHome[name_home_team].append(stats)

        # Visitante
        name_away_team = data["AwayTeam"][i]
        if name_away_team not in dictAway:
            dictAway[name_away_team] = []

        stats = []
        for j in range(len(estadisticas)):
            stats.append(partido["A" + estadisticas[j]])
        dictAway[name_away_team].append(stats)

    # Calculo de promedios por equipo
    # Local
    print("Home:")
    home_averages = {}
    for i in dictHome.keys():
        totals = [0 for _ in range(19)]
        nan_count = [0 for _ in range(19)]
        for j in dictHome[i]:
            for k in range(len(j)):
                if not pd.isna(j[k]):
                    totals[k] += j[k] if k != 1 else int(j[k][:-1])
                elif k != 12 and k != 13:
                    nan_count[k] += 1

        result = []
        print(i, totals)
        for j in range(len(totals)):
            result.append(totals[j] / (len(dictHome[i]) - nan_count[j]))

        home_averages[i] = result

    print(home_averages)
    print()

    # Visitante
    print("Away:")
    away_averages = {}
    for i in dictAway.keys():
        totals = [0 for _ in range(19)]
        nan_count = [0 for _ in range(19)]
        for j in dictAway[i]:
            for k in range(len(j)):
                if not pd.isna(j[k]):
                    totals[k] += j[k] if k != 1 else int(j[k][:-1])
                elif k != 12 and k != 13:
                    nan_count[k] += 1

        result = []
        print(i, totals)
        for j in range(len(totals)):
            result.append(totals[j] / (len(dictAway[i]) - nan_count[j]))

        away_averages[i] = result

    print(away_averages)
    print()

    with open(db_location.split("resultados_anteriores")[0] + "home_averages.csv", 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        for i in home_averages.keys():
            output = home_averages[i]
            output.insert(0, i)
            writer.writerow(output)

    with open(db_location.split("resultados_anteriores")[0] + "away_averages.csv", 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        for i in away_averages.keys():
            output = away_averages[i]
            output.insert(0, i)
            writer.writerow(output)
