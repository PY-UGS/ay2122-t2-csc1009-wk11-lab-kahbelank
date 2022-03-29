import datetime

class clockTime:
    
    def __init__ (self):
        #initialize the variables of hours, min, sec, time
        self.hrs = 0
        self.min = 0
        self.sec = 0
        self.time = datetime.time()

    def setHours(self, hrs):
        #set the hours
        self.hrs = hrs;
    
    def setMinutes(self, min):
        #set minutes
        self.min = min;
    
    def setSeconds(self, sec):
        #set seconds
        self.sec = sec;
    
    def setTime(self, hrs, min, sec):
        #format the time with the hrs, min and sec
        self.time = datetime.time (hrs, min, sec)
    
    def showTime(self):
        print("The time now is: ", self.time.strftime("%H:%M:%S"))

def main():
    clock = clockTime()
    

    hrInput = int(input("Enter Hours (0-23): "))

    #Getting the hours input from user from range of 0 to 24
    while (hrInput <0 or hrInput >24):
        print("Invalid Hours")
        hrInput = int(input("Enter Hours (0-23): "))
    
    #Getting the minutes input from user from range of 0 to 60
    minInput = int(input("Enter Minutes (0-59): "))

    while (minInput <0 or minInput >60):
        print("Invalid Minutes")
        minInput = int(input("Enter Minutes (0-59): "))
    
    #Getting the seconds input from user from range of 0 to 60
    secInput = int(input("Enter Seconds (0-59): "))

    while (secInput <0 or secInput >60):
        print("Invalid Seconds")
        secInput = int(input("Enter Seconds (0-60): "))

    clock.setTime(hrInput, minInput, secInput)

    clock.showTime()

if __name__ == "__main__":
    main()

    