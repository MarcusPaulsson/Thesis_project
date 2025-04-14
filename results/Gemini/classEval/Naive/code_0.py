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
        if not isinstance(request, dict):
            self.logger.warning("Invalid request format. Expected a dictionary.")
            return False

        path = request.get('path')
        method = request.get('method')
        headers = request.get('headers', {})

        if not path or not method:
            self.logger.warning("Request missing 'path' or 'method'.")
            return False

        if self.is_start_with(path):
            return True

        auth_header = headers.get('Authorization')
        if auth_header:
            user_info = self.get_jwt_user(request)
            if user_info:
                user = auth_header.get('user')
                jwt_token = auth_header.get('jwt')
                if user and jwt_token:
                    try:
                        user_name = user.get('name')
                        jwt_date_str = jwt_token.replace(user_name, '')
                        jwt_date = datetime.datetime.strptime(jwt_date_str, '%Y-%m-%d').date()
                        today = datetime.date.today()
                        if jwt_date <= today:
                            time_difference = today - jwt_date
                            if time_difference.days <= 365:
                                user_level = user.get('level')
                                if user_level and user_level > 3:
                                    self.set_current_user_info_and_log(user)
                                    return True
                                elif user_level and user_level == 1:
                                    return None
                                else:
                                    self.set_current_user_info_and_log(user)
                                    return True
                            else:
                                return False
                        else:
                            return False
                    except (ValueError, TypeError) as e:
                        self.logger.error(f"Error processing JWT: {e}")
                        return True
                else:
                    return False
            else:
                return True
        else:
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

        headers = request.get('headers', {})
        auth_header = headers.get('Authorization')

        if auth_header:
            user = auth_header.get('user')
            jwt_token = auth_header.get('jwt')

            if user and jwt_token:
                try:
                    user_name = user.get('name')
                    jwt_date_str = jwt_token.replace(user_name, '')
                    jwt_date = datetime.datetime.strptime(jwt_date_str, '%Y-%m-%d').date()
                    today = datetime.date.today()
                    if jwt_date <= today:
                        return user
                    else:
                        return None
                except (ValueError, TypeError) as e:
                    self.logger.error(f"Error processing JWT: {e}")
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
        if not isinstance(user, dict):
            self.logger.warning("Invalid user format. Expected a dictionary.")
            return

        user_name = user.get('name', 'Unknown User')
        user_address = user.get('address', 'Unknown Address')

        self.logger.info(f"User '{user_name}' from '{user_address}' accessed the gateway.")