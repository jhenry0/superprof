# superprof
Esse codigo é um webscraping que pega todos professores do site e separa em categorias separadas, salvando em TXT.
Como existem muitos dados foi utilizado Celery para que o codigo seja rodado em segundo plano, usando workers separados e fazendo programação paralela.

Necessario usar o MQRabbit para usar de servidor para o Celery ou docker usando o dockerfile!!
