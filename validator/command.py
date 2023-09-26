from exception.command import InvalidCommandError


def check_command(actionable: str):
    if not actionable or len(actionable) == 0:
        raise InvalidCommandError("No item provided after action!")