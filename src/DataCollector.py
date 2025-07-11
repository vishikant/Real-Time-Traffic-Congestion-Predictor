import googlemaps #google maps api is used to get the distance and duration of the route
from datetime import datetime
from config import GOOGLE_API_KEY, ORIGIN, DESTINATION

def get_live_traffic_data():
    """
    Fetches live traffic data from Google Maps API.
    Returns:
        dict: Contains distance and duration of the route.
    """
    gmaps=googlemaps.Client(key=GOOGLE_API_KEY)
    now = datetime.now() # Get the current time
    result=gmaps.distance_matrix(
        origins=ORIGIN,
        destinations=DESTINATION,
        departure_time=datetime.now(),
        traffic_model='best_guess', # 'best_guess' is used to get the best estimate of traffic conditions
    )

    data=result['rows'][0]['elements'][0] # Extracting the first element of the result
    travel_time_sec=data['duration_in_traffic']['value'] # Getting the duration in traffic
    distance_meters=data['distance']['value'] 
    return{
          "timestamp": now.strftime("%Y-%m-%d %H:%M:%S"),
        "travel_time_min": travel_time_sec / 60,
        "distance_km": distance_meters / 1000
    }
if __name__ == "__main__":
    traffic_data = get_live_traffic_data()