import logging
import datetime
import jwt
import os

class AccessGatewayFilter:
    """
    This class is a filter used for accessing gateway filtering, primarily for authentication and access log recording.
    """

    def __init__(self, jwt_secret=None, log_level=logging.INFO, log_file='access.log'):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(log_level)

        # Remove existing handlers to prevent duplicate logs if re-initialized
        for handler in self.logger.handlers[:]:
            self.logger.removeHandler(handler)

        # Create handlers
        c_handler = logging.StreamHandler()
        f_handler = logging.FileHandler(log_file)

        c_handler.setLevel(log_level)
        f_handler.setLevel(log_level)

        # Create formatters and add it to handlers
        c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
        f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        c_handler.setFormatter(c_format)
        f_handler.setFormatter(f_format)

        # Add handlers to the logger
        self.logger.addHandler(c_handler)
        self.logger.addHandler(f_handler)

        # Securely manage the JWT secret
        self.jwt_secret = jwt_secret or os.environ.get("JWT_SECRET")
        if not self.jwt_secret:
            self.logger.warning(
                "JWT_SECRET is not set. Authentication will not function correctly.  "
                "Please set the JWT_SECRET environment variable or pass it to the constructor."
            )

    def filter(self, request):
        """
        Filter the incoming request based on certain rules and conditions.
        :param request: dict, the incoming request details
        :return: bool, True if the request is allowed, False otherwise
        """
        if not request:
            self.logger.warning("Empty request received.")
            return False

        path = request.get('path')
        method = request.get('method')

        if path == '/login' and method == 'POST':
            self.logger.info("Allowing access to /login endpoint.")
            return True

        if self.is_start_with(path):
            user = self.get_jwt_user(request)
            if user:
                self.set_current_user_info_and_log(user)
                return True
            else:
                # get_jwt_user already logs the error, so no need to repeat it here.
                return False

        self.logger.debug(f"Allowing access to {path} without authentication.")
        return True  # Default allow, unless explicitly denied

    def is_start_with(self, request_uri):
        """
        Check if the request URI starts with certain prefixes.
        Currently, the prefixes being checked are "/api" and "/login".
        :param request_uri: str, the URI of the request
        :return: bool, True if the URI starts with certain prefixes, False otherwise
        """
        if not request_uri:
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
            self.logger.debug("No Authorization header found.")
            return None

        if not isinstance(authorization, str): # Expecting a string like "Bearer <token>"
            self.logger.warning("Invalid Authorization header format. Expected a string.")
            return None

        try:
            scheme, token = authorization.split(" ", 1)
            if scheme.lower() != "bearer":
                self.logger.warning(f"Invalid Authorization scheme: {scheme}. Expected 'Bearer'.")
                return None

        except ValueError:
             self.logger.warning("Malformed Authorization header. Expected 'Bearer <token>'.")
             return None

        if not self.jwt_secret:
            self.logger.error("JWT Secret is not configured. Cannot verify JWT.")
            return None

        try:
            # Verify the JWT token.  Include leeway for clock skew.
            decoded_token = jwt.decode(token, self.jwt_secret, algorithms=["HS256"], leeway=datetime.timedelta(seconds=30))
            return decoded_token  # Return the entire decoded token

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
        :param user: dict, the user information (decoded JWT payload)
        :return: None
        """
        if user:
            user_id = user.get('user_id', 'Unknown') # Assuming the JWT contains a 'user_id'
            self.logger.info(f"Access granted for user ID: {user_id}")
        else:
            self.logger.warning("No user information to log.")


if __name__ == '__main__':
    # Example usage (replace with your actual testing)
    filter = AccessGatewayFilter(jwt_secret="my_super_secret_key")

    # Example request
    request = {
        'path': '/api/protected',
        'method': 'GET',
        'headers': {
            'Authorization': 'Bearer <your_jwt_token>'  # Replace with a valid JWT token
        }
    }

    # Simulate generating a JWT (for testing purposes only; in real code, this would be done during login)
    payload = {
        'user_id': '123',
        'username': 'testuser',
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Token expires in 1 hour
    }
    jwt_token = jwt.encode(payload, "my_super_secret_key", algorithm="HS256")
    request['headers']['Authorization'] = f"Bearer {jwt_token}"


    is_allowed = filter.filter(request)

    if is_allowed:
        print("Request is allowed.")
    else:
        print("Request is denied.")

    request = {'path': '/login', 'method': 'POST'}
    is_allowed = filter.filter(request)

    if is_allowed:
        print("Request is allowed.")
    else:
        print("Request is denied.")