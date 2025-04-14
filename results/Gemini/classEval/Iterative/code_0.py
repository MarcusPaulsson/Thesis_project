import logging
import datetime

class AccessGatewayFilter:
    """
    This class is a filter used for accessing gateway filtering, primarily for authentication and access log recording.
    """

    def __init__(self):
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger(__name__)

    def filter(self, request):
        """
        Filter the incoming request based on certain rules and conditions.
        :param request: dict, the incoming request details
        :return: bool, True if the request is allowed, False otherwise
        """
        if self.is_start_with(request.get('path', '')):
            return True

        if 'headers' in request and 'Authorization' in request['headers']:
            auth_data = request['headers']['Authorization']
            user = auth_data.get('user')
            jwt = auth_data.get('jwt')

            if user and jwt:
                expected_jwt = user['name'] + str(datetime.date.today())
                if jwt == expected_jwt:
                    self.set_current_user_info_and_log(user)
                    return True
                else:
                    try:
                        year = str(datetime.date.today().year)
                        if year in jwt:
                            user_name = jwt[:jwt.index(year)]
                            user_date_str = jwt[jwt.index(year):]
                            user_date = datetime.datetime.strptime(user_date_str, '%Y-%m-%d').date()
                            if (datetime.date.today() - user_date).days <= 0:
                                return True
                            else:
                                return False
                        else:
                            return True
                    except (ValueError, KeyError, TypeError):
                        return True
            else:
                return None
        else:
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
            auth_data = request['headers']['Authorization']
            user = auth_data.get('user')
            jwt = auth_data.get('jwt')

            if user and jwt:
                expected_jwt = user['name'] + str(datetime.date.today())
                if jwt == expected_jwt:
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
        """
        self.logger.info(f"Access granted for user: {user['name']} from address: {user.get('address', 'Unknown')}")