import heapq

class Grafo:
    def __init__(self):
        self.ciudades = set()
        self.conexiones = {}

    def agregar_ciudad(self, ciudad):
        self.ciudades.add(ciudad)
        self.conexiones[ciudad] = {}

    def agregar_carretera(self, origen, destino, distancia):
        self.conexiones[origen][destino] = distancia
        self.conexiones[destino][origen] = distancia

    def encontrar_ruta_mas_corta(self, origen, destino):
        distancias = {ciudad: float('inf') for ciudad in self.ciudades}
        anteriores = {ciudad: None for ciudad in self.ciudades}
        distancias[origen] = 0
        cola = [(0, origen)]

        while cola:
            distancia_actual, ciudad_actual = heapq.heappop(cola)

            if ciudad_actual == destino:
                break

            for vecino, peso in self.conexiones[ciudad_actual].items():
                nueva_distancia = distancia_actual + peso
                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
                    anteriores[vecino] = ciudad_actual
                    heapq.heappush(cola, (nueva_distancia, vecino))

        # Reconstruir camino
        camino = []
        ciudad = destino
        while ciudad:
            camino.insert(0, ciudad)
            ciudad = anteriores[ciudad]

        if distancias[destino] == float('inf'):
            return [], float('inf')
        return camino, distancias[destino]


def main():
    mapa = Grafo()

    # Ciudades predefinidas
    mapa.agregar_ciudad("Bucaramanga")
    mapa.agregar_ciudad("Floridablanca")
    mapa.agregar_ciudad("Girón")
    mapa.agregar_ciudad("Piedecuesta")
    mapa.agregar_ciudad("Lebrija")

    # Carreteras predefinidas (distancias aproximadas en km)
    mapa.agregar_carretera("Bucaramanga", "Floridablanca", 7)
    mapa.agregar_carretera("Floridablanca", "Piedecuesta", 9)
    mapa.agregar_carretera("Bucaramanga", "Girón", 10)
    mapa.agregar_carretera("Girón", "Lebrija", 20)
    mapa.agregar_carretera("Floridablanca", "Girón", 6)

    print("=== SISTEMA DE NAVEGACIÓN ===")
    print("Ciudades disponibles:")
    for ciudad in sorted(mapa.ciudades):
        print(f" - {ciudad}")

    origen = input("\nIngrese la ciudad de origen: ").strip()
    destino = input("Ingrese la ciudad de destino: ").strip()

    if origen not in mapa.ciudades or destino not in mapa.ciudades:
        print("\nUna o ambas ciudades no están disponibles en el mapa.")
        return

    ruta, distancia = mapa.encontrar_ruta_mas_corta(origen, destino)

    if ruta:
        print("\nRuta más corta encontrada:")
        print(" → ".join(ruta))
        print(f" Distancia total: {distancia} km")
    else:
        print("No hay ruta disponible entre las ciudades seleccionadas.")


if __name__ == "__main__":
    main()