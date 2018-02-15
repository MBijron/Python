import time


class CommandLineUtils:
    @staticmethod
    def prompt_for_yes_no(message) -> bool:
        response = input(message + " (Y,N)")
        if response is "N" or response is "n":
            return False
        elif response is "Y" or response is "y":
            return True
        else:
            time.sleep(100)
            print("Input was incorrect. Please choose Y or N")
            CommandLineUtils.prompt_for_yes_no(message)
