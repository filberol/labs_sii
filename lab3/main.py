import os

import swiplserver
from swiplserver import PrologMQI
from functions import *
import re

PROLOG_DB_PATH = os.path.abspath("./lab1/lab1_sii.pl").replace('\\','/')

prolog_queries_regex = {
    r'What are the classes for act (.+)\?': ClassPlace.ClassPlace(),
    r'Bosses in act (.+)': BossList.BossList(),
    r'Act unlocked after boss (.+)': UnlockedAct.UnlockedAct(),
    r'Who can defeat the boss (.+)\?': CanDefeatBoss.CanDefeatBoss()
}


def init_query_function(query: str) -> QueryExecutor.AbstractQueryExecutor | None:
    for pattern in prolog_queries_regex:
        match = re.match(pattern, query, re.IGNORECASE)
        if match is None:
            continue
        else:
            function: QueryExecutor.AbstractQueryExecutor = prolog_queries_regex[pattern]
            function.init_vals(match.groups())
            return function
    return None


if __name__ == '__main__':
    with PrologMQI() as mqi:
        with mqi.create_thread() as prolog:
            path = swiplserver.create_posix_path(
                PROLOG_DB_PATH
            )
            prolog.query(f'consult("{PROLOG_DB_PATH}")')
            while True:
                input_query = input('$ ')
                if input_query == 'exit':
                    exit(0)
                executor = init_query_function(input_query)
                if executor is not None:
                    executor.execute(prolog)
                else:
                    print("Incorrect input")
