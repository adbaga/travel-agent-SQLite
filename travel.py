class Travel:
    """A sample Employee class"""

    def __init__(self, dest, duration, package, price, available):
        self.dest = dest
        self.duration = duration
        self.package = package
        self.price = price
        self.available = available
        
        


    @property
    def tripName(self):
        return '{}.{}D'.format(self.dest, self.duration)


    def __repr__(self):
        return "Travel('{} Days', '{}', {})".format(self.tripName, self.package, self.price)