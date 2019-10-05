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
            'v1')

    def test_can_print_resources(self):
        """Verifica se consegue mostrar na tela os recursos presentes na API
        """
        assert_console(self.api_ufrn.print_resources)
