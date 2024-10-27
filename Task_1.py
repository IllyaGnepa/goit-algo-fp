class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def insertion_sort(self):
        sorted_list = None
        current = self.head
        while current:
            next_node = current.next
            sorted_list = self.sorted_insert(sorted_list, current)
            current = next_node
        self.head = sorted_list

    def sorted_insert(self, sorted_list, new_node):
        if not sorted_list or new_node.data < sorted_list.data:
            new_node.next = sorted_list
            return new_node
        else:
            current = sorted_list
            while current.next and current.next.data < new_node.data:
                current = current.next
            new_node.next = current.next
            current.next = new_node
            return sorted_list

    def merge_sorted_lists(self, list1, list2):
        dummy = Node(0)
        tail = dummy
        while list1 and list2:
            if list1.data < list2.data:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        tail.next = list1 if list1 else list2
        return dummy.next

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Приклад використання
llist1 = LinkedList()

# Вставка вузлів
llist1.insert_at_beginning(5)
llist1.insert_at_beginning(10)
llist1.insert_at_end(20)
llist1.insert_at_end(15)

print("Початковий зв'язний список:")
llist1.print_list()

llist1.reverse()
print("Реверсований зв'язний список:")
llist1.print_list()

llist1.insertion_sort()
print("Відсортований зв'язний список (вставками):")
llist1.print_list()

llist2 = LinkedList()
llist2.insert_at_end(2)
llist2.insert_at_end(7)
llist2.insert_at_end(9)

print("Другий відсортований список:")
llist2.print_list()

merged_list = LinkedList()
merged_list.head = merged_list.merge_sorted_lists(llist1.head, llist2.head)
print("Об'єднаний відсортований список:")
merged_list.print_list()