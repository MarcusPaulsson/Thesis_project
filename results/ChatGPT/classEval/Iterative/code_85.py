import time

class Thermostat:
    """
    The class manages temperature control, including setting and retrieving the target temperature,
    adjusting the mode, and simulating temperature operation.
    """

    VALID_MODES = {'heat', 'cool'}

    def __init__(self, current_temperature: float, target_temperature: float, mode: str):
        """
        Initialize instances of the Thermostat class.
        :param current_temperature: float
        :param target_temperature: float
        :param mode: str, the working mode
        """
        self.current_temperature = current_temperature
        self.target_temperature = target_temperature
        self.mode = mode if mode in self.VALID_MODES else 'cool'  # Default to 'cool' if invalid mode

    def get_target_temperature(self) -> float:
        """Get the target temperature."""
        return self.target_temperature

    def set_target_temperature(self, temperature: float) -> None:
        """Set the target temperature."""
        self.target_temperature = temperature

    def get_mode(self) -> str:
        """Get the current working mode."""
        return self.mode

    def set_mode(self, mode: str) -> None:
        """Set the current working mode."""
        if mode in self.VALID_MODES:
            self.mode = mode

    def auto_set_mode(self) -> None:
        """Automatically set the operating mode based on temperature comparison."""
        self.mode = 'heat' if self.current_temperature < self.target_temperature else 'cool'

    def auto_check_conflict(self) -> bool:
        """
        Check for conflicts between the current mode and temperatures.
        Return True if there's no conflict, False otherwise.
        """
        conflict = (self.current_temperature < self.target_temperature and self.mode == 'cool') or \
                   (self.current_temperature > self.target_temperature and self.mode == 'heat')

        if conflict:
            self.auto_set_mode()
        return not conflict

    def simulate_operation(self) -> int:
        """Simulate the thermostat operation until the target temperature is reached."""
        self.auto_set_mode()
        start_time = time.time()

        while abs(self.current_temperature - self.target_temperature) > 0.01:  # Allow for small precision
            if self.mode == 'heat':
                self.current_temperature += 1  # Simulating heating
            else:
                self.current_temperature -= 1  # Simulating cooling

            time.sleep(0.1)  # Simulate time delay

            # Check for conflicts and auto-adjust if necessary
            self.auto_check_conflict()

        return int(time.time() - start_time)