class WeatherSystem:
    """
    A class representing a weather system that provides functionality to query weather information for a specific city 
    and convert temperature units between Celsius and Fahrenheit.
    """

    def __init__(self, city: str) -> None:
        """
        Initialize the weather system with a city name.
        :param city: The name of the city for weather queries.
        """
        self.city = city
        self.temperature = None
        self.weather = None

    def query(self, weather_list: dict, tmp_units: str = 'celsius') -> tuple:
        """
        Query the weather system for the weather and temperature of the city, 
        and convert the temperature units based on the input parameter.
        
        :param weather_list: A dictionary of weather information for different cities.
        :param tmp_units: The temperature units to convert to, either 'celsius' or 'fahrenheit'.
        :return: A tuple containing the temperature and weather of the city, or False if the city is not found.
        """
        city_weather = weather_list.get(self.city)
        if not city_weather:
            return False

        self.weather = city_weather['weather']
        self.temperature = city_weather['temperature']
        
        if tmp_units.lower() == 'fahrenheit':
            self.temperature = self.celsius_to_fahrenheit(self.temperature) if self.is_celsius(city_weather) else self.temperature
        
        return self.temperature, self.weather

    def set_city(self, city: str) -> None:
        """
        Set the city of the weather system.
        
        :param city: The city to set.
        """
        self.city = city

    def celsius_to_fahrenheit(self, celsius: float = None) -> float:
        """
        Convert the temperature from Celsius to Fahrenheit.
        
        :param celsius: Temperature in Celsius. If None, uses the instance temperature.
        :return: The temperature in Fahrenheit.
        """
        if celsius is None:
            celsius = self.temperature
        return (celsius * 9/5) + 32

    def fahrenheit_to_celsius(self, fahrenheit: float = None) -> float:
        """
        Convert the temperature from Fahrenheit to Celsius.
        
        :param fahrenheit: Temperature in Fahrenheit. If None, uses the instance temperature.
        :return: The temperature in Celsius.
        """
        if fahrenheit is None:
            fahrenheit = self.temperature
        return (fahrenheit - 32) * 5/9

    def is_celsius(self, city_weather: dict) -> bool:
        """
        Check if the temperature units of the city weather data is in Celsius.
        
        :param city_weather: The weather data dictionary for the city.
        :return: True if the temperature is in Celsius, False otherwise.
        """
        return city_weather.get('temperature units', '').lower() == 'celsius'