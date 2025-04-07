class WeatherSystem:
    """
    A class representing a weather system that provides functionality to query weather information for a specific city and convert temperature units between Celsius and Fahrenheit.
    """

    def __init__(self, city):
        """
        Initializes the weather system with a city name.

        Args:
            city (str): The name of the city.
        """
        self.city = city
        self.weather_data = None  # Store weather data for the city

    def query(self, weather_data, temp_units='celsius'):
        """
        Queries the weather system for the weather and temperature of the city, and converts the temperature units if necessary.

        Args:
            weather_data (dict): A dictionary of weather information for different cities.  Each city's data should include 'weather', 'temperature', and 'units' (celsius or fahrenheit).
            temp_units (str, optional): The desired temperature units ('celsius' or 'fahrenheit'). Defaults to 'celsius'.

        Returns:
            tuple: A tuple containing the temperature and weather of the city, or None if the city is not found.  The temperature will be in the requested units.

        Raises:
            ValueError: If temp_units is not 'celsius' or 'fahrenheit'.
            TypeError: If temperature is not a number.
        """
        if not isinstance(weather_data, dict):
            raise TypeError("weather_data must be a dictionary")
        if temp_units not in ('celsius', 'fahrenheit'):
            raise ValueError("temp_units must be 'celsius' or 'fahrenheit'")

        if self.city in weather_data:
            city_data = weather_data[self.city]

            if not isinstance(city_data, dict):
                raise TypeError(f"Weather data for {self.city} must be a dictionary")

            if 'weather' not in city_data or 'temperature' not in city_data or 'units' not in city_data:
                raise ValueError(f"Weather data for {self.city} is missing required keys (weather, temperature, units)")

            weather = city_data['weather']
            temperature = city_data['temperature']
            current_units = city_data['units']

            if not isinstance(temperature, (int, float)):
                raise TypeError("Temperature must be a number")

            if current_units not in ('celsius', 'fahrenheit'):
                 raise ValueError(f"Units must be 'celsius' or 'fahrenheit' for {self.city}")


            if current_units != temp_units:
                if temp_units == 'fahrenheit' and current_units == 'celsius':
                    temperature = self.celsius_to_fahrenheit(temperature)
                elif temp_units == 'celsius' and current_units == 'fahrenheit':
                    temperature = self.fahrenheit_to_celsius(temperature)

            return (temperature, weather)
        else:
            return None

    def set_city(self, city):
        """
        Sets the city of the weather system.

        Args:
            city (str): The city to set.
        """
        if not isinstance(city, str):
            raise TypeError("City must be a string")
        self.city = city

    def celsius_to_fahrenheit(self, celsius):
        """
        Converts a temperature from Celsius to Fahrenheit.

        Args:
            celsius (float): The temperature in Celsius.

        Returns:
            float: The temperature in Fahrenheit.

        Raises:
            TypeError: If celsius is not a number.
        """
        if not isinstance(celsius, (int, float)):
            raise TypeError("Celsius temperature must be a number")
        return celsius * 9 / 5 + 32

    def fahrenheit_to_celsius(self, fahrenheit):
        """
        Converts a temperature from Fahrenheit to Celsius.

        Args:
            fahrenheit (float): The temperature in Fahrenheit.

        Returns:
            float: The temperature in Celsius.

        Raises:
            TypeError: If fahrenheit is not a number.
        """
        if not isinstance(fahrenheit, (int, float)):
            raise TypeError("Fahrenheit temperature must be a number")
        return (fahrenheit - 32) * 5 / 9