sentry-statsd
=============

An extension for Sentry to send errors metrics to StatsD.

Install
-------

Install the package with ``pip``::

    pip install -e git+git@github.com:dreadatour/sentry-statsd.git


Configuration
-------------

Go to your project's configuration page (Projects -> [Project]) and select the
"StatsD" tab. Enter the StatsS host, port and prefix for metrics:

.. image:: https://github.com/dreadatour/sentry-statsd/raw/master/docs/images/options.png
