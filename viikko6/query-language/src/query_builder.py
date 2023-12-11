from matchers import *

class QueryBuilder:
    def __init__(self, query = All()):
        self.query = query

    def playsIn(self, team):
        return QueryBuilder(And(self.query, PlaysIn(team)))
        
    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(self.query, HasAtLeast(value, attr)))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(self.query, HasFewerThan(value, attr)))
            
    def oneOf(self, *matchers):
        return QueryBuilder(Or(*matchers))

    def build(self):
        return self.query
    
