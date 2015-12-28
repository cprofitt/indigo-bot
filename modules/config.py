from ConfigParser import SafeConfigParser

# Loads and parses the configuration file for the bot. ###


class Config:

    def __init__(self, filename):
        self.conf = SafeConfigParser()
        self.file = filename
        self.load_config(self.file)

    def load_config(self, conffile):
        try:
            self.conf.read(conffile)
            return True
        except:
            return False

    def get_option(self, section, option):
        try:
            return self.conf.get(section, option)
        except Exception as err:
            return False

