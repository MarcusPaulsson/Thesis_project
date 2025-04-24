class WeatherSystem:
    """
    This is a class representing a weather system that provides functionality to query weather information for a specific city and convert temperature units between Celsius and Fahrenheit.
    """

    def __init__(self, city: str) -> None:
        """
        Initialize the weather system with a city name.
        """
        self.city = city

    def query(self, weather_list: dict, tmp_units: str = 'celsius') -> tuple | bool:
        """
        Query the weather system for the weather and temperature of the city, and convert the temperature units based on the input parameter.

        :param weather_list: A dictionary of weather information for different cities. The dictionary should have the following structure:
                             {'city_name': {'weather': 'weather_condition', 'temperature': temperature_value, 'temperature units': 'celsius' or 'fahrenheit'}}
        :param tmp_units: The temperature units to convert to ('celsius' or 'fahrenheit'). Defaults to 'celsius'.
        :return: A tuple containing the temperature and weather of the city, or False if the city is not found in the weather_list.
        """
        if not isinstance(weather_list, dict):
            raise TypeError("weather_list must be a dictionary.")

        if self.city not in weather_list:
            return False

        weather_data = weather_list[self.city]
        temperature = weather_data['temperature']
        weather = weather_data['weather']
        temperature_units = weather_data['temperature units']

        if tmp_units.lower() not in ('celsius', 'fahrenheit'):
            raise ValueError("tmp_units must be either 'celsius' or 'fahrenheit'.")

        if temperature_units.lower() not in ('celsius', 'fahrenheit'):
            raise ValueError("temperature units must be either 'celsius' or 'fahrenheit'.")

        if tmp_units.lower() == 'fahrenheit' and temperature_units.lower() == 'celsius':
            temperature = self.celsius_to_fahrenheit(temperature)
        elif tmp_units.lower() == 'celsius' and temperature_units.lower() == 'fahrenheit':
            temperature = self.fahrenheit_to_celsius(temperature)

        return (temperature, weather)

    def set_city(self, city: str) -> None:
        """
        Set the city of the weather system.
        :param city: The city to set.
        :return: None
        """
        if not isinstance(city, str):
            raise TypeError("City must be a string.")
        self.city = city

    def celsius_to_fahrenheit(self, celsius: float) -> float:
        """
        Convert the temperature from Celsius to Fahrenheit.
        :param celsius: The temperature in Celsius.
        :return: The temperature in Fahrenheit.
        """
        if not isinstance(celsius, (int, float)):
            raise TypeError("Temperature must be a number.")
        return celsius * 9 / 5 + 32

    def fahrenheit_to_celsius(self, fahrenheit: float) -> float:
        """
        Convert the temperature from Fahrenheit to Celsius.
        :param fahrenheit: The temperature in Fahrenheit.
        :return: The temperature in Celsius.
        """
        if not isinstance(fahrenheit, (int, float)):
            raise TypeError("Temperature must be a number.")
        return (fahrenheit - 32) * 5 / 9