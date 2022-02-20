from geopy.geocoders import Nominatim

class Geolocator:

    def get_coordinates(location):
        """Grabs the lat and long coordinates of a location

        Args:
            location (str): A location searched by user

        Returns:
            tuple : Location object values, lat and lognitute
        """
        geolocator = Nominatim(user_agent="App")
        location = geolocator.geocode(location)
        return (location.latitude, location.longitude)