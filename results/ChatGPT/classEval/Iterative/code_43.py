class HRManagementSystem:
    """
    This is a class representing a personnel management system that implements functions such as adding, deleting, querying, and updating employees.
    """

    def __init__(self):
        """
        Initialize the HRManagementSystem with an attribute employees, which is an empty dictionary.
        """
        self.employees = {}

    def add_employee(self, employee_id: int, name: str, position: str, department: str, salary: int) -> bool:
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
        self.employees[employee_id] = {
            'name': name,
            'position': position,
            'department': department,
            'salary': salary
        }
        return True

    def remove_employee(self, employee_id: int) -> bool:
        """
        Remove an employee from the HRManagementSystem.
        :param employee_id: The employee's id, int.
        :return: If the employee is already in the HRManagementSystem, returns True, otherwise, returns False.
        """
        return self.employees.pop(employee_id, None) is not None

    def update_employee(self, employee_id: int, employee_info: dict) -> bool:
        """
        Update an employee's information in the HRManagementSystem.
        :param employee_id: The employee's id, int.
        :param employee_info: The employee's information, dict.
        :return: If the employee is already in the HRManagementSystem, returns True, otherwise, returns False.
        """
        if employee_id not in self.employees:
            return False
        self.employees[employee_id].update(employee_info)
        return True

    def get_employee(self, employee_id: int):
        """
        Get an employee's information from the HRManagementSystem.
        :param employee_id: The employee's id, int.
        :return: If the employee is already in the HRManagementSystem, returns the employee's information, otherwise, returns None.
        """
        return self.employees.get(employee_id)

    def list_employees(self) -> dict:
        """
        List all employees' information in the HRManagementSystem.
        :return: A dictionary of all employees' information, including their IDs.
        """
        return {employee_id: {**{'employee_ID': employee_id}, **info} for employee_id, info in self.employees.items()}