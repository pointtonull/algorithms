from collections import defaultdict


class Trie:
    def __init__(self, symbols=None):
        self.buckets = defaultdict(Trie)
        self.terminal = False
        if symbols:
            for symbol in symbols:
                self.add(symbol)

    def add(self, symbol):
        if len(symbol) == 1:
            self.buckets[symbol].terminal = True
        else:
            head, tail = symbol[0], symbol[1:]
            self.buckets[head].add(tail)

    def _all_leaves(self):
        if self.terminal:
            yield ""
        for name, node in self.buckets.items():
            for leave in node._all_leaves():
                yield name + leave

    def _query(self, query):
        if query:
            head, tail = query[0], query[1:]
            yield from self.buckets[head]._query(tail)
        else:
            yield from self._all_leaves()

    def query(self, query):
        for leave in self._query(query):
            yield query + leave


def autocomplete_system(symbols, query):
    """
    AUTOCOMPLETE SYSTEM

    This problem was asked by Twitter.
    Difficulty: Medium

    Implement an autocomplete system. That is, given a query string s and a set of all
    possible query strings, return all strings in the set that have s as aprefix. For
    example, given the query string "de" and the set of strings [dog, deer, deal],
    return [deer, deal].

    Hint: Try preprocessing the dictionary into a more efficient data structure tospeed
    up queries.
    """
    trie = Trie(symbols)
    return list(trie.query(query))
