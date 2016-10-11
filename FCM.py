import networkx as nx
import matplotlib.pyplot as plt
from types import FunctionType


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

        if weight<-1.0 or weight >1.0 :           # Error checking for the weight

            print 'Invalid weight value in add_edge'
            return

        if concept1 not in self._fcm_graph.nodes() :   # If the node doesnt exist,create the node
            self.add_concept(concept1,value=0)

        if concept2 not in self._fcm_graph.nodes() :   # If the node doesnt exist,create the node
            self.add_concept(concept2)

        self._fcm_graph.add_edge(concept1,concept2,weight=weight) # Adding the edge

    '''
    This method is an interface for
    the remove_node() .If the node
    does exist,it prints an error
    message and returns.

    '''
    def remove_concept(self,concept) :

        if concept not in self._fcm_graph.nodes() :
            print 'Concept not found.Unable to delete'
            return

        self._fcm_graph.remove_node(concept)


    '''
    This method is an interface for
    nodes().It returns the list of
    concepts in the graph.
    '''

    def concepts(self) :

        return self._fcm_graph.nodes()

    '''
    This method adds an attribute to
    a node and accepts either an integer
    of a function which returns an integer
    '''

    def set_value(self,concept,num) :

        if concept not in self._fcm_graph.nodes() :   # Error if the given concept does not exist
            print 'Given concept not found '
            return

        if type(num) is int or type(num) is float  :             # If the parameter passed is an int,add it to the attribute
            self._fcm_graph.node[concept]['value']=num

        elif type(num) is FunctionType or type(num) is self.FunctionType :
            self._fcm_graph.node[concept]['value']=num()

        else :
            print 'Invalid parameter to set_value'
            return









    '''
    This method is an interface for the draw()
    in the networkx package.We draw the DiGraph
    using spring layout and labels with the help
    of matplotlib

    '''
    def draw(self) :

       nx.draw(self._fcm_graph,pos=nx.spring_layout(self._fcm_graph),with_labels=True)
       plt.show()
