class HRManagementSystem:
    """
    This is a class as personnel management system that implements functions such as adding, deleting, querying, and updating employees
    """

    def __init__(self):
        """
        Initialize the HRManagementSystem withan attribute employees, which is an empty dictionary.
        """
        self.employees = {}

    def add_employee(self, employee_id, name, position, department, salary):
        """
        Add a new employee to the HRManagementSystem.
        :param employee_id: The employee's id, int.
        :param name: The employee's name, str.
        :param position: The employee's position, str.
        :param department: The employee's department, str.
        :param salary: The employee's salary, int.
        :return: If the employee is already in the HRManagementSystem, returns False, otherwise, returns True.

        """
        if employee_id in self.employees:
            return False
        else:
            self.employees[employee_id] = {'name': name, 'position': position, 'department': department, 'salary': salary}
            return True

    def remove_employee(self, employee_id):
        """
        Remove an employee from the HRManagementSystem.
        :param employee_id: The employee's id, int.
        :return: If the employee is already in the HRManagementSystem, returns True, otherwise, returns False.

        """
        if employee_id in self.employees:
            del self.employees[employee_id]
            return True
        else:
            return False

    def update_employee(self, employee_id: int, employee_info: dict):
        """
        Update an employee's information in the HRManagementSystem.
        :param employee_id: The employee's id, int.
        :param employee_info: The employee's information, dict.
        :return: If the employee is already in the HRManagementSystem, returns True, otherwise, returns False.

        """
        if employee_id in self.employees:
            valid_keys = {'name', 'position', 'department', 'salary'}
            for key in employee_info:
                if key.lower() not in valid_keys:
                    return False
            self.employees[employee_id].update(employee_info)
            return True
        else:
            return False

    def get_employee(self, employee_id):
        """
        Get an employee's information from the HRManagementSystem.
        :param employee_id: The employee's id, int.
        :return: If the employee is already in the HRManagementSystem, returns the employee's information, otherwise, returns False.

        """
        if employee_id in self.employees:
            return self.employees[employee_id]
        else:
            return False

    def list_employees(self):
        """
        List all employees' information in the HRManagementSystem.
        :return: A list of all employees' information,dict.

        """
        employee_list = {}
        for employee_id, employee_info in self.employees.items():
            employee_list[employee_id] = {'employee_ID': employee_id, **employee_info}
        return employee_list