import sys
from FCM import FCM

def f1() : return 0.2

def f2(a=3) : return 0.4


fcm_graph=None

# Test 1 : Check for FCM creation
try :
    fcm_graph=FCM()
except :
    print 'Error detected in creating the FCM'
    sys.exit(2)

print '### FCM creation successful'

# Test 2 : Test for adding concepts
try :
    fcm_graph.add_concept("concept1")
    fcm_graph.add_concept("concept2")
except :
    print 'Error detected in adding concepts'
    sys.exit(2)

print '### FCM adding concepts successful'

# Test 3 : Adding valid edges

stat=fcm_graph.add_edge('concept1','concept2',0.3)
if stat :
    print '### FCM adding valid concepts successful'
else :
    print 'Error adding concepts : Test case failed'
    sys.exit(2)

fcm_graph.remove_edge('concept1','concept2')


# Test 3 : Adding edges which did not exist

stat=fcm_graph.add_edge('new concept1','new concept2',0.3)
if stat :
    print '### FCM adding new concepts successful'
else :
    print 'Error adding edges with new concepts : Test case failed'
    sys.exit(2)

# Test 4 : Adding invalid value for weights

stat=fcm_graph.add_edge('invalid concept1','invalid concept1',9.2)
if not stat :
    print '### FCM adding invalid weight concepts successful'
else :
    print 'Adding edges with invalid weights : Test case failed'
    sys.exit(2)

# Test 5 : Setting valid values for nodes

stat=fcm_graph.set_value('concept2',0.4)
if stat :
    print '### FCM Setting value successful '
else :
    print 'Error setting value : Test case failed'

# Test 6 : Setting values for nodes which did not exist :

stat=fcm_graph.set_value('some random name',0.3)
if not stat :
    print '### FCM Setting value for a node which did not exist successful'
else :
    print 'Setting value for a node which did not exist : Test case failed'

# Test 7 : Setting invalid values for nodes
stat=fcm_graph.set_value('concept2',2.1)
if not stat :
    print '### FCM Setting invalid value for a node successful'
else :
    print 'Setting invalid value for a node : Test case failed'

# Test 8 : Setting value for node using function with no parameters
stat=fcm_graph.set_value('concept2',f1)
if stat :
    print '### FCM Setting value using a function with no parameters succesful'
else :
    print 'Setting value using a function with no parameters : Test case failed'

# Test 9 : Setting value for node using function with parameters
stat=fcm_graph.set_value('concept2',f2)
if not stat :
    print '### FCM Setting value using invalid function successful'
else :
    print 'FCM Setting value using invalid function : Test case failed'


# Test 10 : Remove nodes which exist
stat=fcm_graph.remove_concept('concept1')
if stat :
    print '### FCM removing existing nodes successful'
else :
    print 'Error removing existing edges'
    sys.exit(2)

# Test 11 : Remove nodes which do not exist

stat=t=fcm_graph.remove_concept("some concept which does not exist")
if not stat :
    print '### FCM removing nodes which did not exist successful'
else :
    print 'Remove nodes which do not exist : Test case failed'


# Test 12 : Drawing the graph

try :
    fcm_graph.draw()
except :
    print 'Error in drawing the graph : Test case failed'

print '### FCM drawing the graph successful'





print 'All test cases passed .'
