import logging
import datetime
import jwt


class AccessGatewayFilter:
    """
    This class is a filter used for accessing gateway filtering, primarily for authentication and access log recording.
    """

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO)

    def filter(self, request):
        """
        Filter the incoming request based on certain rules and conditions.
        :param request: dict, the incoming request details
        :return: bool, True if the request is allowed, False otherwise
        >>> filter = AccessGatewayFilter()
        >>> filter.filter({'path': '/login', 'method': 'POST'})
        True

        """
        if request.get('path') == '/login' and request.get('method') == 'POST':
            return True
        elif self.is_start_with(request.get('path')):
            user = self.get_jwt_user(request)
            if user:
                self.set_current_user_info_and_log(user)
                return True
            else:
                self.logger.warning("Invalid JWT token, request rejected.")
                return False
        else:
            self.logger.info(f"Request to {request.get('path')} allowed without authentication.")
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
        if request_uri and (request_uri.startswith('/api') or request_uri.startswith('/login')):
            return True
        else:
            return False

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
                user_data = auth_header.get('user')
                jwt_token = auth_header.get('jwt')

                # Verify JWT token (replace 'your-secret-key' with your actual secret key)
                payload = jwt.decode(jwt_token, 'your-secret-key', algorithms=['HS256'])

                if user_data and 'user' in user_data:
                   return user_data
                else:
                    self.logger.warning("User data missing from JWT.")
                    return user_data

            except jwt.ExpiredSignatureError:
                self.logger.warning("JWT token has expired.")
                return None
            except jwt.InvalidTokenError:
                self.logger.warning("Invalid JWT token.")
                return None
            except Exception as e:
                self.logger.error(f"Error decoding JWT: {e}")
                return None
        else:
            self.logger.warning("Authorization header missing.")
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

if __name__ == '__main__':
    import doctest
    doctest.testmod()