'''
space.py contains objects for Planets and other objects that may 
interact with ships in the tw_space_program
'''

class Planet(object):
    '''
    A planet object that specifies a n*n rectangular terrain on which
     ships can land or interact with
    '''

    def __init__(self, lat=0, lon=0):
        self.area = (lat, lon)
