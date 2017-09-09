class Time:
    '''class definition for Time''' 
    def __init__(self, hours=0, mins=0, secs=0):
        '''initialise time object'''
        self.hours = hours
        self.mins = mins
        self.secs = secs
        return

    def __str__(self):
        '''print time object'''
        return(("%d:%d:%d")%(self.hours, self.mins, self.secs))


    def add(self, t):
        '''adds 2 time objects and returns the new object'''
        ttemp = Time()
        
        ttemp.hours = self.hours + t.hours
        ttemp.mins = self.mins + t.mins
        ttemp.secs = self.secs + t.secs

        return ttemp 

if __name__ == "__main__":
    '''main function'''
    t1 = Time(10, 10, 10)
    t2 = Time(20, 20, 20)
    t3 = t2.add(t1)

    print "t1 =>", t1
    print "t2 =>", t2
    print "t3 =>", t3

    #EOF