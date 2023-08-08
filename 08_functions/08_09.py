# Messages
from typing import List

message: List = ['Portugal is in Europe', 'Spain is in Europe', 'France is in Europe',
                 'Angola is in Africa', 'Japan is in Asia']

def show_messages(msgs: List):
    for msg in msgs:
        print(msg)


show_messages(message)

