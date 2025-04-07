import re


class PersonRequest:
    """
    This class validates input personal information data and sets invalid fields to None based to specific rules.
    """

    ALLOWED_SEXES = ["Man", "Woman", "UGM"]
    PHONE_NUMBER_LENGTH = 11
    MAX_NAME_LENGTH = 33

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

    def _validate_name(self, name: str) -> str | None:
        """
        Validate the name.

        If name is empty or exceeds MAX_NAME_LENGTH characters in length, return None.

        :param name: str, the name to validate
        :return: str | None, the validated name or None if invalid
        """
        name = name.strip()
        if not name or len(name) > self.MAX_NAME_LENGTH:
            return None
        return name

    def _validate_sex(self, sex: str) -> str | None:
        """
        Validate the sex.

        If sex is not in ALLOWED_SEXES, return None. Case-insensitive comparison is performed.

        :param sex: str, the sex to validate
        :return: str | None, the validated sex or None if invalid
        """
        if sex.strip() and sex.strip() in self.ALLOWED_SEXES:
            return sex.strip()
        return None

    def _validate_phone_number(self, phone_number: str) -> str | None:
        """
        Validate the phone number.

        If phone_number is empty, not a digit, or not PHONE_NUMBER_LENGTH digits long, return None.

        :param phone_number: str, the phone number to validate
        :return: str | None, the validated phone number or None if invalid
        """
        phone_number = phone_number.strip()
        if not phone_number:
            return None

        if not re.match(r"^[0-9]+$", phone_number) or len(phone_number) != self.PHONE_NUMBER_LENGTH:
            return None

        return phone_number