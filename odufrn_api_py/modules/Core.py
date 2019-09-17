import json
import requests
from abc import ABC
from .exceptions import HeaderException


class Core(ABC):
    """Classe com os atributos e métodos responsáveis pelo
    funcionamento do pacote.
    """

    def __init__(self, client_id: str, client_secret: str,
                 x_api_key: str, version: str):
        """
        Atributos
        ---------
        client_id: str
            Chave do cliente da API da UFRN.
        client_secret: str
            Segredo do cliente da API da UFRN.
        x_api_key: str
            Hash de acesso a API da UFRN.
        version: str
        Versão da API a ser utilizada.
        """
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

    def _format_url_to_resource(self, url: str):
        """Converte a url de um recurso em um nome de recurso.
        Atributos
        ---------
        url: str
            a url que será formatada

        Retorno
        ---------
        str:
            url no formato https://api.ufrn.br/algum-resource/v1/v2/api-docs
        """
        return url.replace(self.swagger_url + '?url=', '')

    def _auth_api_request(self):
        """Realiza o processo de autenticacao dos dados do usuário.

        Primeiro realiza uma requisição post com as chaves da api,
        essa requisição retorna uma chave de acesso e quando essa
        chave irá expirar.
        """
        requisicao_token = requests.post(self.url_token)
        response = json.loads(requisicao_token.content)
        self.token = response['access_token']
        self.token_expires_in = response['expires_in']
        self.headers['Authorization'] = 'bearer ' + self.token

    def _make_requests(self, url: str) :
        """Realiza requisição a API.

        Espera-se o usuário previamente autenticado. Caso o token
        seja inválido ou tenha expirado lança-se exceção.
        """
        try:
            if self.token == '' or self.token_expires_in <= 0:
                raise HeaderException
            return requests.get(url, headers=self.headers)
        except HeaderException as e:
            raise HeaderException from e

    def _request_get(self, url: str) -> dict:
        """Realiza a requisição desejada e retorna os dados
        e o caminho formado para download.
        Parâmetros
        ----------
        url: str
            a url que se deseja realizar a requisição.
        Retorno
        ----------
        dict:
            a resposta da requisição em json (dicionário)."""
        request_get = requests.get(url)

        return request_get.json()
