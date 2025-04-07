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
        """
        if self.is_start_with(request['path']):
            return True
        
        if 'headers' in request and 'Authorization' in request['headers']:
            user_info = self.get_jwt_user(request)
            if user_info:
                level = user_info.get('level', 0)
                if level >= 3:
                    self.set_current_user_info_and_log(user_info)
                    return True
                elif level == 1:
                    return None
                else:
                    return False
        return False

    def is_start_with(self, request_uri):
        """
        Check if the request URI starts with certain prefixes.
        Currently, the prefixes being checked are "/api" and "/login".
        :param request_uri: str, the URI of the request
        :return: bool, True if the URI starts with certain prefixes, False otherwise
        """
        return request_uri.startswith(('/api', '/login'))

    def get_jwt_user(self, request):
        """
        Get the user information from the JWT token in the request.
        :param request: dict, the incoming request details
        :return: dict or None, the user information if the token is valid, None otherwise
        """
        auth = request.get('headers', {}).get('Authorization', {})
        user = auth.get('user')
        jwt = auth.get('jwt')
        
        if user and jwt == user['name'] + str(datetime.date.today()):
            return user
        return None

    def set_current_user_info_and_log(self, user):
        """
        Set the current user information and log the access.
        :param user: dict, the user information
        :return: None
        """
        self.logger.info(f"User logged in: {user['name']} from {user.get('address', 'unknown')}")