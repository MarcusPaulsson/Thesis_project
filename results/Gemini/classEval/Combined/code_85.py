class Thermostat:
    """
    Manages temperature control, including setting and retrieving the target temperature,
    adjusting the mode, and simulating temperature operation.
    """

    VALID_MODES = ['heat', 'cool']

    def __init__(self, current_temperature, target_temperature, mode):
        """
        Initializes a Thermostat instance.

        Args:
            current_temperature (float): The current temperature.
            target_temperature (float): The desired target temperature.
            mode (str): The operating mode ('heat' or 'cool').
        Raises:
            ValueError: If the mode is invalid.
        """
        self.current_temperature = current_temperature
        self.target_temperature = target_temperature
        if mode not in self.VALID_MODES:
            raise ValueError(f"Invalid mode: {mode}.  Must be one of {self.VALID_MODES}")
        self.mode = mode

    def get_target_temperature(self):
        """
        Returns the target temperature.

        Returns:
            float: The target temperature.
        """
        return self.target_temperature

    def set_target_temperature(self, temperature):
        """
        Sets the target temperature.

        Args:
            temperature (float): The new target temperature.
        """
        self.target_temperature = temperature

    def get_mode(self):
        """
        Returns the current operating mode.

        Returns:
            str: The current operating mode ('heat' or 'cool').
        """
        return self.mode

    def set_mode(self, mode):
        """
        Sets the operating mode.

        Args:
            mode (str): The new operating mode ('heat' or 'cool').

        Returns:
            bool: True if the mode was successfully set, False otherwise.
        """
        if mode in self.VALID_MODES:
            self.mode = mode
            return True
        return False

    def auto_set_mode(self):
        """
        Automatically sets the operating mode based on the current and target temperatures.
        If the current temperature is lower than the target, the mode is set to 'heat', otherwise 'cool'.
        """
        if self.current_temperature < self.target_temperature:
            self.mode = 'heat'
        else:
            self.mode = 'cool'

    def auto_check_conflict(self):
        """
        Checks for and resolves conflicts between the operating mode and the temperature difference.
        If a conflict exists, the mode is adjusted.

        Returns:
            bool: True if no conflict exists after the check, False otherwise (and the mode was adjusted).
        """
        if self.mode == 'heat' and self.current_temperature > self.target_temperature:
            self.mode = 'cool'
            return False
        elif self.mode == 'cool' and self.current_temperature < self.target_temperature:
            self.mode = 'heat'
            return False
        else:
            return True

    def simulate_operation(self):
        """
        Simulates the thermostat operation, adjusting the current temperature until it reaches the target.

        Returns:
            int: The number of iterations it took to reach the target temperature.
        """
        iterations = 0
        self.auto_set_mode()

        while abs(self.current_temperature - self.target_temperature) > 0.5:
            if self.mode == 'heat':
                self.current_temperature += 1
            else:
                self.current_temperature -= 1
            iterations += 1

        # Ensure current_temperature is exactly target_temperature after simulation
        self.current_temperature = self.target_temperature

        return iterations