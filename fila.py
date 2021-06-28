from node import Node; 

class Fila:
    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0
    
    def push(self, elem):
        node = Node(elem)
        if self.last is None:
            self.last = node
        else: 
            self.last.next = node 
            self.last = node 
        
        if self.first is None:
            self.first = node 
        
        self._size = self._size + 1
        
    def pop(self): 
        if self._size > 0:
            elem = self.first.data
            self.first = self.first.next 
            self._size = self._size - 1
            return elem 
        raise print("A fila está vazia")
        
    def peek(self):
        if self._size > 0:
            elem = self.first.data
            return print (elem)
        raise print("A fila está vazia")
        
    
    def __len__(self):
        return self._size
    
    
    def imprimir(self):
        if self._size > 0:
            vaga = ""
            pointer = self.first
            while(pointer):
                vaga = vaga + str(pointer.data) + " "
                pointer = pointer.next
            return print(vaga)
        return print("A fila está vazia") 
            
    
    def __str__(self):
        return self.__repr__()
        
        
        
        