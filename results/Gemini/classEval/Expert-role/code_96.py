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
        >>> weatherSystem = WeatherSystem('New York')
        >>> weather_list = {'New York': {'weather': 'sunny','temperature': 27,'temperature units': 'celsius'},'Beijing': {'weather': 'cloudy','temperature': 23,'temperature units': 'celsius'}}
        >>> weatherSystem.query(weather_list)
        (27, 'sunny')

        """
        if self.city in weather_list:
            weather_data = weather_list[self.city]
            temperature = weather_data['temperature']
            weather = weather_data['weather']
            temperature_units = weather_data['temperature units']

            if temperature_units != tmp_units:
                if tmp_units == 'celsius':
                    if temperature_units == 'fahrenheit':
                        temperature = self.fahrenheit_to_celsius_static(temperature)
                elif tmp_units == 'fahrenheit':
                    if temperature_units == 'celsius':
                        temperature = self.celsius_to_fahrenheit_static(temperature)

            return (temperature, weather)
        else:
            return False

    def set_city(self, city):
        """
        Set the city of the weather system.
        :param city: the city to set, str.
        :return: None
        >>> weatherSystem = WeatherSystem('New York')
        >>> weatherSystem.set_city('Beijing')
        >>> weatherSystem.city
        'Beijing'

        """
        self.city = city

    def celsius_to_fahrenheit(self):
        """
        Convert the temperature from Celsius to Fahrenheit.
        :return: the temperature in Fahrenheit, float.
        >>> weatherSystem = WeatherSystem('New York')
        >>> weatherSystem.temperature = 27
        >>> weatherSystem.celsius_to_fahrenheit()
        80.6

        """
        return self.celsius_to_fahrenheit_static(self.temperature)

    def fahrenheit_to_celsius(self):
        """
        Convert the temperature from Fahrenheit to Celsius.
        :return: the temperature in Celsius, float.
        >>> weatherSystem = WeatherSystem('New York')
        >>> weatherSystem.temperature = 80.6
        >>> weatherSystem.fahrenheit_to_celsius()
        26.999999999999996

        """
        return self.fahrenheit_to_celsius_static(self.temperature)

    @staticmethod
    def celsius_to_fahrenheit_static(celsius):
        """
        Convert Celsius to Fahrenheit.
        """
        return celsius * 9 / 5 + 32

    @staticmethod
    def fahrenheit_to_celsius_static(fahrenheit):
        """
        Convert Fahrenheit to Celsius.
        """
        return (fahrenheit - 32) * 5 / 9