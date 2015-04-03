
class jtkHVAC:

    #Conventional HVAC Control switches
    ########################
    # G     - Fan
    # Y     - 1st Stage Cooling
    # Y2    - 2nd Stage Cooling
    # W     - 1st Stage Heating
    # W2/E  - 2nd Stage Heating
    # W3/O/B- 3rd Stage Heating
    setPoint = {'temp': 68, 'status': 'Home'}
    temp = 68 
    def getTemp(self):
         #@@ either add console temp input or get thermometer
        #print "Temp is " +str(self.temp)+ "F"
        return self.temp

    def setTemp(self, temp):
        self.temp = temp
    #@@need to make a set setpoint method to do a temporary range    
    def setSetPoint(self, setPoint):
        self.setPoint['temp'] = setPoint['temp']
        self.setPoint['status'] = setPoint['status']
        
    def controlUpdate(self, sched):
        temp = self.getTemp()

        #sets the setpoint to the current setpoint in the schedule
        self.setSetPoint(sched.getCurrentSeg());
        #cooling
        if(temp > self.setPoint['temp'] + .3): # + .3 avoids frequent switching 
            #low cool Y and G on
            if(temp <= self.setPoint['temp'] +2):
                print("low cool G and Y on")
            #high cool
            else:
                print("high cool G, Y and Y2 on")

        #heating
        if(temp < self.setPoint['temp'] -.3): # + .3 avoids frequent switching
            #low heat G and W
            if(temp >= self.setPoint['temp'] -2):
                print("low heat G and W on")
            #medium heat
            elif(temp >= self.setPoint['temp'] -4 and temp < self.setPoint['temp'] -2):
                print("low heat G, W and W2 on")
            #high heat
            else:
                print("low heat G, W, W2 and W3 on")
