class WeatherSystem:
    """
    This class represents a weather system that provides functionality to query weather information for a specific city
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
        Query the weather system for the weather and temperature of the city, and convert the temperature units based on the input parameter.
        
        :param weather_list: a dictionary of weather information for different cities.
        :param tmp_units: the temperature units to convert to, either 'celsius' or 'fahrenheit'.
        :return: the temperature and weather of the city, or False if the city is not found.
        """
        if self.city in weather_list:
            self.weather = weather_list[self.city]['weather']
            self.temperature = weather_list[self.city]['temperature']
            
            if weather_list[self.city]['temperature units'] == 'fahrenheit':
                self.temperature = self.fahrenheit_to_celsius()

            if tmp_units == 'fahrenheit':
                return (self.celsius_to_fahrenheit(), self.weather)
            elif tmp_units == 'celsius':
                return (self.temperature, self.weather)
        
        return False

    def set_city(self, city: str) -> None:
        """
        Set the city of the weather system.
        
        :param city: the city to set.
        """
        self.city = city

    def celsius_to_fahrenheit(self) -> float:
        """
        Convert the temperature from Celsius to Fahrenheit.
        
        :return: the temperature in Fahrenheit.
        """
        return (self.temperature * 9/5) + 32

    def fahrenheit_to_celsius(self) -> float:
        """
        Convert the temperature from Fahrenheit to Celsius.
        
        :return: the temperature in Celsius.
        """
        return (self.temperature - 32) * 5/9