dict = {'k':1, 'q':1, 'l':2, 'b':2, 'n':2, 'p':8}

k, q, l, b, n, p = map(int, input().split())

print(dict['k']-k, dict['q']-q, dict['l']-l, dict['b']-b, dict['n']-n, dict['p']-p)