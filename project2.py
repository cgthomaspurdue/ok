import math as m 

eOut = 120
g = 9.80
wDensity = 1000

turbineEfficiency = .92



def get_eTloss(turbineEfficiency):
    return (eOut*(1/turbineEfficiency)-1)

def get_headLoss(Hf,Hl,Hv,Hd):
    return (eOut*(1/turbineEfficiency)-1)
    return ((Hf*Hl*m.sqrt(Hv))/(Hd*2*g))




#effTurbine = 
#pipeD
#pipeL
#pipeF
#depth
#H
#qPump
#qTurbine
#effK1
#effK2

