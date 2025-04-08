class HRManagementSystem:
    """
    A personnel management system that implements functions such as adding, deleting, querying, and updating employees.
    """

    def __init__(self):
        """
        Initializes the HRManagementSystem with an empty dictionary to store employees.
        """
        self.employees = {}

    def add_employee(self, employee_id, name, position, department, salary):
        """
        Adds a new employee to the HRManagementSystem.

        Args:
            employee_id (int): The unique identifier for the employee.
            name (str): The employee's name.
            position (str): The employee's job title.
            department (str): The department the employee belongs to.
            salary (int): The employee's salary.

        Returns:
            bool: True if the employee was added successfully, False if an employee with the same ID already exists.
        """
        if not isinstance(employee_id, int):
            raise TypeError("Employee ID must be an integer.")

        if employee_id in self.employees:
            return False

        self.employees[employee_id] = {
            'name': name,
            'position': position,
            'department': department,
            'salary': salary
        }
        return True

    def remove_employee(self, employee_id):
        """
        Removes an employee from the HRManagementSystem.

        Args:
            employee_id (int): The ID of the employee to remove.

        Returns:
            bool: True if the employee was removed successfully, False if the employee ID was not found.
        """
        if not isinstance(employee_id, int):
            raise TypeError("Employee ID must be an integer.")

        if employee_id in self.employees:
            del self.employees[employee_id]
            return True
        return False

    def update_employee(self, employee_id, employee_info):
        """
        Updates an employee's information in the HRManagementSystem.

        Args:
            employee_id (int): The ID of the employee to update.
            employee_info (dict): A dictionary containing the employee information to update.
                                   Keys should correspond to the employee attributes (e.g., 'name', 'salary').

        Returns:
            bool: True if the employee was updated successfully, False if the employee ID was not found or
                  if the provided keys are invalid.
        """
        if not isinstance(employee_id, int):
            raise TypeError("Employee ID must be an integer.")

        if not isinstance(employee_info, dict):
            raise TypeError("Employee info must be a dictionary.")

        if employee_id not in self.employees:
            return False

        for key, value in employee_info.items():
            if key in self.employees[employee_id]:
                self.employees[employee_id][key] = value
            else:
                return False  # Invalid key

        return True

    def get_employee(self, employee_id):
        """
        Retrieves an employee's information from the HRManagementSystem.

        Args:
            employee_id (int): The ID of the employee to retrieve.

        Returns:
            dict: A dictionary containing the employee's information if found, False otherwise.
        """
        if not isinstance(employee_id, int):
            raise TypeError("Employee ID must be an integer.")

        if employee_id in self.employees:
            return self.employees[employee_id]
        return False

    def list_employees(self):
        """
        Lists all employees' information in the HRManagementSystem.

        Returns:
            dict: A dictionary where keys are employee IDs and values are dictionaries containing employee information,
                  including the employee ID itself under the key 'employee_ID'. Returns empty dict if there are no employees.
        """
        employee_list = {}
        for employee_id, employee_info in self.employees.items():
            employee_list[employee_id] = {'employee_ID': employee_id, **employee_info}
        return employee_list