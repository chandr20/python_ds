class DirectedGraphAL:
    def __init__(self,size):
        self.size = size
        self.vertices = [None]*size

    def addEdge(self,u,v,weight):
        if self.vertices[u] is None:
            self.vertices[u] = []
        for e in self.vertices[u]:
            if e[0] == v:
                self.vertices[u].remove(e)
                break
        self.vertices[u].append((v,weight))

    def Neighbors(self,u):
        if self.vertices[u]:
            for e in self.vertices[u]:
                yield e


    def __repr__(self):
        rep = 'Graph:['
        for u in range(self.size):
            if self.vertices[u]:
                rep += str(u)+":"
                rep += ','.join(map(str,self.vertices[u]))
        return rep + ']'