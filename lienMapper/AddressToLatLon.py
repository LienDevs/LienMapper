import googlemaps

def findLatLng(fulladdress):
    gmaps = googlemaps.Client(key='AIzaSyC6kTxPzMaZvnUQpZGAXt5uTNX1KMeY0Wk')
    internalL=gmaps.geocode(fulladdress)

    LAT = internalL[0]['geometry']['location']['lat']
    LNG = internalL[0]['geometry']['location']['lng']

    return (LAT,LNG)


        


