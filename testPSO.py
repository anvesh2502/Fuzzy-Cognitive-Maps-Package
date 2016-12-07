import sys
from FCM import *
from Simulation import *


test_fcm1= FCM()

test_fcm1.add_concept("Tank1")
test_fcm1.add_concept("Tank2")
test_fcm1.add_concept("Valve1")
test_fcm1.add_concept("Valve2")
test_fcm1.add_concept("Valve3")
test_fcm1.add_concept("Heat element")
test_fcm1.add_concept("Therm_tank1")
test_fcm1.set_value("Tank1",.2)
test_fcm1.add_concept("Therm_tank2")

test_fcm1.set_value("Tank2",.01)

test_fcm1.set_value("Valve1",.55)
test_fcm1.set_value("Valve2",.58)
test_fcm1.set_value("Valve3",.0)

test_fcm1.set_value("Heat element",.2)
test_fcm1.set_value("Therm_tank1",.1)
test_fcm1.set_value("Therm_tank2",.05)

test_fcm1.add_edge("Tank1","Valve1",.21)
test_fcm1.add_edge("Tank1","Valve2",.38)
test_fcm1.add_edge("Tank2","Valve2",.7)
test_fcm1.add_edge("Tank2","Valve3",.6)
test_fcm1.add_edge("Valve1","Tank1",.76)
test_fcm1.add_edge("Valve2","Tank1",-.6)
test_fcm1.add_edge("Valve2","Tank2",.8)
test_fcm1.add_edge("Valve2","Therm_tank2",.09)
test_fcm1.add_edge("Valve3","Tank2",-.42)
test_fcm1.add_edge("Heat element","Therm_tank1",.6)
test_fcm1.add_edge("Therm_tank1","Heat element",.53)
test_fcm1.add_edge("Therm_tank1","Valve1",.4)
test_fcm1.add_edge("Therm_tank2","Valve2",.3)


print 'Running Test case 1'
print
print
#pso=PSO(test_fcm1,{'Tank1':(0.6,0.9),'Tank2': (0.3,0.9)})
pso=PSO(test_fcm1,{'Tank1' : (0.6,0.9)})
pso.run_convergence()
print
print

test_fcm2=FCM()

print 'Running Test case 2'
print
print
test_fcm2.add_concept("Interest rate")
test_fcm2.add_concept("Productive Investments")
test_fcm2.add_concept("Occupation")
test_fcm2.add_concept("Inflation")

test_fcm2.add_edge("Interest rate","Productive Investments",-0.8)
test_fcm2.add_edge("Productive Investments","Occupation",1.0)
test_fcm2.add_edge("Occupation","Inflation",0.9)
test_fcm2.add_edge("Inflation","Interest rate",1.0)

test_fcm2.set_value("Interest rate",0.64)
test_fcm2.set_value("Productive Investments",0.3)
test_fcm2.set_value("Occupation",0.3)
test_fcm2.set_value("Inflation",0.45)

pso=PSO(test_fcm2,{"Occupation" : (0.4,0.73)})
pso.run_convergence()
print
print

test_fcm3=FCM()

test_fcm3.add_concept("Wetlands")
test_fcm3.add_concept("Fish")
test_fcm3.add_concept("Lake Pollution")
test_fcm3.add_concept("Income")
test_fcm3.add_concept("Law Enforcement")

test_fcm3.add_edge("Wetlands","Fish",1.0)
test_fcm3.add_edge("Lake Pollution","Income",-0.2)
test_fcm3.add_edge("Law Enforcement","Income",-0.2)
test_fcm3.add_edge("Wetlands","Income",0.8)
test_fcm3.add_edge("Law Enforcement","Fish",0.4)
test_fcm3.add_edge("Lake Pollution","Wetlands",-0.1)
test_fcm3.add_edge("Wetlands","Income",0.8)
test_fcm3.add_edge("Law Enforcement","Wetlands",0.2)

test_fcm3.set_value("Wetlands",0.3)
test_fcm3.set_value("Fish",0.5)
test_fcm3.set_value("Lake Pollution",0.6)
test_fcm3.set_value("Income",0.2)
test_fcm3.set_value("Law Enforcement",0.3)

print 'Running Test case 3'
print
print
pso=PSO(test_fcm3,{"Fish" : (0.6,0.8)})
pso.run_convergence()
