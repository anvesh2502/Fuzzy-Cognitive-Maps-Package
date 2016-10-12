from FCM import FCM

def f() : return 2

fcm=FCM()
fcm.add_concept("Obesity")
fcm.add_concept("Depression")
fcm.add_edge("Obesity","Depression",0.5) #edge weights MUST be limited
fcm.add_edge("Depression","Antidepressants",0.6) #if a concept doesn't
#fcm.remove_concept("Depression") #removes the concept and all associated edges
fcm.draw()
