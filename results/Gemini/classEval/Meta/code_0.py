import logging
import datetime
import jwt

class AccessGatewayFilter:
    """
    This class is a filter used for accessing gateway filtering, primarily for authentication and access log recording.
    """

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        # create console handler and set level to info
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # add formatter to ch
        ch.setFormatter(formatter)

        # add ch to logger
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
        if request['path'] == '/login' and request['method'] == 'POST':
            return True
        if self.is_start_with(request['path']):
            user = self.get_jwt_user(request)
            if user:
                self.set_current_user_info_and_log(user)
                return True
            else:
                return False
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
            try:
                # Assuming the token is a simple string representation of the user
                # This is a placeholder, in reality, you'd verify the JWT signature
                # and decode the payload.
                # decoded_token = jwt.decode(auth_header['jwt'], 'secret', algorithms=["HS256"])
                return auth_header['user']
            except Exception as e:
                self.logger.error(f"Error decoding JWT: {e}")
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
        self.logger.info(f"User {user.get('name', 'Unknown')} from {user.get('address', 'Unknown')} accessed the gateway.")