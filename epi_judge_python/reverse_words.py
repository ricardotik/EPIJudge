import functools
import collections
from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Assume s is a list of strings, each of which is of length 1, e.g.,
# ['r', 'a', 'm', ' ', 'i', 's', ' ', 'c', 'o', 's', 't', 'l', 'y'].
def reverse_words(s):
    # TODO - you fill in here.
    dequeue = collections.deque()
    starting_pointer = 0

    for i in range(len(s)):
        word = ""
        if s[i] == " ":
            for character in (s[starting_pointer:i]):
                word += character
            dequeue.append(word)
            starting_pointer = i + 1
            dequeue.append(" ")

    word = ""
    for character in (s[starting_pointer:]):
        word += character
    dequeue.append(word)

    i = 0
    while len(dequeue) > 0:
        word = dequeue.pop()
        for character in word:
            s[i] = character
            i += 1

    return s


@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = list(s)

    executor.run(functools.partial(reverse_words, s_copy))

    return ''.join(s_copy)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_words.py', 'reverse_words.tsv',
                                       reverse_words_wrapper))
