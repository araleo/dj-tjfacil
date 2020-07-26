Repositório com os apps em Django 3 do site [TJFácil](https://www.tjfacil.com)

- Busca: direciona o usuário aos sites dos Tribunais brasileiros, a partir de um número de processo ou de sua sigla.
- Jurimetria: busca em sentenças criminais do TJMG classificadas entre condenatórias, absolutórias e neutras.
- Notícias: links para notícias jurídicas de diferentes portais.
- Timekeep: planner que gera gráficos a partir das tarefas finalizadas.


Para instalar cada app em um projeto Django:

- copiar a pasta do app para a pasta do projeto
- no arquivo settings.py do projeto, em INSTALLED_APPS, incluir: 'busca.apps.BuscaConfig', substituindo busca pelo nome de cada app.
- no arquivo urls.py do projeto, em urlpatterns incluir: path("busca/", include("busca.urls", namespace="tj-busca")).
- python manage.py migrate
