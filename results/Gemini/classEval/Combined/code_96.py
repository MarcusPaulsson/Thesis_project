class WeatherSystem:
    """
    This is a class representing a weather system that provides functionality to query weather information for a specific city and convert temperature units between Celsius and Fahrenheit.
    """

    def __init__(self, city):
        """
        Initialize the weather system with a city name.
        """
        self.city = city
        self.temperature = None
        self.weather = None

    def query(self, weather_data, tmp_units='celsius'):
        """
        Query the weather system for the weather and temperature of the city, and convert the temperature units based on the input parameter.

        :param weather_data: A dictionary of weather information for different cities.
        :param tmp_units: The temperature units to convert to ('celsius' or 'fahrenheit').
        :return: A tuple containing the temperature and weather of the city, or False if the city is not found.
        """
        if self.city not in weather_data:
            return False

        city_data = weather_data[self.city]
        temperature = city_data['temperature']
        weather = city_data['weather']
        temperature_units = city_data['temperature units']

        if temperature_units.lower() not in ('celsius', 'fahrenheit'):
            raise ValueError("Invalid temperature units in weather data. Must be 'celsius' or 'fahrenheit'.")

        if tmp_units.lower() not in ('celsius', 'fahrenheit'):
            raise ValueError("Invalid tmp_units. Must be 'celsius' or 'fahrenheit'.")

        if temperature_units.lower() != tmp_units.lower():
            if tmp_units.lower() == 'celsius':
                temperature = self.fahrenheit_to_celsius_static(temperature)
            else:  # tmp_units == 'fahrenheit'
                temperature = self.celsius_to_fahrenheit_static(temperature)

        return temperature, weather

    def set_city(self, city):
        """
        Set the city of the weather system.

        :param city: The city to set.
        """
        self.city = city

    def celsius_to_fahrenheit(self):
        """
        Convert the temperature from Celsius to Fahrenheit.

        :return: The temperature in Fahrenheit.
        """
        if self.temperature is None:
            raise ValueError("Temperature must be set before conversion.")
        return self.celsius_to_fahrenheit_static(self.temperature)

    def fahrenheit_to_celsius(self):
        """
        Convert the temperature from Fahrenheit to Celsius.

        :return: The temperature in Celsius.
        """
        if self.temperature is None:
            raise ValueError("Temperature must be set before conversion.")
        return self.fahrenheit_to_celsius_static(self.temperature)

    @staticmethod
    def celsius_to_fahrenheit_static(celsius):
        """
        Convert Celsius to Fahrenheit.
        """
        return (celsius * 9 / 5) + 32

    @staticmethod
    def fahrenheit_to_celsius_static(fahrenheit):
        """
        Convert Fahrenheit to Celsius.
        """
        return (fahrenheit - 32) * 5 / 9