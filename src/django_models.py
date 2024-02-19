import os

from django import setup as django_setup
from django.conf import settings as django_settings
from django.db import models

django_settings.configure(
    DEBUG=True,
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'database.db',
            'USER': '',
            'PASSWORD': '',
            'HOST': '',
            'PORT': '',
        }
    })
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django_setup()


class ClientInfo(models.Model):
    info = models.CharField(max_length=256, null=False, blank=False)

    class Meta:
        managed = False
        db_table = 'clients_info'
        app_label = 'fast_api'


class Client(models.Model):
    client_name = models.CharField(max_length=256, null=False, blank=False)
    client_info = models.ForeignKey(
        ClientInfo,
        db_column='client_info',
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )

    class Meta:
        managed = False
        db_table = 'clients'
        app_label = 'fast_api'


class Endpoint(models.Model):
    endpoint_name = models.CharField(max_length=256, null=False, blank=False)

    class Meta:
        managed = False
        db_table = 'endpoints'
        app_label = 'fast_api'


class EndpointStates(models.Model):
    client = models.ForeignKey(Client, on_delete=models.PROTECT, null=False, blank=False)
    endpoint = models.ForeignKey(Endpoint, on_delete=models.PROTECT, null=False, blank=False)
    state_name = models.CharField(max_length=256)
    state_reason = models.CharField(max_length=256)
    state_start = models.CharField(max_length=256)
    state_end = models.CharField(max_length=256)
    state_id = models.CharField(max_length=256)
    group_id = models.CharField(max_length=256)
    reason_group = models.CharField(max_length=256)
    info = models.JSONField(default={})

    class Meta:
        managed = False
        db_table = 'endpoint_states'
        app_label = 'fast_api'
