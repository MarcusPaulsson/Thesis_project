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
        """
        if self.is_start_with(request.get('path', '')):
            return True

        if 'headers' in request and 'Authorization' in request['headers']:
            user = self.get_jwt_user(request)
            if user:
                if user.get('user', {}).get('level', 0) >= 3:
                    self.set_current_user_info_and_log(user['user'])
                    return True
                else:
                    return False
            else:
                return False
        return None


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
        if 'headers' in request and 'Authorization' in request['headers']:
            auth_header = request['headers']['Authorization']
            if 'jwt' in auth_header and 'user' in auth_header:
                jwt_token = auth_header['jwt']
                user_info = auth_header['user']
                today = datetime.date.today()
                try:
                    user_name = user_info['name']
                    if jwt_token == user_name + str(today):
                        return auth_header
                    else:
                        return None
                except (KeyError, TypeError):
                    return None
        return None

    def set_current_user_info_and_log(self, user):
        """
        Set the current user information and log the access.
        :param user: dict, the user information
        :return: None
        """
        logging.info(f"User {user.get('name', 'unknown')} accessed the gateway.")