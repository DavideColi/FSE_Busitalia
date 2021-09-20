'''
Time handling class: 
it can be either initialized with a string in the format hh:mm:ss, or with an integer which indicates the total number of seconds (h*3600+m*60+s)

It automatically handles operations like addition/subtraction with another Timestring, multiplication/division with a number (result is rounded to the nearest second),
and basic equality operators e.g. == != > < >= <=

Timestring is usable automatically in print statements and will (by default) use the string represantation of the time 
Timestring is hashable (hash is set with the integer value)

Public functions:

to_int(self)
    return the integer format of the time [total number of seconds]

to_str(self)
    return the string format of the time [hh:mm:ss]

'''


class TimeString:
    def __goodformat(self, x):
        if x< 10:
            return "0{0}".format(x)
        else:
            return str(x)
        
    
    def __init__(self, time):
        """ """
        #if we initialize the class with a float, it rounds it up to the neares integer (e.g. the nearest second)
        if isinstance(time, float):         
            time = round(time +0.5)
        if isinstance(time, int):
            self._timeint = time 
            h,min, sec = time//3600, (time//60)%60, time%60 
            self._timeintString = "{0}:{1}:{2}".format(self.__goodformat(h), self.__goodformat(min), self.__goodformat(sec) )
        elif isinstance(time, str):
            self._timeintString = time 
            h,min,sec = map(int, time.split(':')) 
            self._timeint =h*3600+min*60+sec  
        else:                                                               #if we are initializing a timesting with something that it is not a int, float, or str, it raises error
            raise Exception("Initialization of Timestring with type {0} has not been implemented\n[accepted types are: int, float, str]".format(type(time)))
    
    def __str__(self):
        return self._timeintString
    def __repr__(self):
        return self._timeintString
    
    def __add__(self, other):
        newtime = self._timeint + other._timeint 
        return TimeString(newtime)
    
    def __sub__(self, other):
        newtime= self._timeint - other._timeint 
        return TimeString(newtime)
    
    def __mul__(self, other):
        return TimeString(self._timeint*other)
    
    def __truediv__(self, other):
        return TimeString(self._timeint /other)
    
    def __div__(self, other):
        return self.__truediv__(other) 
    
    def __rmul__(self, other):
        return self.__mul__(other) 
    
    def __eq__(self, other):
        return (self._timeint == other._timeint) 
    
    def __ne__(self, other):
        return (self._timeint != other._timeint)
    
    def __lt__(self, other):
        return (self._timeint < other._timeint)
    
    def __gt__(self, other):
        return self._timeint > other._timeint 
    
    def __le__(self, other):
        return self._timeint <= other._timeint 
    
    def __ge__(self, other):
        return self._timeint >= other._timeint 
    
    def __hash__(self):
        return hash(self._timeint)
    
    def to_int(self):
        return self._timeint
    
    def to_str(self):
        return self._timeintString

