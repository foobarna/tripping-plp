class ConfigReaderException(Exception):
    """Exception class for ConfigReader."""
    pass


class ConfigReader:
    """A configuration reader."""
    def __init__(self, filename, load=True):
        """Initialize the configurator with values from file, if given."""
        if filename is None:
            raise ConfigReaderException("No file given for loading the configuration.")

        self.filename = filename
        self.config = {}
        if load:
            self.load()

    def load(self):
        """Loads configuration from file."""
        with open(self.filename) as f:
            self.config = {}
            for line in f:
                splitted = line.split(':', 1)
                key = splitted[0]
                value = splitted[1].strip()
                self.config[key] = value

    def get(self, key):
        """Returns the value of a configuration key."""
        return self.config.get(key, None)

    def set(self, key, value, save=False):
        """Sets the value for a configuration key and save it in file."""
        if key is None or value is None:
            raise ConfigReaderException("key or value can not be None.")

        self.config[key] = value
        if save:
            self.save()

    def save(self):
        """Saves the configuration in file."""
        with open(self.filename, 'w') as f:
            lines = []
            for key, value in self.config.iteritems():
                lines.append('%s: %s\n' % (key, value))
            f.writelines(lines)


def test_conf_reader():
    cr = ConfigReader()
    print cr.get('core'), cr.get('desc')
    cr.set('desc', 'something more555S')

if __name__ == '__main__':
    test_conf_reader()
