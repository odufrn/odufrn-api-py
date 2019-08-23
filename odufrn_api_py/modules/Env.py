import json
import requests
from abc import ABC


class Env(ABC):
    def __init__(self, client_id, client_secret, x_api_key, version):
        self.url_base = 'https://api.ufrn.br/'
        self.warnings = False
        self.swagger_url = 'https://swagger.info.ufrn.br/'
        self.url_base_autenticacao = 'https://autenticacao.info.ufrn.br/'
        # construtores
        self.client_id = client_id
        self.client_secret = client_secret
        self.x_api_key = x_api_key
        self.version = version
        autenticacao = ('authz-server/oauth/token?' +
                        'client_id={0}&client_secret={1}' +
                        '&grant_type=client_credentials'
                        ).format(client_id, client_secret)
        # variáveis necessárias para autenticação na api
        self.url_token = self.url_base_autenticacao + autenticacao
        self.token = ''
        self.token_expires_in = 0
        self.headers = {
            'Authorization': 'bearer ' + self.token,
            'x-api-key': self.x_api_key
        }
        self._auth_api_request()

    def _format_url_to_resource(self, url):
        """Transforma uma url de um recurso em um nome de recurso.

        Ex.
            converte:
                https://swagger.info.ufrn.br/?url=https://api.ufrn.br/acao-associada/v1/v2/api-docs
            em:
                https://api.ufrn.br/acao-associada/v1/v2/api-docs
        """
        return url.replace(self.swagger_url + '?url=', '')

    def _auth_api_request(self):
        """Realiza o processo de autenticacao dos dados do usuário.

        Primeiro realiza uma requisição post com as chaves da api,
        essa requisição retorna uma chave de acesso e quando essa
        chave irá expirar.
        """
        requisicao_token = requests.post(self.url_token)
        resposta = json.loads(requisicao_token.content)
        self.token = resposta['access_token']
        self.token_expires_in = resposta['expires_in']
        self.headers['Authorization'] = 'bearer ' + self.token

    def _make_requests(self, url):
        """Realiza requisição a API.

        Espera-se o usuário previamente autenticado. Caso o token
        seja inválido ou tenha expirado lança-se exceção.
        """
        try:
            if self.token == '' or self.token_expires_in <= 0:
                raise HeaderError
            return requests.get(url, headers=self.headers)
        except HeaderError as e:
            raise HeaderError from e
