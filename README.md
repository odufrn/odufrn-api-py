## OPEN DATA UFRN API WRAPPER

Implementação de uma interface pythonica para uso da [API da UFRN](https://api.ufrn.br/). 

## Instalação
O repositório ainda não está no pipy, sua instalação local pode ser feita com:
```
pip install -e .
```

## Guia de uso
```
from odufrn_api_py import UfrnApi
wrapper_api = UfrnApi('client-id', 'client-secret', 'x-api-key', 'api-version')
```

## Métodos

| Método | Descrição |
| ------ | --------- |
| print_resources | Imprime no terminal todos os serviços disponibilizados pela API |
