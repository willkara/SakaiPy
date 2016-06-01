import random
import string

from requests import Session

loginURLtemplate = "/portal/xlogin"


class SakaiSession(Session):
    """
    Create and maintain a session in Sakai.
    """

    def __init__(self, username, password, base_url):
        super().__init__()

        # Create the session and then grab the generated session id.
        self.csrftoken = ''.join(
            random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(25))
        self.data = {'csrftoken': self.csrftoken,
                     'eid': username,
                     'pw': password}
        self.api_url = base_url + '/direct'

        self.session_id = self.post(base_url + loginURLtemplate,
                                    data=self.data).headers.get('X-Sakai-Session')

    def terminate_session(self):
        """
        Terminate the current session
        :return:
        """
        return self.delete(self.api_url + '/session/' + self.session_id)

    def get_current_user_info(self):
        """
        Get information for the currently logged in user.
        :return:
        """
        return self.get(self.api_url + '/user/current.json').json()

    def get_session_info(self):
        """
        Get information about the current session.
        :return:
        """
        return self.get(self.api_url + '/session/current.json').json()

    def executeRequest(self, type, url, data=None, params=None):
        """
        Execute a HTTP request. We handle it ourselves.
        :param type: The type of HTTP request to execute.
        :param url: The right half of the URL to execute. Everything BUT the api url.
        :param data: The data to include, if any.
        :param params: The parameters to include, if any.
        :return: A Response Object.
        """

        if data is None:
            data = {'csrftoken': self.csrftoken}
        else:
            data['csrftoken'] = self.csrftoken

        if type is 'GET':
            return self.get(self.api_url + url).json()
        elif type is 'POST':
            return self.post(self.api_url + url, data=data, params=params)
        else:
            return None
