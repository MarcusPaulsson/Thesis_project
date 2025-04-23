class HRManagementSystem:
    """
    A personnel management system that implements functions such as adding, deleting, querying, and updating employees.
    """

    def __init__(self):
        """Initialize the HRManagementSystem with an empty dictionary for employees."""
        self.employees = {}

    def add_employee(self, employee_id: int, name: str, position: str, department: str, salary: int) -> bool:
        """
        Add a new employee to the HRManagementSystem.
        
        :param employee_id: The employee's id.
        :param name: The employee's name.
        :param position: The employee's position.
        :param department: The employee's department.
        :param salary: The employee's salary.
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
        
        :param employee_id: The employee's id.
        :return: True if the employee was removed, False if the employee does not exist.
        """
        return self.employees.pop(employee_id, None) is not None

    def update_employee(self, employee_id: int, employee_info: dict) -> bool:
        """
        Update an employee's information in the HRManagementSystem.
        
        :param employee_id: The employee's id.
        :param employee_info: A dictionary containing the employee's updated information.
        :return: True if the employee was updated, False if the employee does not exist.
        """
        if employee_id not in self.employees:
            return False
        self.employees[employee_id].update(employee_info)
        return True

    def get_employee(self, employee_id: int) -> dict:
        """
        Get an employee's information from the HRManagementSystem.
        
        :param employee_id: The employee's id.
        :return: The employee's information if found, otherwise None.
        """
        return self.employees.get(employee_id)

    def list_employees(self) -> dict:
        """
        List all employees' information in the HRManagementSystem.
        
        :return: A dictionary of all employees' information with their IDs.
        """
        return {emp_id: {**info, 'employee_ID': emp_id} for emp_id, info in self.employees.items()}