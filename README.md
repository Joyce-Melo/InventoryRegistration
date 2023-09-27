O motivo pelo qual você está recebendo "00:00:00" ao imprimir a data é porque, por padrão, o Openpyxl interpreta as datas do Excel como objetos datetime.datetime, que incluem informações de hora, minuto, segundo e microssegundo, mesmo que essas informações não estejam presentes na planilha. Para obter apenas a data sem a hora, você pode usar o método date() para converter o objeto datetime em um objeto date.

funcionalidades semelhantes a Work Queue do Blue Prism usando bibliotecas e ferramentas disponíveis na linguagem Python. Aqui estão algumas alternativas e abordagens que você pode considerar:

Banco de Dados ou Armazenamento em Nuvem: Você pode usar um banco de dados (como SQLite, MySQL, PostgreSQL, etc.) ou armazenamento em nuvem (como Amazon S3, Google Cloud Storage, etc.) para armazenar e gerenciar itens em uma fila. Você pode criar tabelas ou contêineres dedicados para armazenar esses itens e implementar as operações de adição, remoção e processamento de itens na fila usando consultas SQL ou APIs de armazenamento em nuvem.

Bibliotecas de Filas: Existem bibliotecas em Python que oferecem recursos de filas para gerenciar tarefas em um estilo semelhante a uma fila de trabalho. Duas bibliotecas populares são Celery e RQ (Redis Queue). Essas bibliotecas permitem que você defina tarefas, as enfileire e as processe em segundo plano de maneira escalável e distribuída.

Gerenciadores de Tarefas: Você pode criar seu próprio sistema de gerenciamento de tarefas simples usando threads ou processos em Python. Por exemplo, você pode criar uma lista compartilhada (fila) de tarefas a serem processadas e usar threads ou processos para retirar tarefas da fila e processá-las.

Bibliotecas de Mensagens: Você pode usar bibliotecas de mensagens como RabbitMQ ou Apache Kafka para implementar uma fila de mensagens. Essas ferramentas permitem que você crie sistemas de mensagens distribuídas e pode ser uma maneira poderosa de gerenciar fluxos de trabalho em Python.


- Adicionar Status de Ok se processado
- Enviar email - Ok

- TO DO
    - Enviar email de erro
    - Enviar log e planilha final