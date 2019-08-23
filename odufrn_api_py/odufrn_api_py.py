from .modules.Env import Env
from .modules.Exceptions import *

class ODUFRNApi(Env):
    def __init__(self, client_id, client_secret, x_api_key, version):
        super().__init__(client_id, client_secret, x_api_key, version)

    def print_resources(self):
        """Imprime na tela os recursos presentes na API."""
        for resource in self._request_get(self.url_base + 'documentacao'):
            print(
                "Nome: {},\nUrl: {},\n".format(
                    resource['name'],
                    self._format_url_to_resource(resource['url']),
                )
            )
