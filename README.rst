sentry-statsd
=============

An extension for Sentry to send errors metrics to StatsD.

Install
-------

Install the package with ``pip``::

    pip install sentry-statsd


Configuration
-------------

Go to your project's configuration page (Projects -> [Project]) and select the
"StatsD" tab. Enter the StatsS host, port and prefix for metrics:

.. image:: https://github.com/dreadatour/sentry-statsd/raw/master/docs/images/options.png


After installing and configuring, make sure to restart sentry-worker for the
changes to take into effect.
