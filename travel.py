class Travel:


    def __init__(self, dest, duration, package, price, available):
        self.dest = dest
        self.duration = duration
        self.package = package
        self.price = price
        self.available = available       


    @property
    def tripName(self):
        return '{}-{}D'.format(self.dest, self.duration)


    def __repr__(self):
        return "Travel('{} Days', '{}', {})".format(self.tripName, self.package, self.price)

class Package:
    def __init__(self, package, hotelStar, localTrans, guide):
        self.package = package
        self.hotelStar = hotelStar
        self.localTrans = localTrans
        self.guide = guide
