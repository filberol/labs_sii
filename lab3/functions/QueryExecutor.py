from swiplserver import PrologThread


class AbstractQueryExecutor:
    def __init__(self):
        pass

    def execute(self, prolog: PrologThread):
        pass

    def fail(self, res):
        pass

    def success(self, res):
        pass

    def query(self):
        pass

    def init_vals(self, match):
        pass
