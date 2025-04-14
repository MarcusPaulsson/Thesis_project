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
            auth_data = request['headers']['Authorization']
            user = auth_data.get('user')
            jwt_token = auth_data.get('jwt')

            if user and jwt_token:
                jwt_user = self.get_jwt_user(request)
                if jwt_user:
                    user_level = user.get('level')
                    if user_level is not None:
                        if user_level > 3:
                            return True
                        elif user_level == 3:
                            return True
                        else:
                            return None
                    else:
                        return True
                else:
                    return True # even if jwt is invalid, still return true for other checks

        return True


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
            auth_data = request['headers']['Authorization']
            user = auth_data.get('user')
            jwt_token = auth_data.get('jwt')

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
        """
        self.logger.info(f"User {user['name']} from {user['address']} accessed the gateway.")