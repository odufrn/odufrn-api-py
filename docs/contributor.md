# Como contribuir?

Esse documento é destinado para os desenvolvedores que desejarem contribuir com o projeto.

## Chaves de acesso a API
Para utilização e testes desse projeto é necessário solicitar suas credenciais para ter acesso a API da UFRN. Para mais informações sobre seu cadastro, consulte a documentação clicando [aqui](https://api.ufrn.br/documentacao.html#cadastro).

## Requerimentos

- [Requests](https://pypi.org/project/requests/)
- [Environs](https://pypi.org/project/environs/)

### Como usar o pacote `Environs`
Para a utilização desse pacote é necessário a criação de um arquivo `.env` no qual vai conter suas chaves de acesso a API.

Exemplo:
```sh
export CLIENT_ID=sua-chave-id
export CLIENT_SECRET=sua-chave-secreta
export X_API_KEY=sua-chave-de-acesso
export API_VERSION=v1
```

OBS: A versão depende exclusivamente do [site oficial da API](https://api.ufrn.br/).

Essas chaves serão requeridas para a execução dos testes através do código abaixo

```python
from environs import Env

def setUp(self):
    """ Inicia novo objeto em todos os testes."""
    env = Env()
    env.read_env()
    self.api_ufrn = UfrnApi(
        env("CLIENT_ID"),
        env("CLIENT_SECRET"),
        env("X_API_KEY"),
        env("API_VERSION"))
```