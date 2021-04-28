import gmplot
apikey = 'AIzaSyDNhX6JLoc3uTlVV30AhkIZ_wFDoqnYYUI' # (your API key here)
gmap = gmplot.GoogleMapPlotter.from_geocode('Chiyoda City, Tokyo', apikey=apikey)
gmap.draw("map.html")