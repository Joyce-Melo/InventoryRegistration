#Log -> Registra eventos que já aconteceu no sistema
#Python tem uma biblioteca padrão de loggin

from logging import error, warning, debug, info, critical
from logging import basicConfig
from logging import INFO

# Temos como níveis os DEBUG->INFO->WARNING->ERROR->CRITICAL, estamos indo do mais "leve" ao mais grave
# basicConfig(level=INFO) # Aqui estamos especificando o nivel que queremos, como aqui está como INFO, iremos imprimir no console logs do nível INFO para frente. Ou seja, todos serão impressos exceto o DEBUG, que está um nível atrás de INFO

basicConfig(level=INFO)

warning("Algo de errado não está certo")
error('Ihhh deu ruim')

#Vídeo pausado aos 32:31