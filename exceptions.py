class Impossible(Exception):
    """Exception raised when an action is impossible to be performed.

    The reason is given as an error message.
    """


class QuitWithoutSaving(SystemExit):
    """Can be raised to exit the game without automatically saving."""
