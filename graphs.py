




class Graph:
    def __init__(self):
        self.vertices = {} #adjacency list

    def add_vertex(self, vertex):
        if vertex not in self.vertices: #need a dictionary to plot connection: weight
            self.vertices[vertex] = {} #dont want to overwrite a vertex that already exists, this will create a deadspot in my graph
        else:
            print("You already have this vertex")

    def add_edge(self, v1, v2, weight):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1][v2] = weight
            self.vertices[v2][v1] = weight #backwards connection for undirected graph
            
    def dijkstras(self, start):
        distances = {vertex: float('inf') for vertex in self.vertices} #Tracks the shortest distance from start to each node
        predecessor = {vertex: None for vertex in self.vertices} #For each node, tracks the best first step to jump to, to get back to the start
                    #start A : {A: None, B: A, C:B. D:A}

        distances[start] = 0
        pq = [(0, start)] #primary

        while pq:

            current_distance, current_vertex = pq.pop()

            if current_distance> distances[current_vertex]: #distance is less efficiaent than a path we've already charted
                continue #no point in looking at this node

            for neighbor, weight in self.vertices[current_vertex].items(): #going through the neigboring nodes
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    predecessor[neighbor] = current_vertex
                    pq.append((distance, neighbor))

        return distances, predecessor
    
    def fastest_path(self, start, end):

        distances, predecessor = self.dijkstras(start)

        path = []
        current = end
        while predecessor[current] is not None:
            path.append(current)
            current = predecessor[current]

        path.append(start)
        path.reverse()

        return (distances[end], path )




graph = Graph()

graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')

graph.add_edge('A', 'B', 2)
graph.add_edge('B', 'C', 5)
graph.add_edge('C', 'D', 7)
graph.add_edge('D', 'A', 2)

print(graph.vertices)

print(graph.fastest_path("A", "C"))
