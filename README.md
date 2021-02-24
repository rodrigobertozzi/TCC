# TCC - Rodrigo Bertozzi de Castro

Trabalho de conclusão de curso - Ciência da Computção - Pontíficia Católica de Minas Gerais - Campus Poços de Caldas

## Pré requisitos

```bash
Você deve ter uma conta do Google, que lhe dá acesso ao pacote de produtos do Google, incluindo o Google Cloud.

Você também deve ter um projeto do Google Cloud para autenticar (mas não necessariamente hospedar) suas solicitações de API. Acesse o console do Google Cloud e use um projeto existente ou siga estas etapas para criar um novo:

Passo 1 - Entrar com sua conta google

Passo 2 - No link https://console.cloud.google.com
        - Clique em criar Novo Projeto
        - Nomeie seu projeto
        - Clicar no botão "Criar"
        
Para ter acesso a Perspective API, será necessaŕio preencher um formulário ( https://docs.google.com/forms/d/e/1FAIpQLSdhBBnVVVbXSElby-jhNnEj-Zwpt5toQSCFsJerGfpXW66CuQ/viewform ) para poder ter acesso a API.
```

## Generar uma API Key 
```bash
Para generar uma chave para ter acesso a API, devemos fazer o seguinte:

Passo 1 - Entrar no link a seguir: https://console.developers.google.com/apis/credentials e clicar em " + Criar Credenciais"
Passo 2 - Escolha "Chave API" na lista de credenciais.
Passo 3 - Ver e guardar a sua Key
```

## Python
```bash
Aqui está um exemplo de solicitação e resposta usando a versão Python das bibliotecas cliente da API do Google.
```

## Instalação
```bash
pip install virtualenv
virtualenv <your-env>
source <your-env>/bin/activate
<your-env>/bin/pip install google-api-python-client
```


## Utilização

```bash
from googleapiclient import discovery

API_KEY='replace-this-with-your-API-key'

# Generates API client object dynamically based on service name and version.
service = discovery.build('commentanalyzer', 'v1alpha1', developerKey=API_KEY)

analyze_request = {
  'comment': { 'text': 'friendly greetings from python' },
  'requestedAttributes': {'TOXICITY': {}}
}

response = service.comments().analyze(body=analyze_request).execute()

import json
print json.dumps(response, indent=2)

```

## License
[MIT](https://choosealicense.com/licenses/mit/)
