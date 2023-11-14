def elevator(floors, actual, requests, dir):

    print("Arreglo de pisos: ", floors)
    print("Piso inicial: ", actual)
    print("Pisos ingresados: ", requests)
    print("Direccion: ", dir)

    while len(floors) > 0:
        
        #Movimiento del ascensor
        while(actual not in floors):
            print("Elevador en piso", actual)
            print("Elevator", dir)
            if dir == "Subiendo":
                actual += 1
            else:
                actual -= 1

        #el ascensor se detiene en uno de los pisos pendientes
        print("elevador se detiene en piso", actual)
        floors.remove(actual)
        
        #se mira si en el piso actual se solicita otro piso
        if actual in requests:
            print("Piso seleccionado", requests[actual])
            #se agrega la solicitud a los pisos pendientes si no esta ya en estos.
            if requests[actual] not in floors:
                floors.append(requests[actual])
            print(floors)

        #se revisa que direccion debe seguir el ascensor 
        if len(floors) > 0:
            if actual > floors[0]:
                dir = "Bajando"

def main():
    floors = [5, 29, 13, 10]
    start = 4
    requests = {5:2, 29: 10, 13: 1, 10:1}
    dir = "Subiendo"

    elevator(floors, start, requests, dir)

main()