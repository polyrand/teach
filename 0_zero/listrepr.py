from typing import Iterable

def get_repr(elem, l):

    if len(str(elem)) > l:

        return str(elem)[: l - 3] + "..."

    return str(elem)


def list_repr(iterable: Iterable = None):

    # h = 3

    max_len = max((len(str(e)) for e in iterable))

    # maximun length to print
    max_len_repr = min(max_len, 10)

    # nº of boxes to show
    length = min(len(iterable), 10)

    s0 = []
    s1 = []
    s2 = []

    for n in range(length):

        # max_len + 2 spaces, one each side
        num = max_len_repr + 2

        spaces = num - (len(str(n)) - 1)
        s0.append(f"{n}{' ' * spaces}")

        s1.append(f"+{'-' * num}")

        s2.append(f"|{' ' * num}")

    s2f = []

    for elem in iterable[:length]:

        extra_space = max_len_repr + 2 - len(get_repr(elem, max_len_repr))

        half1 = round(extra_space / 2)
        half2 = extra_space - half1

        s2f.append(f"|{' ' * half1}{get_repr(elem, max_len_repr)}{' ' * half2}")

    s2f = "".join(s2f) + "|"

    s2fn = "".join(s2) + "|"
    
    placeholder = "..." if len(iterable) > length else ""
    
    sf = f""" {"".join(s0)}
{"".join(s1)}+
{s2fn}
{s2f}
{s2fn}
{"".join(s1)}+{placeholder}
"""
    return sf
    
    
# print(
#     list_repr(
#         [1, 2, "asdfgasdasdasdasd", None, 2.3256123123123, -1, 45, 69, 1, 1, 1, 1, 1, 1]
#     )
# )
# 
#  0            1            2            3            4            5            6            7            8            9            
# +------------+------------+------------+------------+------------+------------+------------+------------+------------+------------+
# |            |            |            |            |            |            |            |            |            |            |
# |      1     |      2     | asdfgas... |    None    | 2.32561... |     -1     |     45     |     69     |      1     |      1     |
# |            |            |            |            |            |            |            |            |            |            |
# +------------+------------+------------+------------+------------+------------+------------+------------+------------+------------+...
