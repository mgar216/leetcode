reverse_words = lambda x : ' '.join(((''.join(x)).split(' ')[::-1]))


message = [ 'c', 'a', 'k', 'e', ' ',
        'p', 'o', 'u', 'n', 'd', ' ',
        's', 't', 'e', 'a', 'l' ]

print(reverse_words(message))