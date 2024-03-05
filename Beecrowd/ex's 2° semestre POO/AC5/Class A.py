
from abc import ABC, abstractmethod

class A(ABC):
    def metodo_m(self):
        ...

    @abstractmethod
    def metodo_n(self):
        ...

class B(A):
    def metodo_o():
        ...

x = B()
