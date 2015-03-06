class ConfigReader:
    """A configuration reader."""
    def __init__(self, filename=None):
        """Initialize the configurator with values from file, if given."""
        if filename is None:
            self.filename = None
            self.config = {}
        else:
            self.load(filename)

    def load(self, filename=None):
        """Loads configuration from file."""
        if filename:
            self.filename = filename
        elif self.filename is None:
            return None

        with open(filename) as f:
            self.config = {}
            for line in f:
                splitted = line.split(':', 1)
                key = splitted[0]
                value = splitted[1].strip()
                self.config[key] = value

    def get(self, key):
        """Returns the value of a configuration key."""
        return self.config.get(key, None)

    def set(self, key, value):
        """Sets the value for a configuration key and save it in file."""
        self.config[key] = value
        self.save()

    def save(self):
        """Saves the configuration in file."""
        if self.filename is None:
            return None

        with open(self.filename, 'w') as f:
            lines = []
            for key, value in self.config.iteritems():
                lines.append('%s: %s\n' % (key, value))
            f.writelines(lines)


def test_conf_reader():
    cr = ConfigReader('pseudo.conf')
    print cr.get('core'), cr.get('desc')
    cr.set('desc', 'something more')

if __name__ == '__main__':
    test_conf_reader()
