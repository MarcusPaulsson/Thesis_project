class HRManagementSystem:
    """
    This is a class as personnel management system that implements functions such as adding, deleting, querying, and updating employees
    """

    def __init__(self):
        """
        Initialize the HRManagementSystem with an attribute employees, which is an empty dictionary.
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
        :return: True if the employee is added successfully, False otherwise.
        """
        if not isinstance(employee_id, int):
            raise TypeError("Employee ID must be an integer.")
        if not isinstance(name, str) or not name:
            raise ValueError("Employee name must be a non-empty string.")
        if not isinstance(position, str) or not position:
            raise ValueError("Employee position must be a non-empty string.")
        if not isinstance(department, str) or not department:
            raise ValueError("Employee department must be a non-empty string.")
        if not isinstance(salary, (int, float)) or salary <= 0:
            raise ValueError("Employee salary must be a positive number.")

        if employee_id in self.employees:
            return False
        else:
            self.employees[employee_id] = {
                'name': name,
                'position': position,
                'department': department,
                'salary': salary
            }
            return True

    def remove_employee(self, employee_id):
        """
        Remove an employee from the HRManagementSystem.
        :param employee_id: The employee's id, int.
        :return: True if the employee is removed successfully, False otherwise.
        """
        if not isinstance(employee_id, int):
            raise TypeError("Employee ID must be an integer.")

        if employee_id in self.employees:
            del self.employees[employee_id]
            return True
        else:
            return False

    def update_employee(self, employee_id: int, employee_info: dict):
        """
        Update an employee's information in the HRManagementSystem.
        :param employee_id: The employee's id, int.
        :param employee_info: A dictionary containing the employee's information to update.
        :return: True if the employee is updated successfully, False otherwise.
        """
        if not isinstance(employee_id, int):
            raise TypeError("Employee ID must be an integer.")
        if not isinstance(employee_info, dict):
            raise TypeError("Employee info must be a dictionary.")

        if employee_id in self.employees:
            # Validate employee_info (example)
            if 'salary' in employee_info and not isinstance(employee_info['salary'], (int, float)):
                raise ValueError("Salary must be a number.")

            self.employees[employee_id].update(employee_info)
            return True
        else:
            return False

    def get_employee(self, employee_id):
        """
        Get an employee's information from the HRManagementSystem.
        :param employee_id: The employee's id, int.
        :return: A dictionary containing the employee's information if found, False otherwise.
        """
        if not isinstance(employee_id, int):
            raise TypeError("Employee ID must be an integer.")

        if employee_id in self.employees:
            return self.employees[employee_id]
        else:
            return False

    def list_employees(self):
        """
        List all employees' information in the HRManagementSystem.
        :return: A dictionary where keys are employee IDs and values are employee information dictionaries.
        """
        return self.employees