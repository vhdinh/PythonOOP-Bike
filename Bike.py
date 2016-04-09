class Bike(object):
    def __init__(self, price, max_speed,miles = 0):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles

    def riding(self):
        print "Riding"
        self.miles = self.miles + 10
        return self.miles

    def reverse(self):
        print "Reversing"
        if self.miles < 5:
            return self.miles
        else:
            self.miles = self.miles - 5
        return self.miles

    def displayInfo(self):
        return self.price, self.max_speed, self.miles

bike1 = Bike("$100", "150mph")
bike2 = Bike("$150", "200mph")
bike3 = Bike("$200", "250mph")
print "\n bike1"
print bike1.riding()
print bike1.riding()
print bike1.riding()
print bike1.reverse()
print bike1.displayInfo()

print "\n bike2"
print bike2.riding()
print bike2.riding()
print bike2.reverse()
print bike2.reverse()
print bike2.displayInfo()

print "\n bike3"
print bike3.reverse()
print bike3.reverse()
print bike3.reverse()
print bike3.displayInfo()

