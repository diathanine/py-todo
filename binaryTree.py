class Tree:
    def __init__(self, title):
        self.title = title
        self.child = None
    def add(self, text, child, sub, parent, side): #for children pass none if no children
    #we pass objects in for parent and children
        if parent == None:
            self.child = Node(text, "to do", None, None, self)
            return(self.child)
        else:
            node = parent.insert(text, side)
            return(node)

class Node:
    def __init__(self, text, status, child, sub, parent):
        self.text= text
        self.status= status #to-do, active, complete
        self.child= child
        self.sub= sub
        self.parent= parent

    def insert(self, text, side):
        if side:
            self.sub = Node(text, "to do", self.sub, None, self) #it cant inherit subs because if the new node is replacing a child with sub, then the sub moves with the replaced child. if the new nod is a sub being inserted into a chain of subs then those subs are children
            if self.sub.child:
                self.sub.child.parent = self.sub
            return(self.sub)
        else:
            self.child = Node(text, "to do", self.child, None, self)
            if self.child.child:
                self.child.child.parent = self.child
            return(self.child)
