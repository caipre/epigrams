#!/usr/bin/env python3

def partition_into_anagrams(lst):
    d = {}
    for word in lst:
        sw = ''.join(sorted(word))
        try: d[sw].append(word)
        except: d[sw] = [word]
    return ([vs for vs in d.values() if len(vs) > 1])

lst = [ 'debitcard', 'elvis', 'silent', 'badcredit', 'lives', 'freedom', 'listen', 'levis' ]
assert partition_into_anagrams(lst) == [ ['elvis', 'lives', 'levis'],
                                         ['debitcard', 'badcredit'],
                                         ['silent', 'listen'] ]
