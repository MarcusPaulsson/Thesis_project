import logging
import datetime

class AccessGatewayFilter:
    """
    This class is a filter used for accessing gateway filtering, primarily for authentication and access log recording.
    """

    def __init__(self):
        self.allowed_paths = ['/api', '/login']
        logging.basicConfig(level=logging.INFO)

    def filter(self, request):
        """
        Filter the incoming request based on certain rules and conditions.
        :param request: dict, the incoming request details
        :return: bool, True if the request is allowed, False otherwise
        """
        if not isinstance(request, dict):
            logging.error("Invalid request format.")
            return False
        
        if self.is_start_with(request.get('path', '')):
            user = self.get_jwt_user(request)
            if user:
                self.set_current_user_info_and_log(user)
                return True
        
        logging.warning("Request denied for path: %s", request.get('path'))
        return False

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
        try:
            auth_header = request.get('headers', {}).get('Authorization', {})
            user_info = auth_header.get('user')
            # Here we would normally validate JWT, omitted for simplicity
            return user_info if user_info else None
        except Exception as e:
            logging.error("Error retrieving JWT user: %s", e)
            return None

    def set_current_user_info_and_log(self, user):
        """
        Set the current user information and log the access.
        :param user: dict, the user information
        """
        logging.info("User accessed: %s from address: %s", user.get('name'), user.get('address', 'unknown'))