from flask import Flask , jsonify ,request, render_template,redirect,url_for
import random as r


from sqlalchemy import create_engine, MetaData,Table,Column,Integer,String, Float
from geopy.geocoders import ArcGIS,Nominatim
app = Flask(__name__)
nom = ArcGIS()



engine = create_engine('mysql://root:brainbeam@localhost/demo', echo = True)
meta = MetaData()

campground = Table(
   'campground', meta, 
   Column('id', Integer, primary_key = True), 
   Column('title', String(30)), 
   Column('description', String(60)),
   Column('image', String(60)),
   Column('price', String(20)),
   Column('email', String(20)),
   Column('mobile', String(20)),
   Column('location', String(60)),
   Column('latitude',Float(30)),
   Column('lantitude', Float(30))
)


conn = engine.connect()

def create_table():
    meta.create_all(engine)
    
    
@app.route('/')
def welcome():
    return render_template("demo.html")


@app.get('/campgrounds')
def display_all_campgrounds():
  
 
    return render_template("displayallcampground.html")

@app.post('/newcampground')
def new_campground():
   
        return render_template("newcampground.html")
    
            
    
# create_table()
if __name__ == '__main__':
    app.run(debug=True)
    
    # map.on('load', () => {
    #     // Add a new source from our GeoJSON data and
    #     // set the 'cluster' option to true. GL-JS will
    #     // add the point_count property to your source data.
    #     map.addSource('myfile_map', {
    #         type: 'geojson',
    #         // Point to GeoJSON data. This example visualizes all M1.0+ earthquakes
    #         // from 12/22/15 to 1/21/16 as logged by USGS' Earthquake hazards program.
    #         data: 'http://127.0.0.1:8887/myfile_map.geojson',
            
    #         cluster: true,
    #         clusterMaxZoom: 14, // Max zoom to cluster points on
    #         clusterRadius: 50 // Radius of each cluster when clustering points (defaults to 50)
    #     });

    #     map.addLayer({
    #         id: 'clusters',
    #         type: 'circle',
    #         source: 'myfile_map',
    #         filter: ['has', 'point_count'],
    #         paint: {
    #             // Use step expressions (https://docs.mapbox.com/mapbox-gl-js/style-spec/#expressions-step)
    #             // with three steps to implement three types of circles:
    #             //   * Blue, 20px circles when point count is less than 100
    #             //   * Yellow, 30px circles when point count is between 100 and 750
    #             //   * Pink, 40px circles when point count is greater than or equal to 750
    #             'circle-color': [
    #                 'step',
    #                 ['get', 'point_count'],
    #                 '#51bbd6',
    #                 100,
    #                 '#f1f075',
    #                 750,
    #                 '#f28cb1'
    #             ],
    #             'circle-radius': [
    #                 'step',
    #                 ['get', 'point_count'],
    #                 20,
    #                 100,
    #                 30,
    #                 750,
    #                 40
    #             ]
    #         }
    #     });

    #     map.addLayer({
    #         id: 'cluster-count',
    #         type: 'symbol',
    #         source: 'myfile_map',
    #         filter: ['has', 'point_count'],
    #         layout: {
    #             'text-field': '{point_count_abbreviated}',
    #             'text-font': ['DIN Offc Pro Medium', 'Arial Unicode MS Bold'],
    #             'text-size': 12
    #         }
    #     });

    #     map.addLayer({
    #         id: 'unclustered-point',
    #         type: 'circle',
    #         source: 'myfile_map',
    #         filter: ['!', ['has', 'point_count']],
    #         paint: {
    #             'circle-color': '#11b4da',
    #             'circle-radius': 4,
    #             'circle-stroke-width': 1,
    #             'circle-stroke-color': '#fff'
    #         }
    #     });

    #     // inspect a cluster on click
    #     map.on('click', 'clusters', (e) => {
    #         const features = map.queryRenderedFeatures(e.point, {
    #             layers: ['clusters']
    #         });
    #         const clusterId = features[0].properties.cluster_id;
    #         map.getSource('myfile_map').getClusterExpansionZoom(
    #             clusterId,
    #             (err, zoom) => {
    #                 if (err) return;

    #                 map.easeTo({
    #                     center: coordinates,
    #                     zoom: zoom
    #                 });
    #             }
    #         );
    #     });

    #     // When a click event occurs on a feature in
    #     // the unclustered-point layer, open a popup at
    #     // the location of the feature, with
    #     // description HTML from its properties.
    #     map.on('click', 'unclustered-point', (e) => {
    #         const coordinates = e.coordinates.slice();
    #         const mag = e.coordinates;
            
    #         // Ensure that if the map is zoomed out such that
    #         // multiple copies of the feature are visible, the
    #         // popup appears over the copy being pointed to.
    #         while (Math.abs(e.lngLat.lng - coordinates[0]) > 180) {
    #             coordinates[0] += e.lngLat.lng > coordinates[0] ? 360 : -360;
    #         }

    #         new mapboxgl.Popup()
    #             .setLngLat(coordinates)
    #             .setHTML(
    #                 `latlong: ${mag}`
    #             )
    #             .addTo(map);
    #     });

    #     map.on('mouseenter', 'clusters', () => {
    #         map.getCanvas().style.cursor = 'pointer';
    #     });
    #     map.on('mouseleave', 'clusters', () => {
    #         map.getCanvas().style.cursor = '';
    #     });
    # });