import networkx as nx

def girvan_newman(graph):
    # Create a copy of the original graph to work on
    G = graph.copy()
    communities = list(nx.connected_components(G))
   
    while len(communities) == 1:
        # Calculate edge betweenness centrality
        edge_betweenness = nx.edge_betweenness_centrality(G)
       
        # Find the edge(s) with the highest betweenness
        max_betweenness = max(edge_betweenness.values())
        for edge, betweenness in edge_betweenness.items():
            if betweenness == max_betweenness:
                G.remove_edge(*edge)
       
        # Recalculate connected components
        communities = list(nx.connected_components(G))
   
    return communities

# sample graph
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (4, 6), (5, 6)])


result = girvan_newman(G)
print("\nCommunities:", result)
print()