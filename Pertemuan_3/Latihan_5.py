class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
    
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("null")

    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next # simpan next
            current.next = prev      # balik arah pointer
            prev = current           # geser prev
            current = next_node      # geser current

        self.head = prev # update head

input_data = input("Masukan elemen untuk Linked List: ")
angka = list(map(int, input_data.split(",")))

ll = SingleLinkedList()

for nilai in angka:
    ll.append(nilai)

print("Linked List sebelum dibalik:", end=" ")
ll.display()

ll.reverse()

print("Linked List setela dibalik", end=" ")
ll.display()