class Logger:
    """A minimalistic logger."""
    CRITICAL = 50
    ERROR = 40
    WARNING = 30
    INFO = 20
    DEBUG = 10
    NOTSET = 0

    levelNames = {
        CRITICAL: 'CRITICAL',
        ERROR: 'ERROR',
        WARNING: 'WARNING',
        INFO: 'INFO',
        DEBUG: 'DEBUG',
        NOTSET: 'NOTSET',
        'CRITICAL': CRITICAL,
        'ERROR': ERROR,
        'WARNING': WARNING,
        'INFO': INFO,
        'DEBUG': DEBUG,
        'NOTSET': NOTSET,
    }

    def __init__(self, level=CRITICAL, enabled_levels=None, filename=None):
        """Creates the logger with the monitoring level and desire levels."""
        self.level = level
        self.filename = filename
        if enabled_levels is None:
            self.enabledLevels = {key: True for key, value in Logger.levelNames.iteritems() if isinstance(key, str)}
        else:
            self.enabledLevels = {key: True for key, value in enabled_levels.iteritems() if isinstance(key, str) and key in Logger.levelNames}

    def log(self, level, msg, *args, **kwargs):
        """Logs a message for the given level, if monitored."""
        if self.level_enabled(level):
            self.print_log(level, msg, *args, **kwargs)

    def level_enabled(self, level):
        """Checks if the given level is enabled and monitored by the logger."""
        return level <= self.level and self.enabledLevels.get(Logger.levelNames[level], False)

    def print_log(self, level, msg, *args, **kwargs):
        """Format and print the log message."""
        line = "Logger::%s::%s" % (Logger.levelNames[level], msg.format(*args, **kwargs))
        print line
        if self.filename:
            with open(self.filename, 'a') as f:
                f.write("%s\n" % line)

    def set_level(self, level):
        """Set the monitoring level of logger."""
        self.level = level

    def enable_level(self, level):
        """Enable a level for monitoring."""
        self.enabledLevels[Logger.levelNames[level]] = True

    def disable_level(self, level):
        """Disable a level for monitoring."""
        self.enabledLevels[Logger.levelNames[level]] = False


def test_logger():
    l = Logger()
    l.log(Logger.ERROR, "Some {} for error", "message")

    l.disable_level(Logger.INFO)
    l.log(Logger.INFO, "Some {} for info that will not be displayed", "message")

    l.enable_level(Logger.INFO)
    l.log(Logger.INFO, "Display {level_name} messages.", level_name="info")

    l.set_level(Logger.WARNING)
    l.log(Logger.ERROR, "{level_name} messages will not be displayed.", level_name="error")

if __name__ == "__main__":
    test_logger()
