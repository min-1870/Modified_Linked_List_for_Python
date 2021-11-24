class Node:
    def __init__ (self, item, link=None):
        self.item = item
        self.link = link

    def __str__ (self):
        return str(self.item)


class linkedListIterator:
    def __init__(self, node) -> None:
        self.current = node

    def __iter__(self) -> Node:
        return self
    
    def __next__(self):
        if self.current is not None:
            item = self.current.item
            self.current = self.current.link
            return item
        else:
            raise StopIteration   


class linkedList:

    def __init__ (self) -> None:
        self.head = None
        self.tail = None
        self.size = 0


    def __len__ (self) -> int:
        '''
        This method return the number of the elements in the list.
        O(1)
        '''

        return self.size


    def __iter__ (self) -> linkedListIterator:
        '''
        This method allow the list iterable.
        O(n) n = self.size
        '''

        return linkedListIterator(self.head)


    def empty (self) -> bool:
        '''
        This method check the list is empty or not.
        O(1)
        '''

        result = False

        if self.head is None:
            result = True
        
        return result
    
    
    def append (self, value) -> None:
        '''
        This method append the element to the list.
        O(1)
        '''

        newNode = Node(value, None)

        if self.empty():
            self.head = newNode
            
        else:
            self.tail.link = newNode

        self.tail = newNode
        newNode.link = None
        self.size += 1


    def removeAtIndex (self, index) -> None:
        '''
        This method remove the node at the index.
        O(n) n = index
        '''

        if index >= self.size and index < 0:
            raise IndexError("The index is out of bounds.")

        if index == 0:
            self.head = self.head.link

        else:
            current = self.head
            counter = 0

            while current.link is not None:

                if counter+1 == index:
                    current.link = current.link.link

                    if current.link == None:
                        self.tail = current

                    break

                current = current.link
                counter += 1
        
        self.size -= 1


    def removeAtIndexes (self, Indexes) -> None:
        '''
        This method remove the nodes at multiple indexes.
        O(n) n = the biggest index in the list
        '''
        
        def makeSlice(lst):
            '''
            This method change the format of the list into slicing.
            O(n) n = length of the list
            '''
            start = lst[0]  
            result = []

            for i in range(len(lst)-1):
                diff = lst[i+1] - lst[i]

                if diff != 1:
                    end = lst[i]
                    end += 1
                    result.append([start, end])
                    start = lst[i+1]
        
            result.append([start, lst[len(lst)-1]+1])
    
            return result

        if self.empty():
            raise IndexError("There is not elements to remove.")
        
        else:
            index = 0
            current = self.head
            sliced = makeSlice(Indexes)
            m = sliced[:]
            print(sliced)

            while current is not None:
                    
                if index == sliced[0][1]:
                    if  0 == sliced[0][0]:
                        self.head = current
                    else:
                        startNode.link = current
                    del sliced[0]
                
                if len(sliced) == 0: 
                    break   

                if index+1 == sliced[0][0] and 0 != sliced[0][0]:
                    startNode = current

                    if self.size == sliced[0][1]:
                        startNode.link = None
                        self.tail = startNode
                 
                current = current.link
                index += 1 

            self.size -= sum([i[1]-i[0] for i in m])

    
    def __str__(self) -> str:
        '''
        This method make the list of each item.
        O(n) n = self.size       
        '''
        result = []
        
        for i in self:
            result.append(i)

        return str(result)