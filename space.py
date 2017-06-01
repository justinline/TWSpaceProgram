class Planet(object):
    def __init__(self, lat=0, lon=0):
        self.lat = lat
        self.lon = lon
        self.area = (self.lat, self.lon)