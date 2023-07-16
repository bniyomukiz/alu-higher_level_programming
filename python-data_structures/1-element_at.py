#!/usr/bin/python3
def element_at(my_list, idx):
    """function to retrieve an element"""
    if idx < 0 or idx >= len(my_list):
        return None
    else:
        return my_list[idx]
