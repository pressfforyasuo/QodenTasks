import array as arr

class HashTable:
    def __init__(self, size):
        self.values = [None] * size
    
    def add(self, new_value):
        index = new_value % len(self.values)
        new_node = ListNode(new_value)
        
        if self.values[index] is None:
            self.values[index] = new_node
        else:
            current_node = self.values[index]
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
    
    def print_table(self):
        for i in range(len(self.values)):
            print(f"{i}: ", end="")
            current_node = self.values[i]
            while current_node is not None:
                print(f"{current_node.value} ", end="")
                current_node = current_node.next
            print()

class ListNode:
    def __init__(self, new_value):
        self.value = new_value
        self.next = None

N = int(input())
input_values = input().split()
values = arr.array('i', map(int, input_values))
        
hash_table = HashTable(N)
for value in values:
    hash_table.add(value)
        
hash_table.print_table()
