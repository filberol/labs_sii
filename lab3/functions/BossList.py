from swiplserver import PrologThread

from lab3.functions.QueryExecutor import AbstractQueryExecutor


class BossList(AbstractQueryExecutor):
    def __init__(self, boss_name=''):
        super().__init__()
        self.boss_name = boss_name

    def query(self):
        return f'bosses_in_act(BossList, "{self.boss_name}").'

    def execute(self, prolog: PrologThread):
        res = prolog.query(self.query())
        if not res or len(res[0]["BossList"]) == 0:
            self.fail(res)
        else:
            self.success(res)

    def fail(self, res):
        print("No bosses in this act")

    def success(self, res):
        print(f'Bosses in act {self.boss_name} are ', end="")
        for boss in res[0]['BossList'][:-1]:
            print(boss, end=', ')
        print(res[0]['BossList'][-1], end='.\n')

    def init_vals(self, match):
        if len(match) != 1:
            print("Incorrect input for question")
        else:
            self.boss_name = match[0]
