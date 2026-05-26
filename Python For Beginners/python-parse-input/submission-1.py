from typing import List

def read_integers() -> List[int]:
    value = input()
    str_list = value.split(",")
    return [int(x) for x in str_list]

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())