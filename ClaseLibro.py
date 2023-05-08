class viajeroFrecuente:
    __numViajero = 0
    __dni = ''
    __Nombre = ''
    __Apellido=''
    __millasacum = 0

    def __init__(self, numViajero, dni, Nombre, Apellido, millasacum):
        self.__numViajero = numViajero
        self.__dni = dni
        self.__Nombre = Nombre
        self.__Apellido = Apellido
        self.__millasacum = millasacum

    def __str__(self):
        return "%s %s %s %s %s " % (self.__numViajero, self.__dni, self.__Nombre, self.__Apellido, self.__millasacum)

    def getnumViajero(self):
        return self.__numViajero

    def getDNI(self):
        return self.__dni

    def getNom(self):
        return self.__Nombre

    def getApellido(self):
        return self.__Apellido

    def getMillAcum(self):
        return self.__millasacum



    def cantidadTotalMillas(self):
        return self.__millasacum
    def acumularMillas(self,millasRecorr):
        #self.__millasacum += millas
        self.__millasacum = self.__millasacum + millasRecorr
        return self.__millasacum

    def canjearMillas(self,millasCanjear):
        if self.__millasacum>=millasCanjear:
            self.__millasacum = self.__millasacum - millasCanjear
            return print ("La cantidad de millas acumuladas es {}, es posible canjear las millas".format(self.__millasacum))
        else:return print("ERROR: La cantidad de millas a canjear es mayor a las millas acumuladas\n La cantidad de millas acumuladas es {}".format(self.__millasacum))
    def mostrarDatos(self):
        print('Numero de Viajero {}, Numero de DNI {}, Nombre {}, Apellido {}, Millas Acumuladas {}'.format(self.__numViajero, self.__dni, self.__Nombre, self.__Apellido, self.__millasacum))