__author__ = 'Enriquito'
# User define exceptions
class NumeroNegativoError(Exception): pass

class MayorAUnoError(Exception):
    def __init__(self, variableName):
        self.variableName = variableName
    def __str__(self):
         return repr(self.variableName)

class TemperaturaIncompatibleError(Exception):
     def __init__(self, variableName,value):
        self.variableName = variableName
        self.value = value


class AlphaIncompatibleError(Exception):
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2
