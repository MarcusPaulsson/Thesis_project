class WeatherSystem:
    """
    This is a class representing a weather system that provides functionality to query weather information for a specific city and convert temperature units between Celsius and Fahrenheit.
    """

    def __init__(self, city) -> None:
        """
        Initialize the weather system with a city name.
        """
        self.temperature = None
        self.weather = None
        self.city = city
        self.weather_list = {}

    def query(self, weather_list, tmp_units = 'celsius'):
        """
        Query the weather system for the weather and temperature of the city,and convert the temperature units based on the input parameter.
        :param weather_list: a dictionary of weather information for different cities,dict.
        :param tmp_units: the temperature units to convert to, str.
        :return: the temperature and weather of the city, tuple.
        """
        if self.city in weather_list:
            city_data = weather_list[self.city]
            temperature = city_data['temperature']
            temperature_units = city_data['temperature units']
            weather = city_data['weather']

            if tmp_units == 'fahrenheit' and temperature_units == 'celsius':
                temperature = self.celsius_to_fahrenheit()
            elif tmp_units == 'celsius' and temperature_units == 'fahrenheit':
                temperature = self.fahrenheit_to_celsius()

            return (temperature, weather)
        else:
            return False

    def set_city(self, city):
        """
        Set the city of the weather system.
        :param city: the city to set, str.
        :return: None
        """
        self.city = city

    def celsius_to_fahrenheit(self):
        """
        Convert the temperature from Celsius to Fahrenheit.
        :return: the temperature in Fahrenheit, float.
        """
        if self.temperature is not None:
            return (self.temperature * 9/5) + 32
        else:
            return None

    def fahrenheit_to_celsius(self):
        """
        Convert the temperature from Fahrenheit to Celsius.
        :return: the temperature in Celsius, float.
        """
        if self.temperature is not None:
            return (self.temperature - 32) * 5/9
        else:
            return None