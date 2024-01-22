# Fakturama Product Registration Bot - PT

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

* botcity-framework-core>=1.0.0,<2.0
* botcity-framework-web>=0.8.0,<1.0
* botcity-maestro-sdk>=0.3.3,<1.0
* google-api-python-client
* pandas
* openpyxl
* gdown
* python-environ
* loguru
* environ*

Certifique-se de instalar essas dependências antes de executar o bot.

  

## Execução

Para executar o bot, basta seguir as instruções detalhadas no código Python e garantir que todas as dependências estejam instaladas.


**Observação**: Certifique-se de ter as permissões necessárias para realizar operações no Google Drive, abrir o programa Fakturama.exe e enviar emails.



# Fakturama Product Registration Bot - EN

This is a Python automation process that registers products in the Fakturama.exe program. The bot follows a series of steps to ensure that products are added correctly and keeps a detailed record of the process.


# Bot Operation 

## Parameter Download: 

The bot starts by downloading the necessary files from **Google Drive** in the directory called **Parameters**.

The required files are **EmailList.xlsx** and **DataParameter.xlsx**.

## Date Verification: 

The bot checks the **DateParameter.xlsx** file.

If the **Date** column is filled with a specific date, it looks for the corresponding **products_inventory** file for that date in the **Input folder**.

If the Date column is **empty**, it looks for the corresponding **products_inventory** file for the **bot execution date**.

## Registration in Fakturama: 

The bot opens the **Fakturama.exe** program and selects the **“new products”** option.

For each item in the **products_inventory** file, it adds the corresponding information to the program.

## Registration and Email Sending: 

After adding each product, the bot records the product code in a **log**.

Adds **“ok” to the status column** of the file referring to that product.

Sends an email to the address listed in the **EmailList.xlsx** file with information about the registered product. In case of error, an error email is sent.

## Process Completion: 

After registering all products, the bot sends an email to the address in **EmailList.xlsx** informing the end of the process.

Attaches the process log and the **products_inventory** file with the **status field filled**.

**Uploads** the log to the output directory, inside the log folder, with the name **“LOG + Execution Date”**.

**Uploads** the **products_inventory file + Date of the DateParameter** file or **products_inventory + Execution Date** in the output directory, within the Product Inventory Files folder.

## Cleaning: 

Upon completion of the execution, the bot **deletes** all downloaded files and the log.

## Dependencies:

The project requires the following dependencies, listed in the requirements.txt file:

* botcity-framework-core>=1.0.0,<2.0 
* botcity-framework-web>=0.8.0,<1.0 
* botcity-maestro-sdk>=0.3.3,<1.0 
* google-api-python-client
* pandas 
* openpyxl 
* gdown 
* python-environ 
* loguru 
* environ

Make sure to install these dependencies before running the bot.

## Execution: 

To run the bot, simply follow the detailed instructions in the Python code and ensure that all dependencies are installed.

**Note**: Make sure you have the necessary permissions to perform operations on Google Drive, open the Fakturama.exe program, and send emails.