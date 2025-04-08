class WeatherSystem:
    """
    Represents a weather system providing weather information and temperature conversions.
    """

    def __init__(self, city: str) -> None:
        """
        Initializes the WeatherSystem with a city.

        Args:
            city: The name of the city.
        """
        self.city = city

    def query(self, weather_data: dict, temp_unit: str = 'celsius') -> tuple[float, str] | bool:
        """
        Queries weather information for the city and converts temperature units if needed.

        Args:
            weather_data: A dictionary containing weather information for different cities.
                Example: {'New York': {'weather': 'sunny', 'temperature': 27, 'temperature units': 'celsius'}}
            temp_unit: The desired temperature unit ('celsius' or 'fahrenheit'). Defaults to 'celsius'.

        Returns:
            A tuple containing the temperature and weather description, or False if the city is not found.
            Example: (27, 'sunny') or False
        """
        if self.city not in weather_data:
            return False

        city_data = weather_data[self.city]
        temperature = city_data['temperature']
        weather = city_data['weather']
        current_unit = city_data['temperature units']

        if temp_unit.lower() == 'fahrenheit' and current_unit.lower() == 'celsius':
            temperature = self.celsius_to_fahrenheit(temperature)
        elif temp_unit.lower() == 'celsius' and current_unit.lower() == 'fahrenheit':
            temperature = self.fahrenheit_to_celsius(temperature)

        return temperature, weather

    def set_city(self, city: str) -> None:
        """
        Sets the city for the weather system.

        Args:
            city: The name of the city.
        """
        self.city = city

    def celsius_to_fahrenheit(self, celsius: float) -> float:
        """
        Converts Celsius to Fahrenheit.

        Args:
            celsius: The temperature in Celsius.

        Returns:
            The temperature in Fahrenheit.
        """
        return celsius * 9 / 5 + 32

    def fahrenheit_to_celsius(self, fahrenheit: float) -> float:
        """
        Converts Fahrenheit to Celsius.

        Args:
            fahrenheit: The temperature in Fahrenheit.

        Returns:
            The temperature in Celsius.
        """
        return (fahrenheit - 32) * 5 / 9