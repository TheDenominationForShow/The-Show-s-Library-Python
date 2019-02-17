import logging
import configparser
import os
# init log config
log = logging.getLogger()
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
log.basicConfig(filename='my.log', level=logging.DEBUG, format=LOG_FORMAT)

# init config file
config = configparser.RawConfigParser()
if os.path.exists('./finder.cfg') is False:
    with open('./finder.cfg','w') as f:
        pass
config.read('./finder.cfg')
config.add_section('DataBaseInfo')
