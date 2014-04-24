def calcEnthalpy(molarMass,gramsCompound,gramsWater,initTemp,finalTemp):
	print "The Heat of Solution is " + str((((4.2 * gramsWater * (finalTemp - initTemp))/(gramsCompound / molarMass))/1000) * -1) + " kJ/mol."
	return
calcEnthalpy(molarMass=40.0,gramsCompound=3.0,gramsWater=50.0,initTemp=0.0,finalTemp=12.5)