import math

class TimeSpan:
    
    def __init__(self, seconds=0.0, minutes=0.0, hours=0.0):
        self.set_time(seconds, minutes, hours)
    
    
    def __str__(self):
        return f"Hours: {round(self.hours)}, Minutes: {round(self.minutes)}, Seconds: {round(self.seconds)}"
    
    def set_time(self, seconds=0.0, minutes=0.0, hours=0.0):
            total_seconds = hours * 3600 + minutes * 60 + seconds
            self.hours = total_seconds // 3600
            self.minutes = (total_seconds % 3600) // 60
            self.seconds = (total_seconds % 3600) % 60  
    
    def get_hours(self):
        return self.hours
    
    def get_minutes(self):
        return self.minutes
    
    def get_seconds(self):
        return self.seconds
    
    def get_total_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds
    
    def __gt__(self, other):
        return self.get_total_seconds() > other.get_total_seconds()

    def __ge__(self, other):
        return self.get_total_seconds() >= other.get_total_seconds()
    
    def __lt__(self, other):
        return self.get_total_seconds() < other.get_total_seconds()

    def __le__(self, other):
        return self.get_total_seconds() <= other.get_total_seconds()
    
    def __eq__(self, other):
        return self.get_total_seconds() == other.get_total_seconds()
    
    def __ne__(self, other):
        return self.get_total_seconds() != other.get_total_seconds()   
    
    def __add__(self, other):
        augend = self.get_total_seconds()
        addend = other.get_total_seconds()
        sum = augend + addend
        return TimeSpan(sum)

    def __mul__(self, other):
        return TimeSpan(self.seconds * other.seconds , self.minutes * other.minutes, self.hours * other.hours)
    
    def __sub__(self, other):
        minuend = self.get_total_seconds()
        subtrahend = other.get_total_seconds()
        difference = minuend - subtrahend
        return TimeSpan(difference)
   
    def __neg__(self):
        self.seconds = -self.seconds
        self.minutes = -self.minutes
        self.hours = -self.hours
        return self
        
    
    def __isub__(self, other):
        self.set_time(self.seconds - other.seconds , self.minutes - other.minutes, self.hours - other.hours)
        return self

    def __iadd__(self, other):
        self.set_time(self.seconds + other.seconds , self.minutes + other.minutes, self.hours + other.hours)
        return self