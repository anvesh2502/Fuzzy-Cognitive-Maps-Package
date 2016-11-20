import networkx as nx
import matplotlib.pyplot as plt
from types import FunctionType
import inspect
import sys



class FCMConstructionError(Exception) :

    '''
    This class is an exception for FCM construction error
    '''

    def __init__(self,message,errors) :

      message=message+" : "+str(errors)
      super(Exception, self).__init__(message)



class InvalidWeightError(FCMConstructionError) :

    '''
    This class is an exception class for Invalid weights for FCM edges
    '''

    def __init__(self,errors,message="Invalid weight for an edge ") :

        super(InvalidWeightError,self).__init__(message,errors)

class ConceptExistError(FCMConstructionError) :

    '''
    This class is an exception class for Invalid concepts for the FCM
    '''

    def __init__(self,errors,message="Concept does not exist ") :

        super(ConceptExistError,self).__init__(message,errors)

class EdgeExistError(FCMConstructionError) :

    '''
    This class is an exception class for edge existence in FCM
    '''

    def __init__(self,errors,message="Edge does not exist between ") :

        e=str(errors[0])+" - "+str(errors[1])
        super(EdgeExistError,self).__init__(message,e)



class InvalidConceptValueError(FCMConstructionError) :

    '''
    This class is an exception class for invalid concept value of FCM
    '''

    def __init__(self,errors,message="Invalid Concept value ") :

        super(InvalidConceptValueError,self).__init__(message,errors)












class FCM :

    '''
    @package docstring
    This is a Python class  for Fuzzy Cognitive Maps

    '''


    def __init__(self) :
            '''
            @brief  This is the constructor for the Fuzzy graph.It initializes the networkx Digraph
            @params none
            '''


            self._fcm_graph=nx.DiGraph()


    def add_concept(self,concept) :
            '''
            @brief This method is an interface for the add_node method of DiGraph
            @param concept A valid concept

            '''


            self._fcm_graph.add_node(concept)
            self._fcm_graph.node[concept]['value']=0.0
            return


    def add_edge(self,concept1,concept2,weight) :
        '''

        @brief This method is an interface for the add_edge method of Digraph.It checks whether the weight provided is the range of [-1,1].If the node does not exist,we create them before creating the edge.
        @param concept1 a valid concept
        @param concept2 a valid concept
        @param weight a desired weight for the edge
        '''


        if weight<-1.0 or weight >1.0 :           # Error checking for the weight

             raise InvalidWeightError(weight)



        if concept1 not in self._fcm_graph.nodes() :   # If the node doesnt exist,create the node
            self.add_concept(concept1)

        if concept2 not in self._fcm_graph.nodes() :   # If the node doesnt exist,create the node
            self.add_concept(concept2)

        self._fcm_graph.add_edge(concept1,concept2,weight=weight) # Adding the edge


    def get_weight(self,concept1,concept2) :

        '''
        @brief returns the weight of the edge,if the edge exists
        @param concept1 a valid concept
        @param concept2 a valid concept
        '''

        edge_data=self._fcm_graph.get_edge_data(concept1,concept2)
        if edge_data==None :
            return None

        if 'weight' in edge_data :
            return edge_data['weight']

        return None


    def remove_edge(self,node1,node2) :
        '''
        @brief This method removes edges from the fcm graph.It also checks if the nodes exist and if the edge exists.
        @param node1 a valid concept
        @param node2 a valid concept
        '''


        if node1 not in self._fcm_graph.nodes()  :
            raise ConceptExistError(node1);

        if  node2 not in self._fcm_graph.nodes() :
            raise ConceptExistError(node2)


        if not self._fcm_graph.has_edge(node1,node2) :
            nodes=[node1,node2]
            raise EdgeExistError(nodes)

        self._fcm_graph.remove_edge(node1,node2)


    def remove_concept(self,concept) :
        '''
        @brief This method is an interface for the remove_node() .If the node does exist,it prints an error message and returns.
        @param concept A valid concept
        '''


        if concept not in self._fcm_graph.nodes() :

            raise ConceptExistError(concept)



        self._fcm_graph.remove_node(concept)
        return True



    def concepts(self) :
     '''
     @brief This method is an interface for nodes().It returns the dictionary of concepts in the graph having the node of the value as value and the concept as the key.
     @param none
     '''



     dictToReturn = {}
     for node in self._fcm_graph.nodes():
      dictToReturn[node] = self._fcm_graph.node[node]['value']
     return dictToReturn


    def set_value(self,concept,num) :
        '''
        @brief This method adds an attribute to a node and accepts either an integer of a function which returns an integer
        @param concept A valid concept
        @param num a valid integer between [-1,1 ]
        '''


        if concept not in self._fcm_graph.nodes() :   # Error if the given concept does not exist
            raise ConceptExistError(concept)



        if type(num) is int or type(num) is float  :             # If the parameter passed is an int,add it to the attribute

          if num>=-1.0 and num<=1.0 :
            self._fcm_graph.node[concept]['value']=num
          else :
            raise InvalidConceptValueError(num)

        elif type(num) is FunctionType or type(num) is self.FunctionType :

            param_length=(inspect.getargspec(num)[0])


            if len(param_length)!=0 :
                raise InvalidConceptValueError(num)

            self._fcm_graph.node[concept]['value']=num()

        else :
            raise InvalidConceptValueError(num)


    def get_concept_value(self,concept) :
        '''
        @brief returns the value of the concept
        @param concept a valid concept
        '''


        return self._fcm_graph.node[concept]['value']





    def draw(self) :
       '''
        @brief    This method is an interface for the draw() in the networkx package.We draw the DiGraph using spring layout and labels with the help of matplotlib
        @param none
       '''


       nx.draw(self._fcm_graph,pos=nx.spring_layout(self._fcm_graph),with_labels=True)
       plt.show()
