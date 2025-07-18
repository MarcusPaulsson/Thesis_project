class PersonRequest:
    """
    This class validates input personal information data and sets invalid fields to None based on specific rules.
    """

    VALID_SEXES = {"Man", "Woman", "UGM"}

    def __init__(self, name: str, sex: str, phone_number: str):
        """
        Initialize PersonRequest object with the provided information.
        :param name: str, the name of the person
        :param sex: str, the sex of the person
        :param phone_number: str, the phone number of the person
        """
        self.name = self._validate_name(name)
        self.sex = self._validate_sex(sex)
        self.phone_number = self._validate_phone_number(phone_number)

    def _validate_name(self, name: str) -> str:
        """
        Validate the name and return it. If name is empty or exceeds 33 characters in length, set to None.
        :param name: str, the name to validate
        :return: str, the validated name or None if invalid
        """
        return name if name and len(name) <= 33 else None

    def _validate_sex(self, sex: str) -> str:
        """
        Validate the sex and return it. If sex is not Man, Woman, or UGM, set to None.
        :param sex: str, the sex to validate
        :return: str, the validated sex or None if invalid
        """
        return sex if sex in self.VALID_SEXES else None

    def _validate_phone_number(self, phone_number: str) -> str:
        """
        Validate the phone number and return it. If phone_number is empty or not an 11 digit number, set to None.
        :param phone_number: str, the phone number to validate
        :return: str, the validated phone number or None if invalid
        """
        return phone_number if phone_number.isdigit() and len(phone_number) == 11 else None