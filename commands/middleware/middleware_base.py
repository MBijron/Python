class MiddlewareBase:
    def check(self, input_variable):
        raise NotImplementedError

    def process(self, input_variable):
        raise NotImplementedError

    def get_exception_message(self):
        return "Attribute should be of type " + self.get_type_name()

    def get_type_name(self):
        raise NotImplementedError
