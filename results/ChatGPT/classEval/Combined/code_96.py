class WeatherSystem:
    """
    A class representing a weather system that provides functionality to query weather information for a specific city 
    and convert temperature units between Celsius and Fahrenheit.
    """

    def __init__(self, city: str) -> None:
        """
        Initialize the weather system with a city name.
        :param city: The name of the city.
        """
        self.city = city
        self.temperature = None
        self.weather = None

    def query(self, weather_list: dict, tmp_units: str = 'celsius') -> tuple:
        """
        Query the weather system for the weather and temperature of the city, and convert the temperature units based on the input parameter.
        :param weather_list: A dictionary of weather information for different cities.
        :param tmp_units: The temperature units to convert to ('celsius' or 'fahrenheit').
        :return: A tuple containing the temperature and weather of the city, or False if the city is not found.
        """
        city_weather = weather_list.get(self.city)
        if city_weather is None:
            return False

        self.weather = city_weather['weather']
        self.temperature = city_weather['temperature']

        if tmp_units.lower() == 'fahrenheit':
            self.temperature = self.celsius_to_fahrenheit(self.temperature)

        return self.temperature, self.weather

    def set_city(self, city: str) -> None:
        """
        Set the city of the weather system.
        :param city: The city to set.
        """
        self.city = city

    @staticmethod
    def celsius_to_fahrenheit(celsius: float) -> float:
        """
        Convert the temperature from Celsius to Fahrenheit.
        :param celsius: The temperature in Celsius.
        :return: The temperature in Fahrenheit.
        """
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit: float) -> float:
        """
        Convert the temperature from Fahrenheit to Celsius.
        :param fahrenheit: The temperature in Fahrenheit.
        :return: The temperature in Celsius.
        """
        return (fahrenheit - 32) * 5/9