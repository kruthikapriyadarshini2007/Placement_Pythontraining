class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class sll:
    def __init__(self):
        self.head = None 

    # INSERT AT BEGINNING
    def insert_begin(self, data):
        nn = Node(data)
        if self.head is None:
            self.head = nn
            return
        nn.next = self.head
        self.head = nn

    # INSERT AT END
    def insert_end(self, data):
        nn = Node(data)
        if self.head is None:
            self.head = nn
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = nn

    # INSERT AT ANY POSITION
    def insert_at_pos(self, data, pos):
        if pos <= 0:
            print("Invalid position")
            return
        if pos == 1:
            self.insert_begin(data)
            return
        temp = self.head
        i = 1
        while i < pos - 1 and temp is not None:
            temp = temp.next
            i += 1
        if temp is None:
            print("Insufficient nodes")
            return
        nn = Node(data)
        nn.next = temp.next
        temp.next = nn

    # COUNT
    def count(self):
        temp = self.head
        c = 0
        while temp is not None:
            c += 1
            temp = temp.next
        return c

    # DELETE AT BEGINNING
    def delete_begin(self):
        if self.head is None:
            print("List is empty")
            return
        self.head = self.head.next

    # DELETE AT END
    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None

    # DELETE AT ANY POSITION
    def delete_at_pos(self, pos):
        if self.head is None:
            print("List is empty")
            return
        if pos <= 0:
            print("Invalid position")
            return
        if pos == 1:
            self.delete_begin()
            return
        temp = self.head
        i = 1
        while i < pos - 1 and temp.next is not None:
            temp = temp.next
            i += 1
        if temp.next is None:
            print("Invalid position")
            return
        temp.next = temp.next.next

    # search for song
    def search(self,data):
        temp = self.head
        pos = 1
        while temp is not None:
            if temp.data == data:
                return pos
            temp = temp.next
            pos += 1
        return -1  # Song not found
 
    # DISPLAY
    def display(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def reverse_playlist(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
    



# MAIN PROGRAM

l = sll()

while True:
    print("\n----- SINGLY LINKED LIST -----")
    print("1. Insert a song at beginning")
    print("2. Add a song at the end")
    print("3. Insert a song at a specified position")
    print("4. Remove the first song")
    print("5. Remove the last song")
    print("6. Remove a song at a specified position")
    print("7. Search for a song")
    print("8. Display total number of songs")
    print("9. Display the complete playlist")
    print("10. Reverse the playlist")
    print("11. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        data = input("Enter song name: ")
        l.insert_begin(data)

    elif choice == "2":
        data = input("Enter song name: ")
        l.insert_end(data)

    elif choice == "3":
        data = input("Enter song name: ")
        pos = int(input("Enter position: "))
        l.insert_at_pos(data, pos)

    elif choice == "4":
        l.delete_begin()

    elif choice == "5":
        l.delete_end()

    elif choice == "6":
        pos = int(input("Enter position: "))
        l.delete_at_pos(pos)

    elif choice == "7":
        data = input("Enter song name: ")
        pos = l.search(data)

        if pos != -1:
            print("Song found at position", pos)
        else:
            print("Song not found")

    elif choice == "8":
        print("Number of songs:", l.count())

    elif choice == "9":
        l.display()

    elif choice == "10":
        l.reverse_playlist()
        print("Playlist reversed:")
        l.display()

    elif choice == "11":
        print("Program ended")
        break

    else:
        print("Invalid choice")