import logging
import datetime
from typing import Dict, Any, Optional

class AccessGatewayFilter:
    """
    This class is a filter used for accessing gateway filtering, primarily for authentication and access log recording.
    """

    def __init__(self):
        self.allowed_prefixes = ['/api', '/login'] # initialize allowed prefixes as a list of strings
        self.log = logging.getLogger(__name__)


    def filter(self, request: Dict[str, Any]) -> bool:
        """
        Filter the incoming request based on certain rules and conditions.
        :param request: dict, the incoming request details
        :return: bool, True if the request is allowed, False otherwise
        """
        self.log.info(f"Incoming request: {request}") # log the request

        uri = request['path'] # get the URI from the request dictionary
        method = request['method'] # get the HTTP method from the request dictionary
        if method == 'POST':
            if self.is_start_with(uri):
                jwt_token = None
                try:
                    headers = request['headers']['Authorization'] # assuming that the JWT token is in the "Authorization" header
                    jwt_token = headers['jwt']
                except KeyError:
                    self.log.warning("No JWT token found in the request")
                    return False

                user = self.get_jwt_user(jwt_token)
                if user is not None: # if there's a valid JWT token, set the current user and log the access
                    self.set_current_user_info_and_log(user)
                    return True

        return False # by default, deny all non-POST requests or those with invalid JWT tokens


    def is_start_with(self, request_uri: str) -> bool:
        """
        Check if the request URI starts with certain prefixes.
        Currently, the prefixes being checked are "/api" and "/login".
        :param request_uri: str, the URI of the request
        :return: bool, True if the URI starts with certain prefixes, False otherwise
        """
        for prefix in self.allowed_prefixes: # iterate through all allowed prefixes
            if request_uri.startswith(prefix):
                return True

        return False

    def get_jwt_user(self, jwt_token: str) -> Optional[Dict]:
        """
        Get the user information from the JWT token in the request.
        :param jwt_token: str, the incoming JWT token
        :return: dict or None, the user information if the token is valid, None otherwise
        """

        # Here's a simple example implementation for checking the JWT token. You should replace this with your own validation logic.
        token_user = jwt_token.split('+')[0] # assuming that the user information is in the first part of the token
        try:
            datetime.datetime.strptime(jwt_token.split('+')[1], '%Y-%m-%d') # check if the second part is a valid date string
            return {'name': token_user}
        except ValueError as e:
            self.log.error(f"Invalid JWT token: {e}")

        return None

    def set_current_user_info_and_log(self, user: Dict[str, str]):
        """
        Set the current user information and log the access.
        :param user: dict, the user information
        :return: None
        """
        self.log.info(f"User {user['name']} accessed {request['path']} using {request['method']}") # log the access with user info and method