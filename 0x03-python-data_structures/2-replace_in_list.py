#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
  """Replace element of list at specific position."""
    if idx < 0:
        return (my_list)

    length = len(my_list)

    if idx > length - 1:
        return (my_list)

    my_list[idx] = element

    return (my_list)
