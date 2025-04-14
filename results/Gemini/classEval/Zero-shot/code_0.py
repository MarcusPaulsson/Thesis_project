import logging
import datetime

class AccessGatewayFilter:
    """
    This class is a filter used for accessing gateway filtering, primarily for authentication and access log recording.
    """

    def __init__(self):
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger(__name__)

    def filter(self, request):
        """
        Filter the incoming request based on certain rules and conditions.
        :param request: dict, the incoming request details
        :return: bool, True if the request is allowed, False otherwise
        """
        if self.is_start_with(request.get('path')):
            return True

        auth_header = request.get('headers', {}).get('Authorization')
        if auth_header:
            user = auth_header.get('user')
            jwt_token = auth_header.get('jwt')
            if user and jwt_token:
                expected_jwt = user['name'] + str(datetime.date.today())
                if jwt_token == expected_jwt:
                    self.set_current_user_info_and_log(user)
                    return True
                else:
                    try:
                        user_name = user['name']
                        jwt_date_str = jwt_token.replace(user_name, '')
                        jwt_date = datetime.datetime.strptime(jwt_date_str, '%Y-%m-%d').date()
                        today = datetime.date.today()
                        diff = today - jwt_date
                        if diff.days > 365:
                            return False
                        else:
                            return True
                    except (ValueError, TypeError):
                        return True
            else:
                return True
        else:
            return None


    def is_start_with(self, request_uri):
        """
        Check if the request URI starts with certain prefixes.
        Currently, the prefixes being checked are "/api" and "/login".
        :param request_uri: str, the URI of the request
        :return: bool, True if the URI starts with certain prefixes, False otherwise
        """
        if request_uri.startswith('/api') or request_uri.startswith('/login'):
            return True
        return False

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
                    return {'user': user}
                else:
                    return None
            else:
                return None
        else:
            return None

    def set_current_user_info_and_log(self, user):
        """
        Set the current user information and log the access.
        :param user: dict, the user information
        :return: None
        """
        self.logger.info(f"Access granted for user: {user}")
        # In a real application, you would likely store the user information
        # in a thread-local variable or a similar mechanism for later use.
        pass