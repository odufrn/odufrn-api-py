from .utils import *


class ODUFRNApi(unittest.TestCase):
    """Classe de teste da classe ODUFRNApi().
    """
    def setUp(self):
        """ Pesquisa as variáveis do arquivo .env e
            inicia novo objeto em todos os testes.
        """
        env = Env()
        env.read_env()
        self.api_ufrn = UfrnApi(
            env('CLIENT_ID'),
            env('CLIENT_SECRET'),
            env('X_API_KEY'),
            env('API_VERSION'))

    def test_can_print_resources(self):
        """Verifica se consegue mostrar na tela os recursos presentes na API
        """
        assert_console(self.api_ufrn.print_resources)

    def test_can_print_resource_details(self):
        """Verifica se consegue mostrar na tela os conjunto de dados de
        um recurso da API
        """
        assert_console(lambda: self.api_ufrn.print_resource_details('Pessoa'))

    def test_can_print_resource_endpoints(self):
        """Verifica se consegur mostrar na tela o conjunto de endpoins
        de um recurso específico da API
        """
        assert_console(lambda: self.api_ufrn.print_resource_endpoints(
            'Pessoa'))
