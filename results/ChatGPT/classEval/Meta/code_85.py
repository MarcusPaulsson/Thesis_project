import time

class Thermostat:
    def __init__(self, current_temperature, target_temperature, mode):
        self.current_temperature = current_temperature
        self.target_temperature = target_temperature
        self.mode = mode

    def get_target_temperature(self):
        return self.target_temperature

    def set_target_temperature(self, temperature):
        self.target_temperature = temperature

    def get_mode(self):
        return self.mode

    def set_mode(self, mode):
        if mode in ['heat', 'cool']:
            self.mode = mode
        else:
            return False

    def auto_set_mode(self):
        if self.current_temperature < self.target_temperature:
            self.mode = 'heat'
        else:
            self.mode = 'cool'

    def auto_check_conflict(self):
        if (self.current_temperature < self.target_temperature and self.mode == 'cool') or \
           (self.current_temperature > self.target_temperature and self.mode == 'heat'):
            self.auto_set_mode()
            return False
        return True

    def simulate_operation(self):
        self.auto_set_mode()
        time_taken = 0
        if self.mode == 'heat':
            while self.current_temperature < self.target_temperature:
                self.current_temperature += 1
                time_taken += 1
                time.sleep(0.1)  # Simulating time delay for heating
        elif self.mode == 'cool':
            while self.current_temperature > self.target_temperature:
                self.current_temperature -= 1
                time_taken += 1
                time.sleep(0.1)  # Simulating time delay for cooling
        return time_taken