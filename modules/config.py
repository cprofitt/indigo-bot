from ConfigParser import SafeConfigParser
import logging

# Loads and parses the configuration file for the bot. ###


class Config:

    def __init__(self, filename):
        self.conf = SafeConfigParser()
        self.file = filename
        self.load_config(self.file)
        logging.basicConfig(filename='log.log', level=logging.DEBUG)

    def load_config(self, conffile):
        try:
            self.conf.read(conffile)
            return True
        except:
            logging.error('Error loading configuration file!')
            return False

    def get_option(self, section, option):
        try:
            return self.conf.get(section, option)
        except Exception as err:
            logging.error("Can\'t read configuration option: %s" % (err))
            return False

    def set_option(self, section, option, value):
        try:
            self.conf.set(section, option, value)
            with open(self.file, 'wb') as configfile:
                self.conf.write(configfile)
            return True
        except Exception as err:
            logging.error('Unable to set configuration option: %s' % (err))
            return False

    def get_int(self, section, option):
        try:
            return self.conf.getint(section, option)
        except Exception as err:
            logging.error("Can\'t read configuration option: %s" % (err))
            return False
