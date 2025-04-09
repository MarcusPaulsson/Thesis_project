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
        Get the target temperature.
        :return: float
        """
        return self.target_temperature

    def set_target_temperature(self, temperature):
        """
        Set the target temperature.
        :param temperature: float
        """
        self.target_temperature = temperature

    def get_mode(self):
        """
        Get the current work mode.
        :return: str
        """
        return self.mode

    def set_mode(self, mode):
        """
        Set the work mode.
        :param mode: str, working mode. only ['heat', 'cool']
        :return: bool
        """
        if mode in ['heat', 'cool']:
            self.mode = mode
            return True
        else:
            return False

    def auto_set_mode(self):
        """
        Automatically set the operating mode based on current and target temperatures.
        """
        if self.current_temperature < self.target_temperature:
            self.mode = 'heat'
        else:
            self.mode = 'cool'

    def auto_check_conflict(self):
        """
        Check for conflicts between the operating mode and temperature relationship.
        Adjust the mode if a conflict exists.
        :return: bool
        """
        if self.mode == 'heat' and self.current_temperature >= self.target_temperature:
            self.mode = 'cool'
            return False
        elif self.mode == 'cool' and self.current_temperature < self.target_temperature:
            self.mode = 'heat'
            return False
        else:
            return True

    def simulate_operation(self):
        """
        Simulate thermostat operation until the target temperature is reached.
        :return: int, the time taken for the simulation in hundredths of a second.
        """
        self.auto_set_mode()
        start_time = time.time()
        while abs(self.current_temperature - self.target_temperature) > 0.1:
            if self.mode == 'heat':
                self.current_temperature += 0.5
            else:
                self.current_temperature -= 0.5
            time.sleep(0.01)
        end_time = time.time()
        return int((end_time - start_time) * 100)