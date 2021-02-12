class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self.peek_value = None

    def peek(self):
        if self.peek_value is None:
            self.peek_value = self.iterator.next()
        return self.peek_value

    def next(self):
        if self.peek_value is not None:
            peek_value = self.peek_value
            self.peek_value = None
            return peek_value
        return self.iterator.next()

    def hasNext(self):
        return self.peek_value is not None or self.iterator.hasNext()
