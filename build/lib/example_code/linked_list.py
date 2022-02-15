import sys
"""A simple implementation of a linked list."""


class Link:
    """A link in a linked list.

    Parameters
    ----------
    value :
        The value to be stored in the link.
    next : Link
        The next link in the list.
    """

    def __init__(self, value, next=None):  # set default value as the last link
        self.value = value
        self.next = next

    def insert(self, link):
        """Insert a new link after the current one."""
        link.next = self.next  # link 和 self的下一个 连起来
        self.next = link  # self 和 link 连起来

    def __iter__(self):
        return LinkIterator(self)


class LinkIterator:
    def __init__(self, link):
        self.here = link

    def __iter__(self):
        return self

    def __next__(self):
        if self.here:
            next = self.here
            self.here = self.here.next
            return next.value
        else:
            raise StopIteration


def byte_size(n):
    """Print the size in bytes of lists up to length n."""
    data = []
    for i in range(n):
        a = len(data)
        b = sys.getsizeof(data)
        print(f"Length:{a}; Size in bytes:{b}")
        data.append(i)
