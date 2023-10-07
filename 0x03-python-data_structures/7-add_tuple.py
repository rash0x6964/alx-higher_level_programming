#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = tuple_a[:2]
    b = tuple_b[:2]
    a_n0 = a[0] if len(a) > 0 else 0
    a_n1 = a[1] if len(a) > 1 else 0
    b_n0 = b[0] if len(b) > 0 else 0
    b_n1 = b[1] if len(b) > 1 else 0
    return (a_n0 + b_n0, a_n1 + b_n1)
