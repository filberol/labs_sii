from swiplserver import PrologThread

from lab3.functions.QueryExecutor import AbstractQueryExecutor


class ClassPlace(AbstractQueryExecutor):
    def __init__(self, class_name=''):
        super().__init__()
        self.class_name = class_name

    def query(self):
        return f'available_classes_in_act(Class, "{self.class_name}").'

    def execute(self, prolog: PrologThread):
        res = prolog.query(self.query())
        if not res or len(res[0]["Class"]) == 0:
            self.fail(res)
        else:
            self.success(res)

    def fail(self, res):
        print("No available classes in this act")

    def success(self, res):
        print(f'Classes for {self.class_name} are ', end="")
        for pair in res[:-1]:
            print(pair['Class'], end=', ')
        print(res[-1]["Class"], end='.\n')

    def init_vals(self, match):
        if len(match) != 1:
            print("Incorrect input for question")
        else:
            self.class_name = match[0]
