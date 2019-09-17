from .utils import *


class ODUFRNApi(unittest.TestCase):
    """Classe de teste da classe ODUFRNApi().
    """
    def setUp(self):
        """Inicia novo objeto em todos os testes.
        """
        self.api_ufrn = ODUFRNApi()
