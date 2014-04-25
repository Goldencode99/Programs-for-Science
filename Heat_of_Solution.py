def calcEnthalpy(molarMass,gramsCompound,gramsWater,initTemp,finalTemp):
	print "The Heat of Solution is "+str((((4.2*gramsWater*(finalTemp-initTemp))/(gramsCompound/molarMass))/1000)*-1)+" kJ/mol."
	return
calcEnthalpy(molarMass=80.052,gramsCompound=2.0,gramsWater=20.0,initTemp=0.0,finalTemp=-3.2)