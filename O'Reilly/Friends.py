class Friends:
    def __init__(self, connections):
        self._connections = set(map(frozenset, connections))

    def add(self, connection):
        if connection in self._connections:
            return False
        else:
            self._connections.add(frozenset(connection))
            return True

    def remove(self, connection):
        try:
            self._connections.remove(connection)
        except KeyError:
            return False
        else:
            return True

    def names(self):
        return {
            name
            for connection in self._connections
            for name in connection
        }

    def connected(self, name):
        return {
            friend
            for connection in self._connections if name in connection
            for friend in connection if name != friend
        }


if __name__ == '__main__':
    letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    digit_friends = Friends([{"1", "2"}, {"3", "1"}])
    assert letter_friends.add({"c", "d"}) is True, "Add"
    assert letter_friends.add({"c", "d"}) is False, "Add again"
    assert letter_friends.remove({"c", "d"}) is True, "Remove"
    assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
    assert letter_friends.names() == {"a", "b", "c"}, "Names"
    assert letter_friends.connected("d") == set(), "Non connected name"
    assert letter_friends.connected("a") == {"b", "c"}, "Connected name"
    print('Done!')
