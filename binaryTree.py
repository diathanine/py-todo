class Tree:
    def __init__(self, title):
        self.title = title
        self.child = None
    def add(self, text, status="to do", parent, side): #this is only for adding new nodes that thus wont have children
    #we pass objects in for parent and children
        if parent == None:
            self.child = Node(text, status, None, None, self) #we allow a status to be passed for building saved trees
            return(self.child)
        else:
            node = parent.insert(text, side)
            return(node)

    def address_map(self):
        address_book = self.child.address_crawl()
        return address_book

    def remove_node(node): #should destroy all sub nodes ie if you delete item 2 all items 2.x should also be destroyed
        #cut node out of tree and move child node to replace it
        if node.child:
            node.child.parent = node.parent
            if node.parent.sub == node:
                node.parent.sub = node.child
            else:
                node.parent.child=node.child #don't need to check if parent.child exists because we know the parent has a sub or child since that's our node. so if the parent doesn't have a sub it must have a child

        #get this node and all sub nodes, then call destroy on all of them
        dict = node.sub.address_crawl() # we dont need the top node's children
        for i in dict.items():
            i.destroy()


class Node:
    def __init__(self, text, status, child, sub, parent):
        self.text= text
        self.status= status #to-do, active, complete
        self.child= child
        self.sub= sub
        self.parent= parent

    def insert(self, text, status, side):
        if side:
            self.sub = Node(text, status, self.sub, None, self) #it cant inherit subs because if the new node is replacing a child with sub, then the sub moves with the replaced child. if the new nod is a sub being inserted into a chain of subs then those subs are children
            if self.sub.child:
                self.sub.child.parent = self.sub #correct parent relation
            return(self.sub)
        else:
            self.child = Node(text, status, self.child, None, self) #make sure it inherits the children right
            if self.child.child:
                self.child.child.parent = self.child
            return(self.child)

    def destroy(self):
        return(0)

    def address_crawl (self, dict={}, address=0):
        dict.update({address : self})
        if self.sub:
            sub_address = "%s.0" %address
            dict.update(self.sub.address_crawl(dict, sub_address))
        if sub.child:
            child_address = str(int(address[-1])+1)
            dict.update(self.child.address_crawl(dict, child_address))
        else:
            return(dict)
