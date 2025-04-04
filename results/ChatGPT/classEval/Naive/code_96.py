class WeatherSystem:
    """
    This is a class representing a weather system that provides functionality to query weather information for a specific city
    and convert temperature units between Celsius and Fahrenheit.
    """

    def __init__(self, city: str) -> None:
        """
        Initialize the weather system with a city name.
        """
        self.temperature = None
        self.weather = None
        self.city = city

    def query(self, weather_list: dict, tmp_units: str = 'celsius') -> tuple:
        """
        Query the weather system for the weather and temperature of the city, 
        and convert the temperature units based on the input parameter.
        
        :param weather_list: a dictionary of weather information for different cities, dict.
        :param tmp_units: the temperature units to convert to, str.
        :return: the temperature and weather of the city, tuple.
        
        >>> weatherSystem = WeatherSystem('New York')
        >>> weather_list = {
        ...     'New York': {'weather': 'sunny', 'temperature': 27, 'temperature units': 'celsius'},
        ...     'Beijing': {'weather': 'cloudy', 'temperature': 23, 'temperature units': 'celsius'}
        ... }
        >>> weatherSystem.query(weather_list)
        (27, 'sunny')
        """
        if self.city not in weather_list:
            raise ValueError("City not found in weather list.")
        
        city_weather = weather_list[self.city]
        self.weather = city_weather['weather']
        self.temperature = city_weather['temperature']

        if tmp_units.lower() == 'fahrenheit':
            self.temperature = self.celsius_to_fahrenheit()

        return self.temperature, self.weather

    def set_city(self, city: str) -> None:
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

    def celsius_to_fahrenheit(self) -> float:
        """
        Convert the temperature from Celsius to Fahrenheit.
        
        :return: the temperature in Fahrenheit, float.
        
        >>> weatherSystem = WeatherSystem('New York')
        >>> weatherSystem.temperature = 27
        >>> weatherSystem.celsius_to_fahrenheit()
        80.6
        """
        return (self.temperature * 9/5) + 32

    def fahrenheit_to_celsius(self) -> float:
        """
        Convert the temperature from Fahrenheit to Celsius.
        
        :return: the temperature in Celsius, float.
        
        >>> weatherSystem = WeatherSystem('New York')
        >>> weatherSystem.temperature = 80.6
        >>> weatherSystem.fahrenheit_to_celsius()
        27.0
        """
        return (self.temperature - 32) * 5/9