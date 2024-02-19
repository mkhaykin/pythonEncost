Полагаю в исходном коде были нарочно допущены некоторые неточности: 

- в schema.py в строке `import datetime` ожидалось `from datetime import datetime`

- так же в моделях исправил `on_delete=models.PROTECT()` на `on_delete=models.PROTECT`

- в определении class EndpointStates исправил
`db_table = 'endpoints_states'` на `db_table = 'endpoint_states'` 

- в определении class Client исправил 
`client_info = models.ForeignKey(ClientInfo, on_delete=models.PROTECT, null=True, blank=True)`
на 
`client_info = models.ForeignKey(ClientInfo, db_column='client_info', on_delete=models.PROTECT, null=True, blank=True)`

В django_models.py внес настройки для работы с БД. Стоило, конечно, в отдельный файл. 
