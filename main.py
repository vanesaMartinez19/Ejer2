from Manejadorlibro import ManejadorLibros
from ClaseLibro import viajeroFrecuente

print('hola')


def Test():
    print('--------TEST---------')
    listaViajantes = []

    unViajante = viajeroFrecuente(159, '29588284', 'Vanesa', 'Martinez', 25000)
    listaViajantes.append(unViajante)
    segViajante = viajeroFrecuente(160, '29588285', 'Vane', 'Martin', 30000)
    listaViajantes.append(segViajante)
    terViajante = viajeroFrecuente(161, '29588286', 'Van', 'Mart', 80000)
    listaViajantes.append(terViajante)

    for i in range(len(listaViajantes)):
        listaViajantes[i].mostrarDatos()

    for i in range(len(listaViajantes)):
        print('Cantidad de millas para el viajero numero', listaViajantes[i].getnumViajero(), '\n',
              listaViajantes[i].cantidadTotalMillas())

    for i in range(len(listaViajantes)):
        masMillas = 1000
        print('Cantidad de millas acumuladas para el  viajero', listaViajantes[i].getnumViajero(),'\n', listaViajantes[i].acumularMillas(masMillas), listaViajantes[i].cantidadTotalMillas())
        print('\n')

    mc = int(input('ingrese millas a canjear:'))
    for i in range(len(listaViajantes)):
        print('Para el  viajero', listaViajantes[i].getnumViajero())
        listaViajantes[i].canjearMillas(mc)
        print('\n')


if __name__ == '__main__':

    op = int(input('Desea ejecutar el Test??\n 1_SI \n 2_NO\n'))
    if op == 1:
        Test()

    ml = ManejadorLibros()
    ml.testLibros()
    v = viajeroFrecuente

    print('Listado de Viajeros Frecuentes')
    print(ml)
    #  El usuario ingresa por teclado un número de viajero frecuente, el sistema presente un menú con las siguientes opciones:
    nroVF = int(input('Ingrese Numero de Viajero a buscar:'))
    indice = ml.buscarViajero(nroVF)
    if indice == None:
       print('El numero de viajero {} no se encuentra en el sistema'.format(nroVF))
    else:
        libro = ml.getViajero(nroVF)
        print('Datos del viajero encontrado')
        #print(libro)
        print('Numero de viajero:{},DNI:{},Nombre:{},Apellido:{},Cantidad de millas acumuladas:{}'.format(nroVF, libro.getDNI(), libro.getNom(),libro.getApellido(), libro.getMillAcum()))
        # Mostrar el menú de opciones al usuario
    while True:
        print("Seleccione una opción:")
        print("a- Consultar Cantidad de Millas")
        print("b- Acumular Millas")
        print("c- Canjear Millas")
        print("d- Salir")
        opcion = input()

        if opcion == "a":
            print("Cantidad de Millas acumuladas:", viajeroFrecuente.cantidadTotaldeMillas())
        elif opcion == "b":
            millas_recorridas = int(input("Ingrese la cantidad de millas recorridas: "))
            viajeroFrecuente.acumularMillas(millas_recorridas)
            print("Millas acumuladas:", viajeroFrecuente.cantidadTotaldeMillas())
        elif opcion == "c":
            millas_a_canjear = int(input("Ingrese la cantidad de millas a canjear: "))
            viajeroFrecuente.canjearMillas(millas_a_canjear)

            #idlibro = nroVF
    #if idlibro == None:
        #otro = v.cantidadTotalMillas
        #print('cant{}'.format(otro))


        #print(':{}'.format(ml.getMetCant(nroVF)))

        #ml.paramenu(nroVF)

    print(indice)
    #if indice!= None:
        #libroprint('Cantidad de millas del viajero:{}'.format(libro.))
        #print('XXX{}'.format(viajeroFrecuente.getnumViajero()))
        #viajeroFrecuente.cantidadTotalMillas()
        #algo = vf.cantidadTotalMillas()








