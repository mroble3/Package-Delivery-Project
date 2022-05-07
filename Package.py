class Package:

    def __init__(self, packageid, address_location, address, city, state, zip, delivery, size, note, delivery_start, delivery_status):
        self.pkgid = packageid
        self.add_location = address_location
        self.addy = address
        self.city = city
        self.state = state
        self.zip = zip
        self.delvr = delivery
        self.sze = size
        self.nte = note
        self.delvry_strt = delivery_start
        self.delvry_stats = delivery_status

        self.deliverytime = None
        self.mileage = 0

    def __str__(self):
        return '{self.pkgid} {self.addy} {self.city} {self.state} {self.zip} {self.deliverytime} {self.delvr} {self.mileage} {self.delvry_stats}'.format(self = self)

    def isDelivered (self):
        return self.deliverytime is not None

    '''def isNotDelivered (self):
        return self.deliverytime is None'''

    def isNotDelivered(self):
        return not self.isDelivered()


