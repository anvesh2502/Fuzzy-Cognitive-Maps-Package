import sys
from FCM import *

def f1() : return 0.2

def f2(a=3) : return 0.4


fcm_graph=None

# Test 1 : Check for FCM creation
fcm_graph=FCM()

print '### FCM creation successful'

# Test 2 : Test for adding concepts
fcm_graph.add_concept("concept1")
fcm_graph.add_concept("concept2")

print '### FCM adding valid concepts successful'


# Test 3 : Adding valid edges

fcm_graph.add_edge('concept1','concept2',0.3)

print '### FCM adding valid edges successful'

fcm_graph.remove_edge('concept1','concept2')
print '### FCM removing valid edges successful'


# Test 3 : Adding edges which did not exist

try :
  fcm_graph.add_edge('new concept1','new concept2',0.3)
except ConceptExistError :
  print '### FCM removing adding invalid edges successful '



# Test 4 : Adding invalid value for weights

try :
  fcm_graph.add_edge('invalid concept1','invalid concept1',9.2)
except InvalidWeightError :
  print '### FCM invalid weight error successful'

# Test 5 : Setting valid values for nodes

fcm_graph.set_value('concept2',0.4)
print '### FCM valid values for concept successful'

# Test 6 : Setting values for nodes which did not exist :
try :
 fcm_graph.set_value('some random name',0.3)
except ConceptExistError :
 print '### FCM set value for invalid  concept successful'

# Test 7 : Setting invalid values for nodes

try :
 fcm_graph.set_value('concept2',2.1)
except InvalidConceptValueError :
 print '### FCM setting invalid value for concept successful'



# Test 8 : Setting value for node using function with no parameters
stat=fcm_graph.set_value('concept2',f1)
print '### FCM setting value for node using valid function successful '


# Test 9 : Setting value for node using function with parameters
try :
 fcm_graph.set_value('concept2',f2)
except InvalidConceptValueError :
 print '### FCM setting invalid value using invalid function successful '

# Test 10 : Remove nodes which exist

stat=fcm_graph.remove_concept('concept1')
print '### FCM removing concepts '

# Test 11 : Remove nodes which do not exist
try :
 fcm_graph.remove_concept("some concept which does not exist")
except ConceptExistError :
 print '### FCM removing concepts which does not exist successful'

# Test 12 : Drawing the graph

fcm_graph.draw()

print '### FCM drawing the graph successful'





print 'All test cases passed .'
