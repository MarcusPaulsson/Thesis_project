import logging
import datetime
import jwt

class AccessGatewayFilter:
    """
    This class is a filter used for accessing gateway filtering, primarily for authentication and access log recording.
    """

    def __init__(self, secret_key="secret"):
        self.logger = logging.getLogger(__name__)
        self.secret_key = secret_key

    def filter(self, request):
        """
        Filter the incoming request based on certain rules and conditions.
        :param request: dict, the incoming request details
        :return: bool, True if the request is allowed, False otherwise
        """
        if not isinstance(request, dict):
            self.logger.warning("Invalid request format. Expected a dictionary.")
            return False

        if 'path' not in request or 'method' not in request:
            self.logger.warning("Request missing 'path' or 'method'.")
            return False
        
        if request['path'] == '/login' and request['method'] == 'POST':
            return True
        
        if self.is_start_with(request['path']):
            user = self.get_jwt_user(request)
            if user:
                self.set_current_user_info_and_log(user)
                return True
            else:
                self.logger.warning(f"Unauthorized access attempt to {request['path']}")
                return False
        
        return True


    def is_start_with(self, request_uri):
        """
        Check if the request URI starts with certain prefixes.
        Currently, the prefixes being checked are "/api" and "/login".
        :param request_uri: str, the URI of the request
        :return: bool, True if the URI starts with certain prefixes, False otherwise
        """
        if not isinstance(request_uri, str):
            self.logger.warning("Invalid request URI format. Expected a string.")
            return False
        
        return request_uri.startswith("/api") or request_uri.startswith("/login")


    def get_jwt_user(self, request):
        """
        Get the user information from the JWT token in the request.
        :param request: dict, the incoming request details
        :return: dict or None, the user information if the token is valid, None otherwise
        """
        if not isinstance(request, dict):
            self.logger.warning("Invalid request format. Expected a dictionary.")
            return None

        if 'headers' not in request or 'Authorization' not in request['headers']:
            self.logger.warning("Authorization header not found.")
            return None
        
        auth_header = request['headers']['Authorization']
        if not isinstance(auth_header, str):
            self.logger.warning("Invalid Authorization header format. Expected a string.")
            return None

        try:
            token = auth_header.split(" ")[1]
            decoded_token = jwt.decode(token, self.secret_key, algorithms=["HS256"])
            return decoded_token.get('user')
        except jwt.ExpiredSignatureError:
            self.logger.warning("JWT token has expired.")
            return None
        except jwt.InvalidTokenError:
            self.logger.warning("Invalid JWT token.")
            return None
        except Exception as e:
            self.logger.error(f"Error decoding JWT token: {e}")
            return None

    def set_current_user_info_and_log(self, user):
        """
        Set the current user information and log the access.
        :param user: dict, the user information
        :return: None
        """
        if not isinstance(user, dict):
            self.logger.warning("Invalid user format. Expected a dictionary.")
            return
        
        self.logger.info(f"Access granted to user: {user.get('name', 'Unknown')}")


if __name__ == '__main__':
    import doctest
    logging.basicConfig(level=logging.INFO)
    doctest.testmod()