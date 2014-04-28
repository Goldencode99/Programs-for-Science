def calcEnthalpy(molarMass,gramsCompound,gramsWater,initTemp,finalTemp):
	print "The Heat of Solution is "+str((((4.2*gramsWater*(finalTemp-initTemp))/(gramsCompound/molarMass))/1000)*-1)+" kJ/mol."
	return
print "This program can be used to calculate the \"Heat of Solution\" for a given compound.\nNOTE: Please enter all values to at least the first decimal."
molarMass = input("Enter molar mass of compound: ")
gramsCompound = input("Enter grams of compound used: ")
gramsWater = input("Enter grams of water used: ")
initTemp = input("Enter initial temperature of solution: ")
finalTemp = input("Enter final temperature of solution: ")
calcEnthalpy(molarMass=molarMass,gramsCompound=gramsCompound,gramsWater=gramsWater,initTemp=initTemp,finalTemp=finalTemp)