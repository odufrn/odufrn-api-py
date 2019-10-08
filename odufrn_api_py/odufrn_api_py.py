from .modules.Core import Core


class UfrnApi(Core):
    """Classe que reune todos os módulos do pacote.
    """
    def __init__(self, client_id: str, client_secret: str,
                 x_api_key: str, version: str):
        """Construtor do pacote. Passa atributos pra classe Env.
        """
        super().__init__(client_id, client_secret, x_api_key, version)

    def __url__(self, name: str) -> str:
        """Retorna a url de acordo com o nome do recurso passado
        pelo usuário.

        Parâmetros
        ----------
        name: str
            Nome do recurso utiliado para recuperar
            a url desse memso recurso.
        """
        for resource in self._request_get(self.url_base + 'documentacao'):
            if resource['name'] == name:
                return self._format_url_to_resource(resource['url'])

    def print_resources(self) -> None:
        """Imprime na tela os recursos presentes na API.
        """
        for resource in self._request_get(self.url_base + 'documentacao'):
            print(
                "Nome: {},\nUrl: {},\n".format(
                    resource['name'],
                    self._format_url_to_resource(resource['url']),
                )
            )

    def print_resource_details(self, name: str) -> None:
        """ Imprime na tela as categorias de dados
        presentes no recurso da API escolhido pelo usuário.

        Parâmetros
        ----------
        name: str
            Nome do recurso utiliado para recuperar os
            datasets e descrição dos mesmos.
        """

        print("Conjuntos de dados do serviço {}.".format(name))
        for sub_resource in self._request_get(self.__url__(name))['tags']:
            print(
                "Nome: {}\nDescription: {}\n".format(
                    sub_resource['name'],
                    sub_resource['description']
                )
            )

    def print_resource_endpoints(self, name: str) -> None:
        """ Imprime na tela todos os endpoints que o serviço
        específico oferece.

        Parâmetros
        ----------
        name: str
            Nome do recurso que será usado para recuperar os
            endpoints.
        """
        print("Conjunto de endpoints do serviço {}.".format(name))
        paths = self._request_get(self.__url__(name))['paths']

        # Imprimindo Endpoint e Summary na tela
        for endpoint in paths:
            print(
                "Endpoint: {}\nSummary: {}".format(
                    str(endpoint),
                    paths[str(endpoint)]['get']['summary']
                )
            )

            # Imprimindo os parâmetros do endpoint específico
            print('Parameters: [', end='')
            endpoint_get = paths[str(endpoint)]['get']
            # Verificando se o endpoint possui parâmetros
            if 'parameters' in endpoint_get:
                for parameter in endpoint_get['parameters']:
                    # Verificando se é ultimo parâmetro
                    if parameter == endpoint_get['parameters'][-1]:
                        print(
                            '{}'.format(parameter['name']),
                            end=''
                        )
                    else:
                        print(
                            '{}, '.format(parameter['name']),
                            end=''
                        )
            else:
                print("No parameters", end='')

            print(']\n')
