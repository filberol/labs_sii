from swiplserver import PrologThread

from lab3.functions.QueryExecutor import AbstractQueryExecutor


class UnlockedAct(AbstractQueryExecutor):
    def __init__(self, act=''):
        super().__init__()
        self.act = act

    def query(self):
        return f'unlocked_acts_after_boss(Act, "{self.act}").'

    def execute(self, prolog: PrologThread):
        res = prolog.query(self.query())
        if not res or len(res[0]["Act"]) == 0:
            self.fail(res)
        else:
            self.success(res)

    def fail(self, res):
        print(f"No acts unlocked after {self.act}")

    def success(self, res):
        print(f'Act after {self.act} is ', end="")
        print(f'{res[0]["Act"]}.')

    def init_vals(self, match):
        if len(match) != 1:
            print("Incorrect input for question")
        else:
            self.act = match[0]
