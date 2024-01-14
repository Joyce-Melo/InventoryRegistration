# Fakturama Product Registration Bot

Este é um processo de automação em Python que realiza o registro de produtos no programa Fakturama.exe. 
O bot segue uma série de etapas para garantir que os produtos sejam adicionados corretamente e mantém um registro detalhado do processo.


# Funcionamento do Bot

## Download de Parâmetros:

O bot inicia baixando os arquivos necessários do **Google Drive** no diretório chamado **Parameters**.

Os arquivos necessários são **EmailList.xlsx** e **DataParameter.xlsx**.

## Verificação da Data:

O bot verifica o arquivo **DateParameter.xlsx**.

Se a coluna **Date** estiver preenchida com uma data específica, ele procura pelo arquivo **products_inventory** correspondente a essa data na pasta **Input**.

Se a coluna Date estiver vazia, ele busca pelo arquivo **products_inventory** correspondente à data de execução do bot.

## Registro no Fakturama:

  

O bot abre o programa **Fakturama.exe** e seleciona a opção **"new products"**.

Para cada item no arquivo **products_inventory**, ele adiciona as informações correspondentes ao programa.

## Registro e Envio de Emails:

Após adicionar cada produto, o bot registra o código do produto em um **log**.

Adiciona **"ok" na coluna status** do arquivo referente a esse produto.

Envia um email para o endereço listado no arquivo **EmailList.xlsx** com informações sobre o produto registrado. Em caso de erro, um email de erro é enviado.

## Finalização do Processo:
  
Após registrar todos os produtos, o bot envia um email para o endereço no **EmailList.xlsx** informando o final do processo.

Anexa o log do processo e o arquivo **products_inventory** com o campo **status** preenchido.

Faz upload do log no diretório output, dentro da pasta log, com o nome **"LOG + Data da Execução"**.

Faz upload do arquivo **products_inventory + Data do arquivo DateParameter** ou **products_inventory +Data da Execução** no diretório output, dentro da pasta Product Inventory Files.

## Limpeza:

Ao finalizar a execução, o bot **exclui** todos os arquivos baixados e o log.

## Dependências

O projeto requer as seguintes dependências, listadas no arquivo requirements.txt:

*botcity-framework-core>=1.0.0,<2.0
botcity-framework-web>=0.8.0,<1.0
botcity-maestro-sdk>=0.3.3,<1.0
pandas
openpyxl
gdown
python-environ
loguru
environ*

Certifique-se de instalar essas dependências antes de executar o bot.

  

## Execução

Para executar o bot, basta seguir as instruções detalhadas no código Python e garantir que todas as dependências estejam instaladas.


**Observação**: Certifique-se de ter as permissões necessárias para realizar operações no Google Drive, abrir o programa Fakturama.exe e enviar emails.