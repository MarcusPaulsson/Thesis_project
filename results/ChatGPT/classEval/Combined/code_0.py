import logging
import datetime

class AccessGatewayFilter:
    """
    A filter for gateway access, focused on authentication and access logging.
    """

    def __init__(self):
        self.allowed_methods = {'GET', 'POST'}
        self.valid_user_level = 3
        self.prefixes = {'/api', '/login'}

    def filter(self, request):
        """
        Filter the incoming request based on defined rules.
        :param request: dict, the incoming request details
        :return: bool or None, True if the request is allowed, False if denied, None if no user info
        """
        if not self.is_start_with(request['path']):
            return False
        
        if request['method'] not in self.allowed_methods:
            return False
        
        user = self.get_jwt_user(request)
        if user is None:
            return None
        
        self.set_current_user_info_and_log(user)
        return self.check_user_level(user)

    def is_start_with(self, request_uri):
        """
        Check if the request URI starts with any of the defined prefixes.
        :param request_uri: str, the URI of the request
        :return: bool, True if the URI starts with defined prefixes
        """
        return any(request_uri.startswith(prefix) for prefix in self.prefixes)

    def get_jwt_user(self, request):
        """
        Extract user information from the JWT token in the request.
        :param request: dict, the incoming request details
        :return: dict or None, user information if token is valid, None otherwise
        """
        auth_header = request.get('headers', {}).get('Authorization', {})
        user = auth_header.get('user')
        jwt_token = auth_header.get('jwt')

        if user and jwt_token and self.is_valid_jwt(jwt_token, user['name']):
            return user
        return None

    def is_valid_jwt(self, jwt, username):
        """
        Validate JWT against the username.
        :param jwt: str, the JWT token
        :param username: str, the username to validate against
        :return: bool, True if the JWT is valid
        """
        return jwt == f"{username}{datetime.date.today()}"

    def check_user_level(self, user):
        """
        Verify if the user's access level meets the required level.
        :param user: dict, the user information
        :return: bool, True if user level is sufficient
        """
        return user.get('level', 0) >= self.valid_user_level

    def set_current_user_info_and_log(self, user):
        """
        Log the access of the current user.
        :param user: dict, the user information
        """
        logging.info(f"User {user['name']} accessed the system from {user.get('address', 'unknown')}")