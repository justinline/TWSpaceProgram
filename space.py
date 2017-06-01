class Planet(object):
    '''A planet object that specifies a n*n rectangular terrain'''
    def __init__(self, lat=0, lon=0):
        self.area = (lat, lon)