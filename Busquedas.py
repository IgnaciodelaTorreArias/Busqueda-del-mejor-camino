from Repository import Repository
from dataclasses import dataclass
from sys import maxsize

class Busqueda:
    def __init__(self, repo:Repository):
        self.repo = repo

    def visitA(self, id:int, level:int):
        self.toVisit.remove(id)
        
        for nextId, peso in self.repo.whoConnects(id):
            if level+1 < self.minimumDistances[nextId]['weight']:
                self.minimumDistances[nextId]['weight'] = level+1
                self.minimumDistances[nextId]['previous'] = id
    
    def visitP(self, id:int, level:int):
        self.toVisit.remove(id)

        for nextId, peso in self.repo.whoConnects(id):
            if level+peso < self.minimumDistances[nextId]['weight']:
                self.minimumDistances[nextId]['weight'] = level+peso
                self.minimumDistances[nextId]['previous'] = id

    #type 0:Amplitud
    #type 1:Peso
    def Explore(self, algorithm:bool, origin:int):
        fun = self.visitA if not algorithm else self.visitP
        
        self.toVisit:set = set(id for id, peso in self.repo.getNodos())
        self.minimumDistances = {id:{'weight':maxsize, 'previous':None} for id, peso in self.repo.getNodos()}
        self.minimumDistances[origin]['weight'] = 0

        fun(origin, self.minimumDistances[origin]['weight'])
        while(len(self.toVisit)):
            minKey = None
            for key, value in self.minimumDistances.items():
                if minKey == None and key in self.toVisit:
                    minKey = key
                if key in self.toVisit and value['weight'] < self.minimumDistances[minKey]['weight']:
                    minKey = key
            fun(minKey, self.minimumDistances[minKey]['weight'])
        
    def bestPath(self, destiny:int)->dict:
        result = dict()
        result[destiny] = self.minimumDistances[destiny]['weight']
        while self.minimumDistances[list((result))[-1]]['previous'] is not None:
            previousId = self.minimumDistances[list((result))[-1]]['previous']
            result[previousId] = self.minimumDistances[previousId]['weight']
        result = list(result.items())
        result.reverse()
        result = dict(result)
        return result