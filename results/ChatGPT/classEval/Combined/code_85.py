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
        :param mode: str, the work mode
        """
        self.current_temperature = current_temperature
        self.target_temperature = target_temperature
        self.mode = mode if mode in self.VALID_MODES else 'cool'

    def get_target_temperature(self) -> float:
        """Return the target temperature."""
        return self.target_temperature

    def set_target_temperature(self, temperature: float) -> None:
        """Set the target temperature."""
        self.target_temperature = temperature

    def get_mode(self) -> str:
        """Return the current work mode."""
        return self.mode

    def set_mode(self, mode: str) -> bool:
        """Set the current work mode if valid."""
        if mode in self.VALID_MODES:
            self.mode = mode
            return True
        return False

    def auto_set_mode(self) -> None:
        """Automatically set the operating mode based on current and target temperature."""
        self.mode = 'heat' if self.current_temperature < self.target_temperature else 'cool'

    def auto_check_conflict(self) -> bool:
        """
        Check if there is a conflict between the operating mode and the relationship
        between the current temperature and the target temperature.
        :return: True if mode is consistent with temperature, False otherwise.
        """
        if (self.current_temperature < self.target_temperature and self.mode == 'cool') or \
           (self.current_temperature > self.target_temperature and self.mode == 'heat'):
            self.auto_set_mode()
            return False
        return True

    def simulate_operation(self) -> int:
        """Simulate the operation of the Thermostat."""
        self.auto_set_mode()
        time_taken = 0
        
        while self.current_temperature != self.target_temperature:
            if self.mode == 'heat':
                self.current_temperature += 1
            elif self.mode == 'cool':
                self.current_temperature -= 1
            
            time_taken += 1
            
            # Simulate some delay (optional)
            time.sleep(0.1)

            # Prevent overshooting
            if (self.mode == 'heat' and self.current_temperature > self.target_temperature) or \
               (self.mode == 'cool' and self.current_temperature < self.target_temperature):
                self.current_temperature = self.target_temperature
            
        return time_taken