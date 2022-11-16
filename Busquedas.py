from Repository import Repository
from dataclasses import dataclass
from sys import maxsize

class Busqueda:
    def __init__(self, repo:Repository):
        self.repo = repo
        self.amplitudPath = dict()
        self.weightPath = dict()

    def evaluate(self, origin:int):
        self.origin = origin
        self.amplitudPath =  self.__Explore(self.__visitA)
        self.weightPath = self.__Explore(self.__visitP)

    def __visitA(self, id:int):
        self.toVisit.remove(id) #Se marca como visitado
        level = self.path[id]['weight']

        for nextId, peso in self.repo.whoConnects(id):#Se evaluan los nodos a los que se conecta
            if level+1 < self.path[nextId]['weight']:#Se intercambia el mejor camino hacia los siguientes nodos, hasta encontrar el minimo
                self.path[nextId]['weight'] = level+1
                self.path[nextId]['previous'] = id
    
    def __visitP(self, id:int):
        self.toVisit.remove(id)
        level = self.path[id]['weight']

        for nextId, peso in self.repo.whoConnects(id):
            if level+peso < self.path[nextId]['weight']:
                self.path[nextId]['weight'] = level+peso
                self.path[nextId]['previous'] = id

    def __Explore(self, func):
        self.toVisit:set = set(id for id, peso in self.repo.getNodos()) #Control para evitar bucles
        self.path = {id:{'weight':maxsize, 'previous':None} for id, peso in self.repo.getNodos()} #Para guardar los resultados de cada visita
        
        self.path[self.origin]['weight'] = 0

        func(self.origin)
        while(len(self.toVisit)): #Investigacion de todos los nodos
            minKey = None
            for key in self.toVisit:
                if minKey == None:
                    minKey = key
                    continue
                if self.path[key]['weight'] < self.path[minKey]['weight']: minKey = key
            func(minKey)
        return self.path

    def __bestPath(self, destiny:int, path:dict)->dict:
        bestPathId = [destiny]
        while path[bestPathId[-1]]['previous'] is not None: #Se regresa desde el nodo destino hasta el origen
            bestPathId.append(path[bestPathId[-1]]['previous'])
        bestPathId.reverse()

        bestPath = dict()
        try:
            while(True):
                id = bestPathId.pop(0)
                bestPath[self.repo.getName(id)] = path[id]['weight']
        except:
            pass
        return bestPath

    #Mejor camnino en amplitud y mejor camino en peso
    def bestPath(self, destiny:int)->tuple:
        return (self.__bestPath(destiny, self.amplitudPath), self.__bestPath(destiny, self.weightPath))