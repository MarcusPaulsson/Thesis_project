import logging
import datetime

class AccessGatewayFilter:
    """
    This class is a filter used for accessing gateway filtering, primarily for authentication and access log recording.
    """

    def __init__(self):
        self.allowed_methods = {'GET', 'POST'}
        self.valid_prefixes = ['/api', '/login']

    def filter(self, request):
        """
        Filter the incoming request based on certain rules and conditions.
        :param request: dict, the incoming request details
        :return: bool or None, True if the request is allowed, False if denied, None if user level is insufficient
        """
        if not self._is_start_with(request['path']):
            return False

        if request['method'] not in self.allowed_methods:
            return False

        user = self._get_jwt_user(request)
        if user is None:
            return False

        if user.get('level', 0) < 3:
            return None

        self._set_current_user_info_and_log(user)
        return True

    def _is_start_with(self, request_uri):
        """
        Check if the request URI starts with certain prefixes.
        :param request_uri: str, the URI of the request
        :return: bool, True if the URI starts with certain prefixes, False otherwise
        """
        return any(request_uri.startswith(prefix) for prefix in self.valid_prefixes)

    def _get_jwt_user(self, request):
        """
        Get the user information from the JWT token in the request.
        :param request: dict, the incoming request details
        :return: dict or None, the user information if the token is valid, None otherwise
        """
        auth_header = request.get('headers', {}).get('Authorization', {})
        user_info = auth_header.get('user')
        jwt_token = auth_header.get('jwt')

        if user_info and self._is_jwt_valid(jwt_token, user_info['name']):
            return user_info
        return None

    def _is_jwt_valid(self, jwt_token, username):
        """
        Validate the JWT token.
        :param jwt_token: str, the JWT token
        :param username: str, the username to validate against
        :return: bool, True if the JWT is valid, False otherwise
        """
        expected_token = f"{username}{datetime.date.today()}"
        return jwt_token == expected_token

    def _set_current_user_info_and_log(self, user):
        """
        Set the current user information and log the access.
        :param user: dict, the user information
        :return: None
        """
        logging.info(f"User accessed: {user['name']} from {user.get('address', 'unknown')}")