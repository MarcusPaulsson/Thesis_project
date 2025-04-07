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
        """
        if self.is_start_with(request.get('path')):
            return True

        auth_header = request.get('headers', {}).get('Authorization')
        if auth_header:
            user_info = auth_header.get('user')
            jwt_token = auth_header.get('jwt')
            if user_info and jwt_token:
                user_from_jwt = self.get_jwt_user(request)
                if user_from_jwt:
                    self.set_current_user_info_and_log(user_info)
                    if user_info.get('level') == 1:
                        return None
                    elif user_info.get('level') == 3:
                        return True
                    else:
                        return True
                else:
                    return True
        return True

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
        auth_header = request.get('headers', {}).get('Authorization')
        if auth_header:
            user_info = auth_header.get('user')
            jwt_token = auth_header.get('jwt')
            if user_info and jwt_token:
                expected_jwt = user_info.get('name') + str(datetime.date.today())
                if jwt_token == expected_jwt:
                    return {'user': user_info}
                else:
                    return None
        return None

    def set_current_user_info_and_log(self, user):
        """
        Set the current user information and log the access.
        :param user: dict, the user information
        :return: None
        """
        self.logger.info(f"Access by user: {user}")


if __name__ == '__main__':
    import doctest
    doctest.testmod()