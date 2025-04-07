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
        path = request.get('path', '')
        method = request.get('method', '').upper()
        
        if self.is_start_with(path):
            return True
        
        if 'headers' in request and 'Authorization' in request['headers']:
            user_info = self.get_jwt_user(request)
            if user_info is not None:
                level = user_info.get('level', 0)
                if level >= 3:
                    self.set_current_user_info_and_log(user_info)
                    return True
                elif level == 1:
                    return None
        return False

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
            auth = request['headers']['Authorization']
            jwt = auth.get('jwt', '')
            expected_jwt = auth['user']['name'] + str(datetime.date.today())

            if jwt == expected_jwt:
                return auth['user']
        return None

    def set_current_user_info_and_log(self, user):
        """
        Set the current user information and log the access.
        :param user: dict, the user information
        :return: None
        """
        logging.info(f"Access granted for user: {user['name']} from address: {user['address']}")