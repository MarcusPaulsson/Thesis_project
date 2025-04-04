import time

class Thermostat:
    """
    The class manages temperature control, including setting and retrieving the target temperature, adjusting the mode, and simulating temperature operation.
    """

    def __init__(self, current_temperature: float, target_temperature: float, mode: str):
        """
        Initialize instances of the Thermostat class, including the current temperature, target temperature, and operating mode.
        :param current_temperature: float
        :param target_temperature: float
        :param mode: str, the work mode ('heat' or 'cool')
        """
        self.current_temperature = current_temperature
        self.target_temperature = target_temperature
        self.mode = mode

    def get_target_temperature(self) -> float:
        """Get the target temperature of the thermostat."""
        return self.target_temperature

    def set_target_temperature(self, temperature: float):
        """Set the target temperature."""
        self.target_temperature = temperature

    def get_mode(self) -> str:
        """Get the current operating mode."""
        return self.mode

    def set_mode(self, mode: str):
        """Set the operating mode."""
        if mode in ['heat', 'cool']:
            self.mode = mode
        else:
            raise ValueError("Mode must be 'heat' or 'cool'.")

    def auto_set_mode(self):
        """Automatically set the operating mode based on the current and target temperatures."""
        if self.current_temperature < self.target_temperature:
            self.set_mode('heat')
        else:
            self.set_mode('cool')

    def auto_check_conflict(self) -> bool:
        """
        Check for conflicts between the operating mode and temperature relationship.
        Adjusts mode if there is a conflict.
        :return: True if there is no conflict, False otherwise.
        """
        if (self.current_temperature < self.target_temperature and self.mode == 'cool') or \
           (self.current_temperature > self.target_temperature and self.mode == 'heat'):
            self.auto_set_mode()
            return False
        return True

    def simulate_operation(self) -> int:
        """
        Simulate the operation of the thermostat, adjusting the current temperature until the target is reached.
        :return: int, the time it took to complete the simulation in seconds.
        """
        self.auto_set_mode()
        start_time = time.time()
        
        while abs(self.current_temperature - self.target_temperature) > 0.1:
            adjustment = 0.1 if self.mode == 'heat' else -0.1
            self.current_temperature += adjustment
            time.sleep(1)  # Simulate time passing
        
        return int(time.time() - start_time)