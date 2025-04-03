import time

class Thermostat:
    """
    The class manages temperature control, including setting and retrieving the target temperature, adjusting the mode, and simulating temperature operation.
    """

    def __init__(self, current_temperature, target_temperature, mode):
        """
        Initialize instances of the Thermostat class, including the current temperature, target temperature, and operating mode.
        :param current_temperature: float
        :param target_temperature: float
        :param mode: str, the work mode
        """
        self.current_temperature = current_temperature
        self.target_temperature = target_temperature
        self.mode = mode

    def get_target_temperature(self):
        """
        Get the target temperature of an instance of the Thermostat class.
        :return: float
        """
        return self.target_temperature

    def set_target_temperature(self, temperature):
        """
        Set the target temperature.
        :param temperature: float, the target temperature
        """
        self.target_temperature = temperature

    def get_mode(self):
        """
        Get the current work mode.
        :return: str, working mode. only ['heat', 'cool']
        """
        return self.mode

    def set_mode(self, mode):
        """
        Set the current work mode.
        :param mode: str, working mode. only ['heat', 'cool']
        """
        if mode in ['heat', 'cool']:
            self.mode = mode
        else:
            raise ValueError("Mode must be 'heat' or 'cool'.")

    def auto_set_mode(self):
        """
        Automatically set the operating mode based on the current and target temperature.
        """
        if self.current_temperature < self.target_temperature:
            self.mode = 'heat'
        else:
            self.mode = 'cool'

    def auto_check_conflict(self):
        """
        Check if there is a conflict between the operating mode and the temperatures.
        :return: bool, True if mode isn't in conflict; False otherwise.
        """
        conflict = (self.mode == 'heat' and self.current_temperature >= self.target_temperature) or \
                   (self.mode == 'cool' and self.current_temperature <= self.target_temperature)
        if conflict:
            self.auto_set_mode()
        return not conflict

    def simulate_operation(self):
        """
        Simulate the operation of the Thermostat.
        :return: int, the time it took to complete the simulation.
        """
        self.auto_set_mode()
        start_time = time.time()

        while abs(self.current_temperature - self.target_temperature) > 0.1:
            if self.mode == 'heat':
                self.current_temperature += 0.1
            else:
                self.current_temperature -= 0.1
            time.sleep(0.1)  # Simulate time delay for heating/cooling

        return int(time.time() - start_time)