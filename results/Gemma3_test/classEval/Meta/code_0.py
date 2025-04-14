import logging
import datetime

class AccessGatewayFilter:
    """
    This class is a filter used for accessing gateway filtering, primarily for authentication and access log recording.
    """

    def __init__(self):
        pass

    def filter(self, request):
        """
        Filter the incoming request based on certain rules and conditions.
        :param request: dict, the incoming request details
        :return: bool, True if the request is allowed, False otherwise
        >>> filter = AccessGatewayFilter()
        >>> filter.filter({'path': '/login', 'method': 'POST'})
        True

        """
        path = request.get('path', '')
        method = request.get('method', '')
        headers = request.get('headers', {})

        if self.is_start_with(path):
            return True

        if 'Authorization' in headers:
            user = self.get_jwt_user(request)
            if user:
                self.set_current_user_info_and_log(user['user'])
                return True
        return None


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
        headers = request.get('headers', {})
        if 'Authorization' in headers:
            auth_data = headers['Authorization']
            if 'user' in auth_data and 'jwt' in auth_data:
                user = auth_data['user']
                jwt = auth_data['jwt']
                today = datetime.date.today()
                try:
                    if jwt.startswith(user['name']) and today == datetime.datetime.strptime(jwt[len(user['name']):], "%Y-%m-%d").date():
                        return auth_data
                    else:
                        return None
                except ValueError:
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
        logging.info(f"User {user.get('name', 'unknown')} accessed the gateway.")