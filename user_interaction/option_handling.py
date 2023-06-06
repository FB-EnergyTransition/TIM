from user_interaction import get_user_input_params, input_validation
import user_interaction.welcome_and_end

pr = user_interaction.welcome_and_end.Printer()


class OptionHandler:

    def __init__(self, params):
        self.iv = user_interaction.input_validation.InputValidator()
        self.params = params

    def get_option(self):
        return input()

    def execute_option_and_get_args(self, option):
        args = []
        if self.iv.validate_option(option):
            if option == "1":
                self.params.get_parameters()
            elif option == "2":
                pr.print_csv_requirements()
                pr.print_options()
                self.execute_option_and_get_args(self.get_option())
        else:
            pr.print_invalid_option()
            pr.print_options()
            self.iv.validate_option(self.get_option())
        return args
