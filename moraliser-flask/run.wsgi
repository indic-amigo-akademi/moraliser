#!/usr/bin/python
import sys, os
import logging

logging.basicConfig(stream=sys.stderr)
logging.info(os.path.dirname(sys.executable))
sys.path.insert(0, "/var/www/html/moraliser")

from chat import create_app

application = create_app()
