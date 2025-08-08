# 7. Ranking de puntuaciones: Un juego guarda las puntuaciones de jugadores. 
# Ordena las puntuaciones en orden descendente usando inserción.

Puntuaciones = [412.7, 14.789, 999.453, 203.564, 32.548]
n = len(Puntuaciones)

for i in range(1, n):
    Ranking = Puntuaciones[i]
    j = i -1
    while j >= 0 and Puntuaciones[j] < Ranking:
        Puntuaciones[j + 1] = Puntuaciones[j]
        j -= 1
    Puntuaciones[j + 1] = Ranking

print(f"El Ranking de los jugadores es: {Puntuaciones}")