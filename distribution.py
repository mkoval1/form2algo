from pprint import PrettyPrinter

verteilung_absolute_hauefigkeit = {"4,7": 1, "4,8": 3, "4,9": 6, "5,0": 9, "5,1": 4, "5,2": 2}

summe_absolute_hauefigkeit = 0
for stichprobenwert, absolute_hauefigkeit in verteilung_absolute_hauefigkeit.items():
  summe_absolute_hauefigkeit += absolute_hauefigkeit

# Häufigkeitsfunkiton
verteilung_relative_hauefigkeit = {}
for stichprobenwert, absolute_hauefigkeit in verteilung_absolute_hauefigkeit.items():
  verteilung_relative_hauefigkeit[stichprobenwert] = absolute_hauefigkeit / summe_absolute_hauefigkeit

# Verteilungsfunktion
verteilung = {}
summe_hauefigkeiten = 0
for stichprobenwert, relative_häufigkeit in verteilung_relative_hauefigkeit.items():
  summe_hauefigkeiten += relative_häufigkeit
  verteilung[stichprobenwert] = summe_hauefigkeiten

pp = PrettyPrinter()
pp.pprint(verteilung_relative_hauefigkeit)
pp.pprint(verteilung)