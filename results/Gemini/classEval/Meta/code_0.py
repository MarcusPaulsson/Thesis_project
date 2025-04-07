import logging
import datetime

class AccessGatewayFilter:
    """
    This class is a filter used for accessing gateway filtering, primarily for authentication and access log recording.
    """

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

        # Create a handler that writes log messages to a file
        fh = logging.FileHandler('access_gateway.log')
        fh.setLevel(logging.INFO)

        # Create a formatter and set the formatter for the handler
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)

        # Add the handler to the logger
        self.logger.addHandler(fh)

    def filter(self, request):
        """
        Filter the incoming request based on certain rules and conditions.
        :param request: dict, the incoming request details
        :return: bool, True if the request is allowed, False otherwise
        >>> filter = AccessGatewayFilter()
        >>> filter.filter({'path': '/login', 'method': 'POST'})
        True

        """
        if self.is_start_with(request['path']):
            return True

        if 'headers' in request and 'Authorization' in request['headers']:
            auth_data = request['headers']['Authorization']
            user = auth_data.get('user')
            jwt_token = auth_data.get('jwt')

            if user and jwt_token:
                jwt_user = self.get_jwt_user(request)
                if jwt_user:
                    if user['level'] == 1:
                        return None
                    elif user['level'] >= 3:
                        return True
                    else:
                        return True
                else:
                    return False
            else:
                return True
        else:
            return True


    def is_start_with(self, request_uri):
        """
        Check if the request URI starts with certain prefixes.
        Currently, the prefixes being checked are "/api" and "/login".
        :param request_uri: str, the URI of the request
        :return: bool, True if the URI starts with certain prefixes, False otherwise
        >>> filter = AccessGatewayFilter()
        >>> filter.is_start_with('/api/data')
        True

        """
        return request_uri.startswith('/api') or request_uri.startswith('/login')


    def get_jwt_user(self, request):
        """
        Get the user information from the JWT token in the request.
        :param request: dict, the incoming request details
        :return: dict or None, the user information if the token is valid, None otherwise
        >>> filter = AccessGatewayFilter()
        >>> filter.get_jwt_user({'headers': {'Authorization': {'user': {'name': 'user1'}, 'jwt': 'user1'+str(datetime.date.today())}}})
        {'user': {'name': 'user1'}

        """
        if 'headers' in request and 'Authorization' in request['headers']:
            auth_data = request['headers']['Authorization']
            user = auth_data.get('user')
            jwt_token = auth_data.get('jwt')

            if user and jwt_token:
                expected_jwt = user['name'] + str(datetime.date.today())
                if jwt_token == expected_jwt:
                    return user
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
        >>> filter = AccessGatewayFilter()
        >>> user = {'name': 'user1', 'address': '127.0.0.1'}
        >>> filter.set_current_user_info_and_log(user)

        """
        self.logger.info(f"User access: {user}")