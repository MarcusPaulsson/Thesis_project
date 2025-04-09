class WeatherSystem:
    """
    This is a class representing a weather system that provides functionality to query weather information for a specific city and convert temperature units between Celsius and Fahrenheit.
    """

    def __init__(self, city) -> None:
        """
        Initialize the weather system with a city name.
        """
        self.city = city
        self.temperature = None
        self.weather = None

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
                temperature = self.celsius_to_fahrenheit(temperature)
            elif tmp_units == 'celsius' and temperature_units == 'fahrenheit':
                temperature = self.fahrenheit_to_celsius(temperature)

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

    def celsius_to_fahrenheit(self, celsius):
        """
        Convert the temperature from Celsius to Fahrenheit.
        :param celsius: the temperature in Celsius, float.
        :return: the temperature in Fahrenheit, float.
        """
        return (celsius * 9/5) + 32

    def fahrenheit_to_celsius(self, fahrenheit):
        """
        Convert the temperature from Fahrenheit to Celsius.
        :param fahrenheit: the temperature in Fahrenheit, float.
        :return: the temperature in Celsius, float.
        """
        return (fahrenheit - 32) * 5/9