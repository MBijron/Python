class CommandLineUtils:
    @staticmethod
    def prompt_for_yes_no(message):
        response = input(message + " (Y,N)")
        if response is "N" or response is "n":
            return False
        elif response is "Y" or response is "y":
            return True
        else:
            print("Input was incorrect. Please choose Y or N")
            CommandLineUtils.prompt_for_yes_no(message)
