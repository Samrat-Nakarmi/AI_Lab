import networkx as nx
import matplotlib.pyplot as plt

class SemanticNet:
    def __init__(self):
        self.graph = nx.Graph()

    def add_relationship(self, concept1, concept2, relationship):
        """Adds a relationship between two concepts."""
        self.graph.add_edge(concept1, concept2, relation=relationship)

    def display(self):
        """Displays the semantic network graph."""
        pos = nx.spring_layout(self.graph)
        labels = nx.get_edge_attributes(self.graph, 'relation')
        nx.draw(self.graph, pos, with_labels=True, node_size=3000, node_color='lightblue')
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=labels)
        plt.show()

# Example Usage
semantic_net = SemanticNet()

# Add relationships between animals
semantic_net.add_relationship("Dog", "Mammal", "is_a")
semantic_net.add_relationship("Cat", "Mammal", "is_a")
semantic_net.add_relationship("Mammal", "Animal", "is_a")
semantic_net.add_relationship("Bird", "Animal", "is_a")
semantic_net.add_relationship("Dog", "Pet", "is_a")
semantic_net.add_relationship("Cat", "Pet", "is_a")
semantic_net.add_relationship("Bird", "Pet", "is_a")

# Display the semantic network
semantic_net.display()
