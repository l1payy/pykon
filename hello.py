class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return "Stack is empty"

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        return self.items


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def linear_search(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, current, value):
        if value < current.value:
            if current.left:
                self._insert(current.left, value)
            else:
                current.left = Node(value)
        elif value > current.value:
            if current.right:
                self._insert(current.right, value)
            else:
                current.right = Node(value)

    def inorder(self):
        return self._inorder(self.root, [])

    def _inorder(self, node, traversal):
        if node:
            self._inorder(node.left, traversal)
            traversal.append(node.value)
            self._inorder(node.right, traversal)
        return traversal


class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def display(self):
        return self.adj_list


class HashTable:
    def __init__(self):
        self.table = {}

    def insert(self, key, value):
        self.table[key] = value

    def search(self, key):
        return self.table.get(key, "Not found")


def main():
    while True:
        print("\nWelcome to the Application!")
        print("Choose an option:")
        print("1. Stack")
        print("2. Sorting")
        print("3. Searching")
        print("4. Binary Tree")
        print("5. Graph")
        print("6. Hash Table")
        print("7. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            stack = Stack()
            while True:
                print("\nStack Operations:")
                print("1. Push")
                print("2. Pop")
                print("3. Display")
                print("4. Back to Main Menu")
                op = int(input("Choose operation: "))
                if op == 1:
                    stack.push(input("Enter item to push: "))
                elif op == 2:
                    print("Popped item:", stack.pop())
                elif op == 3:
                    print("Stack contents:", stack.display())
                elif op == 4:
                    break

        elif choice == 2:
            arr = list(map(int, input("Enter numbers to sort (separated by spaces): ").split()))
            print("Sorted array:", bubble_sort(arr))

        elif choice == 3:
            arr = list(map(int, input("Enter numbers (separated by spaces): ").split()))
            target = int(input("Enter number to search: "))
            index = linear_search(arr, target)
            print("Index of target:", index if index != -1 else "Not found")

        elif choice == 4:
            tree = BinaryTree()
            while True:
                print("\nBinary Tree Operations:")
                print("1. Insert")
                print("2. Display (In-order Traversal)")
                print("3. Back to Main Menu")
                op = int(input("Choose operation: "))
                if op == 1:
                    tree.insert(int(input("Enter number to insert: ")))
                elif op == 2:
                    print("Binary Tree (In-order):", tree.inorder())
                elif op == 3:
                    break

        elif choice == 5:
            graph = Graph()
            while True:
                print("\nGraph Operations:")
                print("1. Add Edge")
                print("2. Display")
                print("3. Back to Main Menu")
                op = int(input("Choose operation: "))
                if op == 1:
                    u, v = input("Enter two nodes (u v): ").split()
                    graph.add_edge(u, v)
                elif op == 2:
                    print("Graph Adjacency List:", graph.display())
                elif op == 3:
                    break

        elif choice == 6:
            hash_table = HashTable()
            while True:
                print("\nHash Table Operations:")
                print("1. Insert")
                print("2. Search")
                print("3. Back to Main Menu")
                op = int(input("Choose operation: "))
                if op == 1:
                    key = input("Enter key: ")
                    value = input("Enter value: ")
                    hash_table.insert(key, value)
                elif op == 2:
                    key = input("Enter key to search: ")
                    print("Value:", hash_table.search(key))
                elif op == 3:
                    break

        elif choice == 7:
            print("Exiting the application. Goodbye!")
            break

if __name__ == "__main__":
    main()
