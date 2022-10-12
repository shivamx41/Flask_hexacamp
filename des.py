from geopy.geocoders import ArcGIS,Nominatim
d = [1,2,3,4,5]
print(d[-1:])

nom = Nominatim(user_agent="MyApp",timeout=100)

data = nom.geocode("GObichettipalayam")
latitude = float(data.latitude)
longitude = float(data.longitude)

print(latitude,longitude)
print(type(latitude))
from geojson import Point, Feature, FeatureCollection, dump

print("++++++++++")
features=[]
temp = {"type": "Feature",
                          "properties" : {
                              "id" : 0,
                              "title" : "Hexa"
                          },
                "geometry": {
                    "type": "Point",
                    "coordinates": [longitude,latitude] }},
            
                
feature_collection = FeatureCollection(features)
print(feature_collection)

# <!-- var coordinates = '{{geo.features[0].geometry.coordinates}}';
#   console.log(typeof coordinates);
  
#   cd = coordinates.replace(/\[|\]/g,'').split(',')
#   var coordinate = []  
#   for(i = 0; i < cd.length; i++) {
#       temp = cd[i].replace(/&#39;/g, "").split(',')
#   //   result = x.map(s => s.slice(0,4));
#       console.log(temp)
#       coordinate.push(parseFloat(temp));
#   }
#   console.log(typeof coordinate);
#   console.log(coordinate);
#   console.log("++++++") -->