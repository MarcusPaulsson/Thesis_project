import logging
import datetime
import jwt


class AccessGatewayFilter:
    """
    This class is a filter used for accessing gateway filtering, primarily for authentication and access log recording.
    """

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.jwt_secret = "your-secret-key"

    def filter(self, request):
        """
        Filter the incoming request based on certain rules and conditions.
        :param request: dict, the incoming request details
        :return: bool, True if the request is allowed, False otherwise
        """
        if not request:
            self.logger.warning("Empty request received.")
            return False

        path = request.get('path', '')
        method = request.get('method', '')

        if path == '/login' and method == 'POST':
            return True

        if self.is_start_with(path):
            user = self.get_jwt_user(request)
            if user:
                self.set_current_user_info_and_log(user)
                return True
            else:
                self.logger.warning("Invalid JWT token.")
                return False

        self.logger.info(f"Request to {path} is allowed by default.")
        return True  # Allow by default for other paths.

    def is_start_with(self, request_uri):
        """
        Check if the request URI starts with certain prefixes.
        Currently, the prefixes being checked are "/api" and "/login".
        :param request_uri: str, the URI of the request
        :return: bool, True if the URI starts with certain prefixes, False otherwise
        """
        if request_uri is None:
            return False

        return request_uri.startswith('/api') or request_uri.startswith('/login')

    def get_jwt_user(self, request):
        """
        Get the user information from the JWT token in the request.
        :param request: dict, the incoming request details
        :return: dict or None, the user information if the token is valid, None otherwise
        """
        headers = request.get('headers', {})
        authorization = headers.get('Authorization')

        if not authorization:
            self.logger.warning("Authorization header not found.")
            return None

        try:
            token = authorization
            # Verify and decode the token
            decoded_token = jwt.decode(token, self.jwt_secret, algorithms=["HS256"])  # Replace with your algorithm
            user_info = decoded_token.get('user')
            return user_info
        except jwt.ExpiredSignatureError:
            self.logger.warning("JWT token has expired.")
            return None
        except jwt.InvalidTokenError:
            self.logger.warning("Invalid JWT token.")
            return None
        except Exception as e:
            self.logger.error(f"Error decoding JWT: {e}")
            return None

    def set_current_user_info_and_log(self, user):
        """
        Set the current user information and log the access.
        :param user: dict, the user information
        :return: None
        """
        if user:
            user_name = user.get('name', 'Unknown')
            user_address = user.get('address', 'Unknown')

            self.logger.info(f"User {user_name} from {user_address} accessed the system.")
        else:
            self.logger.warning("User information is missing.")


if __name__ == '__main__':
    import doctest
    doctest.testmod()