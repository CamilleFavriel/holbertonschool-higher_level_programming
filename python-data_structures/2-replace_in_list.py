#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list):
        return
    
    for i in range(len(my_list)):

        if my_list[i] == my_list[idx]:
            my_list[i] = element
        
        return my_list[i]
