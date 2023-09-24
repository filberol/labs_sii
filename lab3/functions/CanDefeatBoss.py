from swiplserver import PrologThread

from lab3.functions.QueryExecutor import AbstractQueryExecutor


class CanDefeatBoss(AbstractQueryExecutor):
    def __init__(self, boss_name=''):
        super().__init__()
        self.boss_name = boss_name

    def query(self):
        return f'can_defeat_boss(Class, "{self.boss_name}").'

    def execute(self, prolog: PrologThread):
        res = prolog.query(self.query())
        if not res or len(res[0]["Class"]) == 0:
            self.fail(res)
        else:
            self.success(res)

    def fail(self, res):
        print("No one can defeat this boss")

    def success(self, res):
        print(f'Classes that can defeat the boss {self.boss_name} are ', end="")
        for pair in res[:-1]:
            print(pair['Class'], end=', ')
        print(res[-1]["Class"], end='.\n')

    def init_vals(self, match):
        if len(match) != 1:
            print("Incorrect input for question")
        else:
            self.boss_name = match[0]
