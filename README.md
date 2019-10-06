## OPEN DATA UFRN API WRAPPER

<a href="https://travis-ci.org/odufrn/odufrn-api-py">
  <img alt="Build" src="https://travis-ci.org/odufrn/odufrn-api-py.svg?branch=master">
</a>
<a href="https://github.com/odufrn/odufrn-api-py/blob/master/LICENSE">
  <img alt="License" src="https://img.shields.io/badge/license-MIT-brightgreen.svg">
</a>

Implementação de uma interface pythonica para uso da [API da UFRN](https://api.ufrn.br/). 

## Instalação
O repositório ainda não está no pipy, sua instalação local pode ser feita com:
```
pip install -e .
```

## Guia de uso
```python
from odufrn_api_py import UfrnApi
wrapper_api = UfrnApi('client-id', 'client-secret', 'x-api-key', 'api-version')
```

## Métodos

| Método | Descrição |
| ------ | --------- |
| `print_resources` | Imprime no terminal todos os serviços disponibilizados pela API |
| `print_resource_details` | Imprime no terminal todos os conjuntos de dados de um serviço específico da API |
| `print_resource_endpoints` | Imprime no terminal todos os endpoints que um serviço da API dispões |
