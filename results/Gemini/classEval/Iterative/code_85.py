import time

class Thermostat:
    """
    Manages temperature control, including setting and retrieving the target temperature,
    adjusting the mode, and simulating temperature operation.
    """

    VALID_MODES = ['heat', 'cool']

    def __init__(self, current_temperature, target_temperature, mode):
        """
        Initializes a Thermostat instance.

        :param current_temperature: The current temperature (float).
        :param target_temperature: The target temperature (float).
        :param mode: The operating mode ('heat' or 'cool').
        :raises ValueError: If the mode is invalid.
        """
        self.current_temperature = current_temperature
        self.target_temperature = target_temperature
        self.mode = self._validate_mode(mode)

    def _validate_mode(self, mode):
        """
        Validates the operating mode.

        :param mode: The operating mode (string).
        :return: The validated mode.
        :raises ValueError: If the mode is invalid.
        """
        if mode not in self.VALID_MODES:
            raise ValueError(f"Invalid mode: {mode}.  Must be one of {self.VALID_MODES}")
        return mode

    def get_target_temperature(self):
        """
        Gets the target temperature.

        :return: The target temperature (float).
        """
        return self.target_temperature

    def set_target_temperature(self, temperature):
        """
        Sets the target temperature.

        :param temperature: The target temperature (float).
        """
        self.target_temperature = temperature

    def get_mode(self):
        """
        Gets the current operating mode.

        :return: The operating mode (string).
        """
        return self.mode

    def set_mode(self, mode):
        """
        Sets the operating mode.

        :param mode: The operating mode ('heat' or 'cool').
        :raises ValueError: If the mode is invalid.
        """
        self.mode = self._validate_mode(mode)

    def auto_set_mode(self):
        """
        Automatically sets the operating mode based on the current and target temperatures.
        If the current temperature is lower than the target temperature, the mode is set to 'heat',
        otherwise, it's set to 'cool'.
        """
        if self.current_temperature < self.target_temperature:
            self.mode = 'heat'
        else:
            self.mode = 'cool'

    def auto_check_conflict(self):
        """
        Checks for conflicts between the operating mode and the temperature relationship.
        If a conflict exists, the operating mode is adjusted automatically.

        :return: True if there is no conflict, False otherwise.
        """
        if self.mode == 'heat' and self.current_temperature >= self.target_temperature:
            self.mode = 'cool'
            return False
        elif self.mode == 'cool' and self.current_temperature <= self.target_temperature:
            self.mode = 'heat'
            return False
        else:
            return True

    def simulate_operation(self, temperature_change_rate=1.0, check_interval=0.1):
        """
        Simulates the operation of the thermostat, adjusting the current temperature
        until it reaches the target temperature.

        :param temperature_change_rate: The amount the temperature changes per interval (default: 1.0).
        :param check_interval: The time interval between temperature adjustments (default: 0.1).
        :return: The time it took to complete the simulation (integer seconds).
        """
        start_time = time.time()
        self.auto_set_mode()

        while abs(self.current_temperature - self.target_temperature) > 0.1:
            if self.mode == 'heat':
                self.current_temperature += temperature_change_rate * check_interval
            else:
                self.current_temperature -= temperature_change_rate * check_interval

            self.auto_check_conflict()
            time.sleep(check_interval)

        end_time = time.time()
        return int(end_time - start_time)