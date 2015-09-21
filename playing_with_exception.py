__author__ = 'Enriquito'
from excepciones import excepciones,MyError


try:
    excepciones(-5)
    #raise MyError(2*2,'error')
except MyError as e:
     print 'My exception occurred, value1:', e.value1,' value2:', e.value2


