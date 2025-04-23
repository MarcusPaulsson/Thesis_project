import logging
import datetime

class AccessGatewayFilter:
    """
    This class is a filter used for accessing gateway filtering, primarily for authentication and access log recording.
    """

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.api_prefixes = ["/api", "/login"]
        self.auth_level_threshold = 3

    def filter(self, request):
        """
        Filter the incoming request based on certain rules and conditions.
        :param request: dict, the incoming request details
        :return: bool, True if the request is allowed, False otherwise
        """
        if not self._is_valid_request(request):
            return False

        if self.is_start_with(request['path']):
            return True

        auth_result = self._check_authorization(request)
        return auth_result

    def _is_valid_request(self, request):
        """
        Validates the request format.
        """
        if not request or not isinstance(request, dict):
            self.logger.warning("Invalid request format.")
            return False

        if 'path' not in request or 'method' not in request:
            self.logger.warning("Request missing 'path' or 'method'.")
            return False

        return True

    def _check_authorization(self, request):
        """
        Checks the authorization header and validates JWT if present.
        """
        if 'headers' in request and 'Authorization' in request['headers']:
            auth_data = request['headers']['Authorization']
            user = auth_data.get('user')
            jwt = auth_data.get('jwt')

            if user and jwt:
                jwt_user = self.get_jwt_user(request)
                if jwt_user:
                    user_level = user.get('level', 1)
                    if user_level >= self.auth_level_threshold:
                        self.set_current_user_info_and_log(user)
                        return True
                    else:
                        return None
                else:
                    return False
            else:
                return True  # Allow if no user/jwt info, assuming other auth mechanisms

        return None #Indicate that the filter doesn't have enough information to make a decision.

    def is_start_with(self, request_uri):
        """
        Check if the request URI starts with certain prefixes.
        Currently, the prefixes being checked are "/api" and "/login".
        :param request_uri: str, the URI of the request
        :return: bool, True if the URI starts with certain prefixes, False otherwise
        """
        if not request_uri or not isinstance(request_uri, str):
            return False

        for prefix in self.api_prefixes:
            if request_uri.startswith(prefix):
                return True
        return False

    def get_jwt_user(self, request):
        """
        Get the user information from the JWT token in the request.
        :param request: dict, the incoming request details
        :return: dict or None, the user information if the token is valid, None otherwise
        """
        if not request or not isinstance(request, dict) or 'headers' not in request or 'Authorization' not in request['headers']:
            return None

        auth_data = request['headers']['Authorization']
        user = auth_data.get('user')
        jwt = auth_data.get('jwt')

        if not user or not jwt:
            return None

        try:
            user_name = user.get('name')
            expected_jwt = user_name + str(datetime.date.today())
            if jwt == expected_jwt:
                return user
            else:
                return None
        except Exception as e:
            self.logger.error(f"Error during JWT validation: {e}")
            return None

    def set_current_user_info_and_log(self, user):
        """
        Set the current user information and log the access.
        :param user: dict, the user information
        :return: None
        """
        if not user or not isinstance(user, dict):
            self.logger.warning("Invalid user information.")
            return

        user_name = user.get('name', 'Unknown')
        user_address = user.get('address', 'Unknown')

        log_message = f"Access granted for user: {user_name} from address: {user_address}"
        self.logger.info(log_message)