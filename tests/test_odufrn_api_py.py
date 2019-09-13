from .utils import *


class ODUFRNApi(Unittest.Test):
    def setUp(self):
        """Inicia novo objeto em todos os testes."""
        self.api_ufrn = ODUFRNApi()
