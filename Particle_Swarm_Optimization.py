from FCM import *
from Simulation import *
from math import exp
from numpy import array
from random import randint
from math import sin, sqrt





class PSO :


    '''
    This class is a class which runs the Particle Swarm Optimization for FCMs to make
    sure that the concepts converge to the bounds given by the experts and the weights
    are globally minimized.

    '''



    def __init__(self,fcm,converge_concepts_dict,steepness_parameter=1,max_iterations=10,constriction_factor=0.7,cognitive_parameter=2,social_parameter=2) :
        '''

        @brief : The constructor here initializes the required attributes which are necessary to run the algorithm .

        @param : fcm - a valid FCM object
                     converge concepts dictionary : a dictionary where the keys are concepts and value is the
                     tuple describing its bounds. Example : {'Tank1' : (0.3,0.9),'Tank2' : '(0.2,0,7)'}

                     the default parameters are steepness_parameter,max_iterations,constriction_factor,cognitive_parameter,
                     social_parameter which are required for the algorithm


        '''


        self.fcm=fcm
        if converge_concepts_dict!=None :
         self.converge_concepts=converge_concepts_dict.keys()
        self.converge_concepts_dict=converge_concepts_dict
        self.steepness_parameter=steepness_parameter
        self.weight_matrix=dict()
        self.constriction_factor=constriction_factor
        self.cognitive_parameter=cognitive_parameter
        self.social_parameter=social_parameter
        self.max_iterations=10
        self.fitness_list=[]
        self.velocity_list=[]
        self.best_weights=[]

    def _sigmoid(self,x) :
        '''
        @brief The formula is  f(x)=(1)(1+exp(-x))
        @param x - a valid integer

        '''
        exponent_x=exp(x*self.steepness_parameter)
        return (exponent_x)/(1+exponent_x)


    def _heaviside(self,x) :
           '''
           @brief  This function is used to determine the objective function which acts as a global minimizer which returns either 0 or 1
           @param  x  a valid integer
           '''
           if x<0 :
             return 0
           return 1


    def _initialize_weight_matrix(self) :
        '''
        @brief : This function is used to create a dictionary of dictionary of the weights of the concept edges
        @param : This function takes no parameters other than the self parameter
        '''


        for node1 in self.fcm.concepts() :

            if node1 not in self.converge_concepts :
                continue

            for node2 in self.fcm.concepts() :
              self.weight_matrix.setdefault(node1,{})
              weight=self.fcm.get_weight(node1,node2)
              if weight!=None :
                  self.weight_matrix[node1][node2]=weight
              else :
                  self.weight_matrix[node1][node2]=0.0

        self.fitness_list=[0.0]*len(self.weight_matrix)
        self.velocity_list=[0.0]*len(self.weight_matrix)
        self.best_weights=[0.0]*len(self.weight_matrix)


    def _get_updated_concept_values(self,concept) :

        '''
        @brief This function updates the concept values according to the changed weights
        @param concept This function takes a valid concept as a parameter
        '''
        all_concepts=self.fcm.concepts()
        concept_vector=[]
        initial_concept_value=self.fcm.get_concept_value(concept)
        concept_vector.append(initial_concept_value)

        i=1

        while i<self.max_iterations :
            previous_concept_value=concept_vector[i-1]
            current_expression=previous_concept_value
            for node in all_concepts :
                if node in self.weight_matrix[concept] :
                    weight=self.weight_matrix[node][concept]
                    value=self.fcm.get_concept_value(node)
                    current_expression+=weight*value

            result=self._sigmoid(current_expression)
            concept_vector.append(result)
            i+=1

        return concept_vector


    def _get_fitness(self, weight):

      '''
      @brief : It is an implementation of the schaffer F6 function which is used to calculate the fitness of the weights
      @param weight - a valid weight number

      '''
      if len(weight) <= 2:
		return self._schafferF6HelperFunction(0, weight)
      else:
		total = 0
		for i in xrange(len(weight)):
			total += weight[i] * self._schafferF6HelperFunction(i, weight)
		return total


    def _schafferF6HelperFunction(self, index, weight):
        '''

        @brief  This function is a pairwise schaffer F6 calculator which is used by the above function
                    The formula is 0.5 + (sin(sqrt(x**2+y**2))-0.5) /(1+0.001*(x**2+y**2))**2
        @param index - a valid integer
                   weight - a valid weight


        '''

        x = weight[index]
        y = weight[(index+1)%len(weight)]
        xsqrdysqrd = x**2 + y**2
        return 0.5 + (sin(sqrt(xsqrdysqrd))-0.5) / (1+0.001*xsqrdysqrd)**2

    def _get_swarm_weights(self) :

        '''
        @brief   This function is used to get the swarm weights by finding the
                     global best and the local best and will update the weights
        @param  This function takes no parameters other than the self parameter

        '''


        gbest=self.weight_matrix[self.converge_concepts[0]].values()
        g_fitness=self._get_fitness(gbest)
        iterations=0


        while iterations<self.max_iterations :

            for i in range(0,len(self.converge_concepts)) :

                current=self.weight_matrix[self.converge_concepts[i]].values()
                fitness=self._get_fitness(current)

                if fitness>self.fitness_list[i] :
                    self.fitness_list[i]=fitness
                    self.best_weights=current

                if fitness>g_fitness :
                    g_fitness=fitness
                    gbest=current



                for j in range(0,len(current)) :
                   if current[j]!=0.0 :
                    self.velocity_list[i]+=(self.constriction_factor)*(self.cognitive_parameter*randint(0,1)*(self.best_weights[j]-current[j]))+(self.social_parameter*randint(0,1)*(gbest[j]-current[j]))
                    current[j]+=self.velocity_list[i]


                k=0

                for key in self.weight_matrix[self.converge_concepts[i]] :
                    if current[k]>1 :
                        div='1'+'0'*(len(str(int(current[k]))))
                        div=int(div)

                        current[k]/=div


                    self.weight_matrix[self.converge_concepts[i]][key]=current[k]
                    k+=1

            iterations+=1


    def _in_bounds(self,value,bounds) :

        '''
        @brief : This method is a utility function which is used to tell if the value lies between the bounds

        @param : value - a valid integer
                   bounds - a tuple in sorted ascending order

        '''


        if value>=bounds[0] and value<=bounds[1] :
            return True

        return False


    def _check_concept_bounds(self) :
        '''
        @brief: This method checks if the concepts are asked to be converged are within the given bounds or not.This function is the
                    termination function for the algorithm
        @param  : No parameters other than the self parameter
        '''


        for concept in self.converge_concepts_dict :
            bounds=self.converge_concepts_dict[concept]
            if not self._in_bounds(self.fcm.get_concept_value(concept),bounds) :
                return False

        return True

    def run_convergence(self) :

        '''
        @brief : This function runs the algorithm which changes the convergence
                         algorithm by the following steps :
                         1) Initialize the weight matrix
                         2) For the requested concepts ,check if they are in bounds,
                         3) If they are out of bounds,do the following
                         4) Run the swarm for weight matrix
                         5) Calculate the objective function
                         6) If the concept values converge,stop the algorithm
                         7) Else,continue the process

        @param  : This method takes no parameters other than the self parameter


        '''



        self._initialize_weight_matrix()

        objective_function=0

        while not self._check_concept_bounds() :

         objective_function=0
         self._get_swarm_weights()


         for concept in self.converge_concepts :
            bounds=self.converge_concepts_dict[concept]
            concept_value=self.fcm._get_concept_value(concept)
            if self._in_bounds(concept_value,bounds) :
                continue

            function_value=concept_value
            for c in self.fcm.concepts() :
                w=self.fcm.get_weight(c,concept)
                v=self.fcm.get_concept_value(c)

                if w==None or v==0.0:
                    continue
                function_value+=w*v

            concept_value=self._sigmoid(function_value)
            self.fcm.set_value(concept,concept_value)

            objective_function+=self._heaviside(bounds[0]-concept_value)*abs(bounds[0]-concept_value)+(self._heaviside(concept_value-bounds[1])*abs(concept_value-bounds[1]))



        print '--------END OF CONVERGENCE--------------------------'
        print 'Global minimizer : '+str(objective_function)
        print 'Final weights'
        print self.weight_matrix
        print 'concept values '
        for c in self.converge_concepts :
          print self.fcm.get_concept_value(c)
