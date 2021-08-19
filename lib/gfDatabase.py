class DataBase:
    def __init__(self):
        self.df = None
        self.path = None
        self.outpath = None
        self.col_dict = {
            'Integer identifying grain': 'n',
            'Average orientation (phi1, PHI, phi2) in degrees': 'ori-d',
            'Average orientation (phi1, PHI, phi2) in radians': 'ori-r',
            'Average Position (x, y) in microns': 'pos',
            'Average Image Quality (IQ)': 'iq',
            'Average Confidence Index (CI)': 'ci',
            'An integer identifying the phase': 'phase',
            'Edge grain (1) or interior grain (0)': 'edge',
            'Number of measurement points in the grain': 'points',
            'Area of grain in square microns': 'area',
            'Diameter of grain in microns': 'dia',
            'ASTM grain size': 'ASTM',
            'Aspect ratio of ellipse fit to grain': 'aspect',
            'Length of major axis of ellipse fit to grain in microns': 'majEll',
            'Length of minor axis of ellipse fit to grain in microns': 'minEll',
            'Grain ellipticity': 'ellipt',
            'Grain circularity': 'circul',
            'Maximmum Feret diameter': 'maxFeret',
            'Minimum Feret diameter': 'minFeret'
        }
        self.outdata = None

    def write_to_df(self, data):
        self.df = data

    def clear_data(self):
        self.df = None

    def write_to_path(self, p):
        self.path = p

    def clear_path(self):
        self.path = None

    def write_outpath(self, p):
        self.outpath = p

    def clear_outpath(self):
        self.outpath = None

    def write_to_outdata(self, data):
        self.outdata = data

    def clear_outdata(self):
        self.outdata = None
