
class Calculadora:
    def __init__(self):
        self._numero1=int(input("numero #1: "))
        self._numero2=int(input("numero #2: "))


    def sumar(self):
        return self._numero1+self._numero2
    

    def restar(self):
        return self._numero1-self._numero2
    

    def multiplicar(self):
        return self._numero1*self._numero2
    

    def dividir(self):
        return self._numero1/self._numero2
    


operacion=Calculadora