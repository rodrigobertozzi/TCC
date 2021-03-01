# TCC - Rodrigo Bertozzi de Castro

Trabalho de conclusão de curso - Ciência da Computção - Pontíficia Católica de Minas Gerais - Campus Poços de Caldas

## Sobre o trabalho - Ferramenta Perspective: um estudo de caso para análise de toxicidade em tweets 
```bash
A plataforma Twitter proporciona ao usuário da rede social atualização em tempo real do que está acontecendo no mundo, como, notícias de política, músicas, futebol, opinião de outras pessoas no Twitter, entre outras coisas. Sendo assim, temos um grande volume de informações sobre cada assunto para estudar e/ou tirar as próprias conclusões.   

Neste contexto, este trabalho, consiste em mostrar as etapas de mineração de textos na rede social Twitter, conhecido como tweets, para visualizar a toxicidade dos usuários do Twitter sobre o assunto do COVID-19 e suas consequências sobre os aspectos de saúde, econômicos e sociais.  
```

## Pré requisitos

```bash
Você deve ter uma conta do Google, que lhe dá acesso ao pacote de produtos do Google, incluindo o Google Cloud.

Você também deve ter um projeto do Google Cloud para autenticar (mas não necessariamente hospedar) suas solicitações de API. Acesse o console do Google Cloud e use um projeto existente ou siga estas etapas para criar um novo:

Passo 1 - Entrar com sua conta google

Passo 2 - No link https://console.cloud.google.com
        - Clique em criar Novo Projeto
        - Nomeie seu projeto
        - Clicar no botão "Criar"
        
Para ter acesso a Perspective API, será necessaŕio preencher um formulário (https://docs.google.com/forms/d/e/1FAIpQLSdhBBnVVVbXSElby-jhNnEj-Zwpt5toQSCFsJerGfpXW66CuQ/viewform ) para poder ter acesso a API.

## Twitter Developer

Para a obtenção dos tweets, precisa-se ter autorização na plataforma Twitter Developer (https://developer.twitter.com/en):
Passo 1 - Criar uma conta 

Passo 2 - Obter as Keys para o processo de captação de tweets
```

## Gerar uma API Key 
```bash
Para generar uma chave para ter acesso a API, devemos fazer o seguinte:

Passo 1 - Entrar no link a seguir: https://console.developers.google.com/apis/credentials e clicar em " + Criar Credenciais"
Passo 2 - Escolha "Chave API" na lista de credenciais.
Passo 3 - Ver e guardar a sua Key
```

## Instalação
```bash
pip install virtualenv
virtualenv <your-env>
source <your-env>/bin/activate
<your-env>/bin/pip install google-api-python-client
```

## Python
```bash
## Utilização básica


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
