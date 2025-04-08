import logging
import datetime

class AccessGatewayFilter:
    """
    This class is a filter used for accessing gateway filtering, primarily for authentication and access log recording.
    """

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

    def filter(self, request):
        """
        Filter the incoming request based on certain rules and conditions.
        :param request: dict, the incoming request details
        :return: bool, True if the request is allowed, False otherwise
        """
        if not isinstance(request, dict):
            self.logger.warning("Invalid request format. Expected a dictionary.")
            return False

        path = request.get('path', '')
        headers = request.get('headers', {})
        auth_header = headers.get('Authorization', None)

        if self.is_start_with(path):
            return True

        if auth_header:
            user_data = auth_header.get('user')
            jwt = auth_header.get('jwt')

            if user_data and jwt:
                user = self.get_jwt_user(request)
                if user:
                    user_level = user_data.get('level', None)
                    if user_level is not None:
                        if user_level > 3:
                            return True
                        elif user_level == 3:
                            return True
                        else:
                            return None
                    else:
                         return None
                else:
                    return False
            else:
                return False

        return True


    def is_start_with(self, request_uri):
        """
        Check if the request URI starts with certain prefixes.
        Currently, the prefixes being checked are "/api" and "/login".
        :param request_uri: str, the URI of the request
        :return: bool, True if the URI starts with certain prefixes, False otherwise
        """
        if not isinstance(request_uri, str):
            return False

        return request_uri.startswith('/api') or request_uri.startswith('/login')


    def get_jwt_user(self, request):
        """
        Get the user information from the JWT token in the request.
        :param request: dict, the incoming request details
        :return: dict or None, the user information if the token is valid, None otherwise
        """
        headers = request.get('headers', {})
        auth_header = headers.get('Authorization', None)

        if auth_header:
            user = auth_header.get('user')
            jwt = auth_header.get('jwt')

            if user and jwt:
                expected_jwt = user['name'] + str(datetime.date.today())
                if jwt == expected_jwt:
                    return user

        return None

    def set_current_user_info_and_log(self, user):
        """
        Set the current user information and log the access.
        :param user: dict, the user information
        :return: None
        """
        if user and isinstance(user, dict):
            user_name = user.get('name', 'Unknown')
            user_address = user.get('address', 'Unknown')

            log_message = f"Access log: User '{user_name}' from address '{user_address}' accessed the gateway."
            self.logger.info(log_message)
        else:
            self.logger.warning("Invalid user information provided.")