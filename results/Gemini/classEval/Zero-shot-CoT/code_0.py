import logging
import datetime

class AccessGatewayFilter:
    """
    This class is a filter used for accessing gateway filtering, primarily for authentication and access log recording.
    """

    def __init__(self):
        self.logger = logging.getLogger(__name__)

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
                expected_jwt = user['name'] + str(datetime.date.today())
                if jwt_token == expected_jwt:
                    self.set_current_user_info_and_log(user)
                    if 'level' in user and user['level'] > 3:
                        return True
                    elif 'level' in user and user['level'] == 1:
                        return None
                    else:
                        return True
                else:
                    try:
                        user_name = user['name']
                        token_date_str = jwt_token.replace(user_name, '')
                        token_date = datetime.datetime.strptime(token_date_str, '%Y-%m-%d').date()
                        today = datetime.date.today()
                        if (today - token_date).days > 365:
                            return False
                        else:
                            return True
                    except (ValueError, TypeError):
                        return True
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
        self.logger.info(f"Access granted for user: {user}")