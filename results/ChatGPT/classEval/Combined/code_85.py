import time

class Thermostat:
    """
    The class manages temperature control, including setting and retrieving the target temperature, adjusting the mode, and simulating temperature operation.
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
        self.set_mode(mode)

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
        """Automatically set the operating mode based on current and target temperatures."""
        self.mode = 'heat' if self.current_temperature < self.target_temperature else 'cool'

    def auto_check_conflict(self) -> bool:
        """
        Check for conflicts between the operating mode and temperature relationship.
        Adjust mode if there is a conflict.
        :return: True if no conflict, False otherwise.
        """
        conflict = (self.current_temperature < self.target_temperature and self.mode == 'cool') or \
                   (self.current_temperature > self.target_temperature and self.mode == 'heat')
        if conflict:
            self.auto_set_mode()
            return False
        return True

    def simulate_operation(self) -> int:
        """Simulate the operation of the thermostat until the target temperature is reached."""
        self.auto_set_mode()
        time_taken = 0
        step = 0.1 if self.mode == 'heat' else -0.1

        while abs(self.current_temperature - self.target_temperature) > 0.1:
            self.current_temperature += step
            time.sleep(0.1)  # Simulate time delay for each adjustment
            time_taken += 1

        return time_taken