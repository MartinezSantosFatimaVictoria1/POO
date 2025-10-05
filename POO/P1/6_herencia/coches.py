import os
os.system ("cls")


class Coches:
    #Metodo constructor.-con este metodo se inicializa un objeto cuando es creado con valores iniciales
    
    def __init__(self,marca,color,modelo,velocidad,caballaje,plazas):
        self._marca=marca
        self._color=color
        self._modelo=modelo
        self._velocidad=velocidad
        self._caballaje=caballaje
        self._plazas=plazas
        
    
    
    def acelerar(self):
        pass
    
    def frenar(self):
        pass

    def _init_(self, color, marca, modelo, velocidad, caballaje, plazas):
        self.__color= color
        self.__marca= marca
        self.__modelo= modelo
        self.__velocidad= velocidad
        self.__caballaje= caballaje
        self.__plazas= plazas

    @property
    def color(self):
        return self.__color     
    

    @color.setter
    def color(self, color):             
        self.__color=color

    
    @property
    def marca(self, marca):
        return self.__marca

    @marca.setter
    def marca(self, marca):
     self.__marca=marca
  
    @property
    def modelo(self, modelo):
        return self.__modelo
    @modelo.setter
    def modelo(self,modelo):
        self.__modelo=modelo

    @property
    def velocidad(self, velocidad):
     return self.__velocidad
    @velocidad.setter
    def velocidad(self, velocidad):
     self.v__velocidad=velocidad

    @property
    def caballaje(self, caballaje):
        return self.__caballaje

    @caballaje.setter
    def caballaje(self, caballaje):
        self.__caballaje=caballaje

    @property
    def plazas(self, plazas):
        return self.__plazas
    @plazas.setter
    def plazas(self, plazas):
        self.__plazas=plazas


class Camiones(Coches):
  def __init__(self, marca, color, modelo, velocidad, caballaje, plazas,eje,capacidadCarga):
      super().__init__(marca, color, modelo, velocidad, caballaje, plazas)
      self.__eje=eje
      self.__capacidadCarga=capacidadCarga

      @property
      def eje(self):
          return self.__eje
      @eje.setter
      def eje(self,eje):
          self.__eje=eje

      @property
      def capacidad_carga(self):
            return self.__capacidad_carga

      @capacidad_carga.setter
      def capacidad_carga(self, capacidad_carga):
            self.__capacidad_carga=capacidad_carga


class Camionetas(Coches):
      def __init__(self, marca, color, modelo, velocidad, caballaje, plazas,traccion,cerrada):
        super().__init__(marca, color, modelo, velocidad, caballaje, plazas)
        self.__traccion=traccion
        self.__cerrada=cerrada

      @property
      def traccion(self):
          return self.__traccion
      @traccion.setter
      def traccion(self,traccion):
          self.__traccion=traccion

      @property
      def cerrada(self):
            return self.__cerrada

      @cerrada.setter
      def cerrada(self, cerrada):
            self.__cerrada=cerrada


