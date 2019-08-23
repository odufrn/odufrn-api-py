

class HeaderError(Exception):
    def __str__(self):
        return ("Algo aconteceu com o header " +
                "da sua requisição. Verifique " +
                "se seu token está ativo")
