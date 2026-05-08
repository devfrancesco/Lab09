import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._nodes = None
        self._edges = None
        self._idMapAO = {}

    def buildGraph(self, distanza):
        self._graph.clear()
        self._nodes = DAO.getAllAirports()
        self.fillIdMap()
        self._graph.add_nodes_from(self._nodes)
        self._edges = DAO.getAllRotte(distanza)
        for rotta in self._edges:
            u = self._idMapAO[rotta.ORIGIN_AIRPORT_ID]
            v = self._idMapAO[rotta.DESTINATION_AIRPORT_ID]
            peso = rotta.media
            if self._graph.has_edge(u, v):
                nuova_media = (self._graph[u][v]['weight'] + peso) / 2
                self._graph[u][v]['weight'] = nuova_media
            else:
                self._graph.add_edge(u, v, weight=peso)

    def getNumNodes(self):
        return self._graph.number_of_nodes()

    def getNumEdges(self):
        return self._graph.number_of_edges()

    def fillIdMap(self):
        for n in self._nodes:
            self._idMapAO[n.ID] = n

    def getDettagli(self):
        result = []
        for u, v, data in self._graph.edges(data=True):
            peso = data.get('weight', 0)
            result.append(f"{u.ID} -> {v.ID} - Distanza media: {peso:.2f}")
        return result

