#Log -> Registra eventos que já aconteceu no sistema
#Python tem uma biblioteca padrão de loggin

from logging import error, warning, debug, info, critical
from logging import basicConfig
from logging import INFO, DEBUG, ERROR, WARNING
# Na lib de logging, temos os handlers, que é a forma como aquele log é registrado, então um handler que escreve nos arquivos, no terminal, manda email, escreve mensagem via socket e por aí vai.
# Aqui iremos importar 2 o stream (que o que escreve na saída, aka terminal) e o File handler que é o que escreve no arquivo
from logging import FileHandler, StreamHandler

# Temos como níveis os DEBUG->INFO->WARNING->ERROR->CRITICAL, estamos indo do mais "leve" ao mais grave
# basicConfig(level=INFO) # Aqui estamos especificando o nivel que queremos, como aqui está como INFO, iremos imprimir no console logs do nível INFO para frente. Ou seja, todos serão impressos exceto o DEBUG, que está um nível atrás de INFO

basicConfig(
    level=INFO,
    # filename='batatinha.txt', #Onde qro salvar esse log, para não ficar só na saída do sistema
    # filemode='a', #Adiciono novas linhas nesse arquivo, ao invés de criar um novo a cada execução, esse a é de append
    encoding='utf-8',
    format='%(asctime)s:%(levelname)s:%(message)s',
    handlers=[FileHandler('LOG.txt', 'a'), #Escreve no arquivo
              StreamHandler() #Escreve no Shell
              ]
)

def setInfoLog(message):
    info(message)

def mainLog(message):
    setInfoLog(message)