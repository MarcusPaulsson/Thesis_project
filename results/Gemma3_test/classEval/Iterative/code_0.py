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
                self.set_current_user_info_and_log(user['user'])
                return True
        return False


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
        if 'headers' in request and 'Authorization' in request['headers']:
            auth_header = request['headers']['Authorization']
            if 'jwt' in auth_header and 'user' in auth_header:
                jwt = auth_header['jwt']
                user = auth_header['user']
                if jwt == user['name'] + str(datetime.date.today()):
                    return {'user': user}
        return None

    def set_current_user_info_and_log(self, user):
        """
        Set the current user information and log the access.
        :param user: dict, the user information
        :return: None
        """
        logging.info(f"User {user.get('name', 'unknown')} accessed the gateway.")