class HRManagementSystem:
    """
    A personnel management system that implements functions such as adding, deleting, querying, and updating employees.
    """

    def __init__(self):
        """Initialize the HRManagementSystem with an empty employee dictionary."""
        self.employees = {}

    def add_employee(self, employee_id: int, name: str, position: str, department: str, salary: int) -> bool:
        """
        Add a new employee to the HRManagementSystem.
        :param employee_id: The employee's id, int.
        :param name: The employee's name, str.
        :param position: The employee's position, str.
        :param department: The employee's department, str.
        :param salary: The employee's salary, int.
        :return: True if the employee was added, False if the employee already exists.
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
        :return: True if the employee was removed, False if the employee does not exist.
        """
        return self.employees.pop(employee_id, None) is not None

    def update_employee(self, employee_id: int, employee_info: dict) -> bool:
        """
        Update an employee's information in the HRManagementSystem.
        :param employee_id: The employee's id, int.
        :param employee_info: A dictionary containing the updated employee information.
        :return: True if the employee was updated, False if the employee does not exist.
        """
        if employee_id not in self.employees:
            return False
        self.employees[employee_id].update(employee_info)
        return True

    def get_employee(self, employee_id: int) -> dict:
        """
        Get an employee's information from the HRManagementSystem.
        :param employee_id: The employee's id, int.
        :return: The employee's information if found, otherwise None.
        """
        return self.employees.get(employee_id)

    def list_employees(self) -> dict:
        """
        List all employees' information in the HRManagementSystem.
        :return: A dictionary of all employees' information, with each employee ID included.
        """
        return {
            employee_id: {**info, 'employee_ID': employee_id}
            for employee_id, info in self.employees.items()
        }