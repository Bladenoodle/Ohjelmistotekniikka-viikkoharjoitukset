from matchers import (
    All,
    And,
    Or,
    PlaysIn,
    HasAtLeast,
    HasFewerThan
)


class QueryBuilder:
    def __init__(self, matcher=All()):
        self._matcher = matcher

    # --- TEHTÄVÄ 5: AND-peräkkäin ketjutettavat ehdot ---

    def plays_in(self, team):
        return QueryBuilder(And(self._matcher, PlaysIn(team)))

    def has_at_least(self, value, attr):
        return QueryBuilder(And(self._matcher, HasAtLeast(value, attr)))

    def has_fewer_than(self, value, attr):
        return QueryBuilder(And(self._matcher, HasFewerThan(value, attr)))


    def one_of(self, *queries):
        """
        queries = lista QueryBuilder-olioita
        Niiden matcherit täytyy hakea .build():llä
        """
        matchers = [query.build() for query in queries]
        return QueryBuilder(Or(*matchers))

    def build(self):
        return self._matcher
