
from datetime import datetime
import time
from social_core.backends.oauth import BaseOAuth2
from django.conf import settings


class WSO2OAuth2(BaseOAuth2):    
    auth_server_hostname = settings.SOCIAL_AUTH_WSO2_HOSTNAME
    print (auth_server_hostname)
    # "http" or "https"
    http_scheme = "https"
    # backend name
    name = "wso2"
        
    auth_server_full_url = "{0}://{1}".format(http_scheme, auth_server_hostname)
    AUTHORIZATION_URL = "{0}/oauth2/authorize".format(auth_server_full_url)
    ACCESS_TOKEN_URL = "{0}/oauth2/token".format(auth_server_full_url)
    ACCESS_TOKEN_METHOD = "POST"
    SCOPE_SEPARATOR = ","
    ID_KEY = "username"
    EXTRA_DATA = [        
    ]

    # user data endpoint
    USER_DATA_URL = "{0}/oauth2/userinfo".format(auth_server_full_url)

    # small margin in expires_at to be safe
    margin_in_seconds = 300

    # testing purpose
    # set_expires_in_to = margin_in_seconds + 20
    set_expires_in_to = None    

    def get_user_details(self, response):        
        return {
            "username": response.get("username"),
            "email": response.get("email"),
        }

    def user_data(self, access_token, *args, **kwargs):        
        try:            
            user = self.get_json(
                self.USER_DATA_URL, params={"access_token": access_token}
            )            
            return {
                'username': user['sub'],
            }
        except ValueError:
            return None

    def auth_complete(self, *args, **kwargs):
        """Completes login process, must return user instance"""
        self.process_error(self.data)
        state = self.validate_state()
        data, params = None, None
        if self.ACCESS_TOKEN_METHOD == "GET":
            params = self.auth_complete_params(state)
        else:
            data = self.auth_complete_params(state)        
        response = self.request_access_token(
            self.access_token_url(),
            data=data,
            params=params,
            headers=self.auth_headers(),
            auth=self.auth_complete_credentials(),
            method=self.ACCESS_TOKEN_METHOD,
        )
        self.process_error(response)
        return self.do_auth(
            response["access_token"], response=response, *args, **kwargs
        )