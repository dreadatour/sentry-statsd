# coding: utf-8
"""
sentry_statsd.plugin
"""
import statsd
from sentry.plugins import Plugin

import sentry_statsd
from sentry_statsd.forms import StatsdOptionsForm


class StatsdPlugin(Plugin):
    """
    Sentry plugin to send errors stats to StatsD.
    """
    author = 'Vladimir Rudnyh'
    author_url = 'https://github.com/dreadatour/sentry-statsd'
    version = sentry_statsd.VERSION
    description = 'Send errors stats to StatsD.'
    slug = 'statsd'
    title = 'StatsD'
    conf_key = slug
    conf_title = title
    resource_links = [
        ('Source', 'https://github.com/dreadatour/sentry-statsd'),
        ('Bug Tracker', 'https://github.com/dreadatour/sentry-statsd/issues'),
        ('README', 'https://github.com/dreadatour/sentry-statsd/blob/master/README.rst'),
    ]
    project_conf_form = StatsdOptionsForm

    def is_configured(self, project, **kwargs):
        """
        Check if plugin is configured.
        """
        params = self.get_option
        return bool(params('host', project) and params('port', project))

    def post_process(self, group, event, is_new, is_sample, **kwargs):
        """
        Process error.
        """
        if not self.is_configured(group.project):
            return

        host = self.get_option('host', group.project)
        port = self.get_option('port', group.project)
        prefix = self.get_option('prefix', group.project)
        add_loggers = self.get_option('add_loggers', group.project)
        track_only_new = self.get_option('track_only_new', False)

        metric = []
        metric.append(group.project.slug.replace('-', '_'))
        if add_loggers:
            metric.append(group.logger)
        metric.append(group.get_level_display())

        client = statsd.StatsClient(host, port, prefix=prefix)

        if not track_only_new or (is_new and track_only_new):
            client.incr('.'.join(metric))
