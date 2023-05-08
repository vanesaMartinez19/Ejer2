import csv
from ClaseViajeroFrecuente import viajeroFrecuente

class ManejadorLibros:
    __listaViajeros =  []

    def __init__(self):
        self.listaViajeros = []
    def __str__(self):
        s = ""
        for viaje in self.listaViajeros:
            s += str(viaje) + '\n'
        return s
    def agregarLibro(self,unViajero):
        self.listaViajeros.append(unViajero)

    def buscarViajero(self, clave):
        indice = 0
        valorDeRetorno = None
        bandera = False
        while not bandera and indice < len(self.listaViajeros):
            if self.listaViajeros[indice].getnumViajero() == clave:
                bandera = True
                valorDeRetorno = indice
                #print(self.v.cantidadTotalMillas())                #listaViajeros[valorDeRetorno].getnumViajero()
            else:
                indice+=1
        return valorDeRetorno

    def getMetCant(self,indice):
        v = viajeroFrecuente
        ind = self.getViajero(indice)
        if ind != None:
            print(ind)
            return ind


       def getViajero(self, indice):
        ind = self.buscarViajero(indice)
        return self.listaViajeros[ind]

    def testLibros(self):
        archivo = open('archiviajeros.csv')
        reader = csv.reader(archivo,delimiter=',')
        bandera = True
        for fila in reader:
            if bandera:
                '''saltear cabecera '''
                bandera = not bandera
            else:
                numViajero = int(fila[0])
                dni = fila[1]
                Nombre = fila[2]
                Apellido = fila[3]
                millasacum = int(fila[4])
                unViajero = viajeroFrecuente(numViajero,dni,Nombre,Apellido,millasacum)
                self.agregarLibro(unViajero)
        archivo.close()
