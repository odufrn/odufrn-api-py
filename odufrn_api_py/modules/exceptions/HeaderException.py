class HeaderException(Exception):
    """Exception emitida quando acontece algum erro
    no header da requisição.
    """
    def __str__(self):
        return ("Algo aconteceu com o header " +
                "da sua requisição. Verifique " +
                "se seu token está ativo")
