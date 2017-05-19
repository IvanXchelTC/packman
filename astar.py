from bge import logic

co=logic.getCurrentController()
o=co.owner

if logic.nodoinicial2!=0 and logic.nodofinal!=0 and o['hecho']==0:
    import collections
    
    meta=logic.nodofinal
    class Queue:
        def __init__(self):
            self.elements = collections.deque()
        
        def empty(self):
            return len(self.elements) == 0
        
        def put(self, x):
            self.elements.append(x)
        
        def get(self):
            return self.elements.popleft()

    # utility functions for dealing with square grids
    def from_id_width(id, *, width):
        return (id % width, id // width)

    def draw_tile(graph, id, style, width):
        r = "."
        if 'number' in style and id in style['number']: r = "%d" % style['number'][id]
        if 'point_to' in style and style['point_to'].get(id, None) is not None:
            (x1, y1) = id
            (x2, y2) = style['point_to'][id]
            if x2 == x1 + 1: r = "\u2192"
            if x2 == x1 - 1: r = "\u2190"
            if y2 == y1 + 1: r = "\u2193"
            if y2 == y1 - 1: r = "\u2191"
        if 'start' in style and id == style['start']: r = "A"
        if 'goal' in style and id == style['goal']: r = "Z"
        if 'path' in style and id in style['path']: r = "@"
        if id in graph.walls: r = "#" * width
        return r
    def checar(lista,numero):
        cont=0
        for b in lista:
            if b == numero:
                cont=1               
        if cont==0:
            lista.append(numero)
         
                
    def draw_grid(graph, width=2, **style):
        for y in range(graph.height):
            for x in range(graph.width):
                print("%%-%ds" % width % draw_tile(graph, (x, y), style, width), end="")
            print()

    # data from main article
    DIAGRAM1_WALLS = [from_id_width(id, width=30) for id in [21,22,51,52,81,82,93,94,111,112,123,124,133,134,141,142,153,154,163,164,171,172,173,174,175,183,184,193,194,201,202,203,204,205,213,214,223,224,243,244,253,254,273,274,283,284,303,304,313,314,333,334,343,344,373,374,403,404,433,434]]

    class SquareGrid:
        def __init__(self, width, height):
            self.width = width
            self.height = height
            self.walls = []
        
        def in_bounds(self, id):
            (x, y) = id
            return 0 <= x < self.width and 0 <= y < self.height
        
        def passable(self, id):
            return id not in self.walls
        
        def neighbors(self, id):
            (x, y) = id
            results = [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]
            if (x + y) % 2 == 0: results.reverse() # aesthetics
            results = filter(self.in_bounds, results)
            results = filter(self.passable, results)
            return results


       
       
            
     
    class GridWithWeights(SquareGrid):
        def __init__(self, width, height):
            super().__init__(width, height)
            self.weights = {}
        
        def cost(self, from_node, to_node):
            return self.weights.get(to_node, 1)

    diagram4 = GridWithWeights(17, 9)
    diagram4.walls = [(4, 0), (4, 1), (1, 1), (1, 2), (2, 1), (1, 3),(3,3),(3,5),(1,5),(1,6),(1,7),(4,8),(4,7),(2,7),(4,3),(4,5),(6,1),(6,3),(6,4),(6,5),
                      (7,5),(8,5),(9,5),(10,5),(6,7),(7,7),(8,7),(9,7),(10,7),(7,1),(8,1),(9,1),(10,1),
                      (10,3),(10,4),(10,5),(12,0),(12,1),(12,3),(12,5),(12,7),(12,8),(14,1),(15,1),(15,2),
                      (15,3),(15,5),(15,6),(15,7),(14,7),(7,3),(9,3),(13,3),(13,5)]
    diagram4.weights = {loc: 5 for loc in [(3, 4), (3, 5), (4, 1), (4, 2),
                                           (4, 3), (4, 4), (4, 5), (4, 6), 
                                           (4, 7), (4, 8), (5, 1), (5, 2),
                                           (5, 3), (5, 4), (5, 5), (5, 6), 
                                           (5, 7), (5, 8), (6, 2), (6, 3), 
                                           (6, 4), (6, 5), (6, 6), (6, 7), 
                                           (7, 3), (7, 4), (7, 5)]}

    import heapq

    class PriorityQueue:
        def __init__(self):
            self.elements = []
        
        def empty(self):
            return len(self.elements) == 0
        
        def put(self, item, priority):
            heapq.heappush(self.elements, (priority, item))
        
        def get(self):
            return heapq.heappop(self.elements)[1]


    def de_cordenada_a_num(path,intpath):
        cont1=0
        for a in path:
               
            if a == (0,0) or a==(1,0) or a== (0,1) or a== (0,2):
                checar(intpath,26)
            if a == (2, 0) or a==(3, 0) or a==(3, 1):
                checar(intpath,25)
            if a == (5,0) or a==(5,1) or a==(6,0):
                checar(intpath,6)
            if a == (7,0) or a==(8,0) or a==(9,0):
                checar(intpath,5)
            if a == (10,0) or a==(11,0) or a==(11,1):
                checar(intpath,4)
            if a == (13,0) or a==(14,0) or a==(13,1):
                checar(intpath,23)
            if a == (15,0) or a==(16,0) or a==(16,1) or a==(16,2):
                checar(intpath,24)
        #linea2
            if a == (14,2) or a==(14,3):
                checar(intpath,21)
            if a==(13,2):
                checar(intpath,22)
            if a == (12,2) or a==(11,2) or a==(10,2) or a==(11,3):
                checar(intpath,2)
            if a == (7,2) or a==(8,2) or a==(9,2):
                checar(intpath,1)
            if a == (4,2) or a==(5,2) or a==(6,2):
                checar(intpath,3)
            if a==(3,2):
                checar(intpath,30)
            if a==(2,2) or a==(2,3):
                checar(intpath,29)
        #linea3
            if a==(0,3) or a==(0,4) or a==(0,5):
                checar(intpath,27)
            if a==(1,4) or a==(2,4) or a==(3,4):
                checar(intpath,28)
            if a==(4,4) or a==(5,4):
                checar(intpath,7)
            if a==(11,4) or a==(12,4):
                checar(intpath,8)
            if a==(13,4) or a==(14,4) or a==(15,4):
                checar(intpath,20)
            if a==(16,3) or a==(16,4) or a==(16,5):
                checar(intpath,19)
        #linea4
            if a==(14,5) or a==(14,6):
                checar(intpath,16)
            if a==(13,6):
                checar(intpath,15)
            if a == (11,5) or a==(11,6) or a==(10,6) or a==(12,6):
                checar(intpath,9)
            if a==(7,6) or a==(8,6) or a==(9,6):
                checar(intpath,10)
            if a==(4,6) or a==(5,6) or a==(6,6):
                checar(intpath,11)
            if a==(3,6):
                checar(intpath,32)
            if a==(2,5) or a==(2,6):
                checar(intpath,31)
        #linea 5
            if a == (0,6) or a==(0,7) or a== (0,8) or a== (1,8):
                checar(intpath,34)
            if a == (2, 8) or a==(3, 8) or a==(3, 7):
                checar(intpath,33)
            if a == (5,8) or a==(5,7) or a==(6,8):
                checar(intpath,12)
            if a == (7,8) or a==(8,8) or a==(9,8):
                checar(intpath,13)
            if a == (10,8) or a==(11,8) or a==(11,7):
                checar(intpath,14)
            if a == (13,8) or a==(14,8) or a==(13,7):
                checar(intpath,17)
            if a == (15,8) or a==(16,8) or a==(16,7) or a==(16,6):
                checar(intpath,18)

    def de_num_a_cordenada(dato):
        if dato == 1:
            dato=(8,2)
        if dato == 2:
            dato=(11,2)
        if dato == 3:
            dato=(5,2)
        if dato == 4:
            dato=(11,0)
        if dato == 5:
            dato=(8,0)
        if dato == 6:
            dato=(5,0)
        if dato == 7:
            dato=(5,4)
        if dato == 8:
            dato=(11,4)
        if dato == 9:
            dato=(11,6)
        if dato == 10:
            dato=(8,6)
        if dato == 11:
            dato=(5,6)
        if dato == 12:
            dato=(5,8)
        if dato == 13:
            dato=(8,8)
        if dato == 14:
            dato=(11,8)
        if dato == 15:
            dato=(13,6)
        if dato == 16:
            dato=(14,6)
        if dato == 17:
            dato=(13,8)
        if dato == 18:
            dato=(16,8)
        if dato == 19:
            dato=(16,4)
        if dato == 20:
            dato=(14,4)
        if dato == 21:
            dato=(14,2)
        if dato == 22:
            dato=(13,2)
        if dato == 23:
            dato=(13,0)
        if dato == 24:
            dato=(16,0)
        if dato == 25:
            dato=(3,0)
        if dato == 26:
            dato=(0,0)
        if dato == 27:
            dato=(0,4)
        if dato == 28:
            dato=(2,4)
        if dato == 29:
            dato=(2,2)
        if dato == 30:
            dato=(3,2)
        if dato == 31:
            dato=(2,6)
        if dato == 32:
            dato=(3,6)
        if dato == 33:
            dato=(3,8)
        if dato == 34:
            dato=(0,8)
        return dato
        
    def reconstruct_path(came_from, start, goal):
        current = goal
        path = [current]
        while current != start:
            current = came_from[current]
            path.append(current)
        path.reverse()
        return path

    def heuristic(a, b):
        (x1, y1) = a
        (x2, y2) = b
        
        return abs(x1 - x2) + abs(y1 - y2)

    def a_star_search(graph, start, goal):
        frontier = PriorityQueue()
        frontier.put(start, 0)
        came_from = {}
        cost_so_far = {}
        came_from[start] = None
        cost_so_far[start] = 0
        
        while not frontier.empty():
            current = frontier.get()
           
            if current == goal:
                break
            
            for next in graph.neighbors(current):
                new_cost = cost_so_far[current] + graph.cost(current, next)
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    aa=heuristic(goal, next)
                    priority = new_cost + aa
                    frontier.put(next, priority)
                    came_from[next] = current
                   
        return came_from, cost_so_far
    print("nodo3=",logic.nodo3)
    if int(logic.nodo3)>0:
       inicia=int(logic.nodo3)
    else:
        inicia=logic.nodoinicial2
    
    
    inicio=de_num_a_cordenada(inicia)
    fin=de_num_a_cordenada(meta)

    print("inicioA*",inicio)
    print("finA*",fin)
        
        
    came_from, cost_so_far = a_star_search(diagram4, inicio, fin)
    draw_grid(diagram4, width=3, path=reconstruct_path(came_from, inicio, fin))
    path=reconstruct_path(came_from,inicio, fin)
    intpath=[]
    de_cordenada_a_num(path,intpath)

    print("A*",intpath)
    logic.camino2=intpath
 
