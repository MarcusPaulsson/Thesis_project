import logging
import datetime

class AccessGatewayFilter:
    """
    This class is a filter used for accessing gateway filtering, primarily for authentication and access log recording.
    """

    def __init__(self):
        self.allowed_paths = ["/api", "/login"]
        logging.basicConfig(level=logging.INFO)

    def filter(self, request):
        """
        Filter the incoming request based on certain rules and conditions.
        :param request: dict, the incoming request details
        :return: bool, True if the request is allowed, False otherwise
        """
        if self.is_start_with(request['path']):
            user = self.get_jwt_user(request)
            if user:
                self.set_current_user_info_and_log(user)
                return True
            return False
        return True  # Allow access for paths not requiring authentication

    def is_start_with(self, request_uri):
        """
        Check if the request URI starts with certain prefixes.
        :param request_uri: str, the URI of the request
        :return: bool, True if the URI starts with certain prefixes, False otherwise
        """
        return any(request_uri.startswith(prefix) for prefix in self.allowed_paths)

    def get_jwt_user(self, request):
        """
        Get the user information from the JWT token in the request.
        :param request: dict, the incoming request details
        :return: dict or None, the user information if the token is valid, None otherwise
        """
        auth_header = request.get('headers', {}).get('Authorization')
        if auth_header and 'jwt' in auth_header and self.validate_jwt(auth_header['jwt']):
            return auth_header['user']
        return None

    def validate_jwt(self, jwt):
        # Placeholder for JWT validation logic
        # For example, check if the JWT is well-formed and not expired
        return True

    def set_current_user_info_and_log(self, user):
        """
        Set the current user information and log the access.
        :param user: dict, the user information
        :return: None
        """
        logging.info(f"User Access: {user['name']} from {user.get('address', 'unknown')} at {datetime.datetime.now()}")