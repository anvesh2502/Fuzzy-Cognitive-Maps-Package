import networkx as nx
import matplotlib.pyplot as plt


'''
This is a Python package for Fuzzy Cognitive Maps

'''


class FCM :

    '''
    This is the constructor for the Fuzzy graph.
    It initializes the networkx Digraph
    '''
    def __init__(self) :

        self._fcm_graph=nx.DiGraph()


    '''
    This method is an interface for the add_node
    method of DiGraph

    '''
    def add_concept(self,concept) :

        return self._fcm_graph.add_node(concept)

    '''
    This method is an interface for the add_edge
    method of Digraph.It checks whether the
    weight provided is the range of [-1,1].

    If the node does not exist,we create them
    before creating the edge.

    '''

    def add_edge(self,concept1,concept2,weight) :

        if weight<=-1.0 or weight >1.0 :           # Error checking for the weight

            print 'Invalid weight value in add_edge'
            return

        if concept1 not in self._fcm_graph.nodes() :   # If the node doesnt exist,create the node
            self.add_concept(concept1)

        if concept2 not in self._fcm_graph.nodes() :   # If the node doesnt exist,create the node
            self.add_concept(concept2)

        self._fcm_graph.add_edge(concept1,concept2,weight=weight) # Adding the edge


    '''
    This method is an interface for the draw()
    in the networkx package.We draw the DiGraph
    using spring layout and labels with the help
    of matplotlib

    '''
    def draw(self) :

       nx.draw(self._fcm_graph,pos=nx.spring_layout(self._fcm_graph),with_labels=True)
       plt.show()
