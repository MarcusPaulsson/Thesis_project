import logging
import datetime

class AccessGatewayFilter:
    """
    This class is a filter used for accessing gateway filtering, primarily for authentication and access log recording.
    """

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.access_level = 3

    def filter(self, request):
        """
        Filter the incoming request based on certain rules and conditions.
        :param request: dict, the incoming request details
        :return: bool, True if the request is allowed, False otherwise
        """
        path = request.get('path')
        if self.is_start_with(path):
            return True

        auth_header = request.get('headers', {}).get('Authorization')
        if auth_header:
            user = auth_header.get('user')
            jwt_token = auth_header.get('jwt')

            if user and jwt_token:
                jwt_user = self.get_jwt_user(request)
                if jwt_user:
                    user_level = user.get('level')
                    if user_level is not None:
                        if user_level > self.access_level:
                            return True
                        elif user_level == self.access_level:
                            return True
                        else:
                            return None
                    else:
                        return True
                else:
                    return True
            else:
                return True
        return False

    def is_start_with(self, request_uri):
        """
        Check if the request URI starts with certain prefixes.
        Currently, the prefixes being checked are "/api" and "/login".
        :param request_uri: str, the URI of the request
        :return: bool, True if the URI starts with certain prefixes, False otherwise
        """
        if not request_uri:
            return False
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
        return None

    def set_current_user_info_and_log(self, user):
        """
        Set the current user information and log the access.
        :param user: dict, the user information
        :return: None
        """
        if user:
            user_name = user.get('name', 'Unknown')
            user_address = user.get('address', 'Unknown')
            log_message = f"User '{user_name}' from address '{user_address}' accessed the gateway."
            self.logger.info(log_message)
        else:
            self.logger.warning("Attempted to set user info and log with empty user data.")