try:
    import ConfigParser
except:
    import configparser as ConfigParser


class DefaultSectionHeader(object):

    def __init__(self, filename, default='[global]'):
        """
        Open a config file and insert a section header if one is missing
        """
        self.fp = open(filename)
        self.sechead = None

        if self.fp.readline().strip() != default:
            self.sechead = default + '\n'
        self.fp.seek(0)


    def readline(self):
        if self.sechead:
            try:
                return self.sechead
            finally:
                self.sechead = None
        else:
            return self.fp.readline()


class ConfigParserCeph(ConfigParser.ConfigParser):

    def optionxform(self, s):
        """
        Make config files with white space use '_'
        """
        stripped = s.strip()
        replaced = stripped.replace(' ', '_')
        return replaced

