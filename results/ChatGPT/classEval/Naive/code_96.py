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

    def query(self, weather_list, tmp_units='celsius'):
        """
        Query the weather system for the weather and temperature of the city, and convert the temperature units based on the input parameter.
        :param weather_list: a dictionary of weather information for different cities, dict.
        :param tmp_units: the temperature units to convert to, str.
        :return: the temperature and weather of the city, tuple.
        """
        if self.city in weather_list:
            self.weather = weather_list[self.city]['weather']
            self.temperature = weather_list[self.city]['temperature']
            if tmp_units == 'fahrenheit':
                self.temperature = self.celsius_to_fahrenheit() if weather_list[self.city]['temperature units'] == 'celsius' else self.temperature
            elif tmp_units == 'celsius':
                self.temperature = self.fahrenheit_to_celsius() if weather_list[self.city]['temperature units'] == 'fahrenheit' else self.temperature
            return self.temperature, self.weather
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
        return (self.temperature * 9/5) + 32

    def fahrenheit_to_celsius(self):
        """
        Convert the temperature from Fahrenheit to Celsius.
        :return: the temperature in Celsius, float.
        """
        return (self.temperature - 32) * 5/9