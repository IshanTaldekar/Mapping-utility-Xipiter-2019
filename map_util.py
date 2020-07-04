import os
os.environ['PROJ_LIB'] = '/home/wraspy/anaconda3/share/proj'
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt


class Map:

    def __init__(self):
        
        boundary = [(38.146269, -76.428164),
                    (38.151625, -76.428683),
                    (38.151889, -76.431467),
                    (38.150594, -76.435361),
                    (38.147567, -76.432342),
                    (38.144667, -76.432947),
                    (38.143256, -76.434767),
                    (38.140464, -76.432636),
                    (38.140719, -76.426014),
                    (38.143761, -76.421206),
                    (38.147347, -76.423211),
                    (38.146131, -76.426653)]    # the boundary coordinates specified in the auvsi 2019 rules.

        search_area_boundary = [()]  # the search area boundary is provided at mission setup time.

        self.map = Basemap(projection='stere', resolution='f', area_thresh=10, lat_0=38.145689,
                           lon_0=-76.428732, satellite_height=100, fix_aspect=False, width=1700, height=1700)

        # Plot the boundary on the basemap projection initialized above.
        for bound_lat, bound_long in boundary:
            x, y = self.map(bound_long, bound_lat)
            self.map.plot(x, y, marker='X', markersize=7, markeredgecolor='black', color='red')

    # plot the aircraft route (GPS coordinates) on the map.
    def add_path(self, path=[]):
        for lat, lon in path:
            x, y = self.map(lon, lat)
            self.map.plot(x, y, marker='.', markersize=1, color='white')
    
    # plot the waypoint coordinates provided at mission time on the map. 
    def add_waypoints(self, waypoints=[]):
        for lat, lon in waypoints:
            x, y = self.map(lon, lat)
            self.map.plot(x, y, marker='X', markersize=7, markeredgecolor='black', color='orange')
    
    # display the map and add some aesthetic elements.
    def show_map(self):
        self.map.drawcoastlines(linewidth=1, color='black')
        self.map.drawmapboundary(fill_color='paleturquoise')
        self.map.fillcontinents(color='darkkhaki')
        plt.show()


if __name__ == '__main__':
    m = Map()
    m.add_waypoints([(38.140464, -76.432636)])
    m.show_map()
