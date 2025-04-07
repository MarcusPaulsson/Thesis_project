import logging
import datetime

class AccessGatewayFilter:
    """
    This class is a filter used for accessing gateway filtering, primarily for authentication and access log recording.
    """

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        # You can configure the logger here if needed

    def filter(self, request):
        """
        Filter the incoming request based on certain rules and conditions.
        :param request: dict, the incoming request details
        :return: bool, True if the request is allowed, False otherwise
        """
        if self.is_start_with(request.get('path', '')):
            return True

        auth_header = request.get('headers', {}).get('Authorization')
        if auth_header:
            user = auth_header.get('user')
            jwt_token = auth_header.get('jwt')
            if user and jwt_token:
                expected_jwt = user['name'] + str(datetime.date.today())
                if jwt_token == expected_jwt:
                    if user.get('level') and user['level'] > 3:
                        self.set_current_user_info_and_log(user)
                        return True
                    elif user.get('level') and user['level'] == 1:
                        return None
                    else:
                        self.set_current_user_info_and_log(user)
                        return True
                else:
                    # Check if JWT is valid for a different user
                    try:
                        user_name = jwt_token[:jwt_token.index(str(datetime.date.today()))]
                    except ValueError:
                        return True
                    return True
        return True


    def is_start_with(self, request_uri):
        """
        Check if the request URI starts with certain prefixes.
        Currently, the prefixes being checked are "/api" and "/login".
        :param request_uri: str, the URI of the request
        :return: bool, True if the URI starts with certain prefixes, False otherwise
        """
        return request_uri.startswith('/api') or request_uri.startswith('/login')

    def get_jwt_user(self, request):
        """
        Get the user information from the JWT token in the request.
        :param request: dict, the incoming request details
        :return: dict or None, the user information if the token is valid, None otherwise
        """
        auth_header = request.get('headers', {}).get('Authorization')
        if auth_header:
            user = auth_header.get('user')
            jwt_token = auth_header.get('jwt')
            if user and jwt_token:
                expected_jwt = user['name'] + str(datetime.date.today())
                if jwt_token == expected_jwt:
                    return user
                else:
                    return None
        return None

    def set_current_user_info_and_log(self, user):
        """
        Set the current user information and log the access.
        :param user: dict, the user information
        :return: None
        """
        # In a real application, you would set the user information
        # in a thread-local storage or similar mechanism.
        # For this example, we'll just log the information.
        self.logger.info(f"User accessed: {user}")