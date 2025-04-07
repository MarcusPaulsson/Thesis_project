import logging
import datetime

class AccessGatewayFilter:
    """
    This class is a filter used for accessing gateway filtering, primarily for authentication and access log recording.
    """

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        ch = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

    def filter(self, request):
        """
        Filter the incoming request based on certain rules and conditions.
        :param request: dict, the incoming request details
        :return: bool, True if the request is allowed, False otherwise
        >>> filter = AccessGatewayFilter()
        >>> filter.filter({'path': '/login', 'method': 'POST'})
        True

        """
        if self.is_start_with(request.get('path')):
            return True

        auth_header = request.get('headers', {}).get('Authorization')
        if auth_header:
            user = auth_header.get('user')
            jwt_token = auth_header.get('jwt')
            if user and jwt_token:
                jwt_user = self.get_jwt_user(request)
                if jwt_user:
                    level = user.get('level')
                    if level is not None:
                        if level > 3:
                            return True
                        elif level < 2:
                            return None
                        else:
                            return False
                    else:
                        return True
                else:
                    return True  # Allow if JWT is invalid but present


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
        self.logger.info(f"Access granted to user: {user}")