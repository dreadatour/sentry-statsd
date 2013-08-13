# coding: utf-8
"""
sentry_statsd.forms
"""
from django import forms


class StatsdOptionsForm(forms.Form):
    host = forms.CharField(
        max_length=255,
        help_text='StatsD host (for example: "localhost")'
    )
    port = forms.IntegerField(
        max_value=65535,
        help_text='StatsD port (for example: "8125")'
    )
    prefix = forms.CharField(
        max_length=255,
        help_text='Prefix for Sentry metrics in StatsD (for example: "sentry")'
    )
    add_loggers = forms.BooleanField(
        required=False,
        help_text='Add loggers names to StatsD metrics (otherwise only project names will be used)'
    )
    track_only_new = forms.BooleanField(
        required=False,
        help_text='Add statsd count to only new exceptions')
