import binaryTree

def convert(tree): #convert to a human readable text file
    dict=tree.address_crawl() #dictionary of addresses and node objects
    array=[tree.title]
    for key in dict:
        array.append("%s:%s:%s" %(entry, dict[key].text, dict[key].status))
    string = "\n".join(array)
    return(string)
    #should give something like:
    #0:item0:status
    #1:item1:status
    #1.0:subitem0:status
    #1.1:subitem1:status

def Save(tree, file_path):
    data = convert(tree)
    file = open(file_path, 'w')
    file.write(data)
    file.close()
    return(0)

def get_text(line): #this is a dodge to circumnavigate potential delimiter collision in texxt (someone could put a colon in there)
    line.pop(0)
    line.pop(-1)
    text = ':'.join(line)
    return(text)

def load(file_path):
    file = open(file_path, 'r').readlines()

    tree = binaryTree.Tree(file[0])#create tree with title
    file.pop(0)

    line = file[0].split(':')
    parent = tree.add(get_text(line), line[-1], None, 0) #create root node
    file.pop(0)

    address_book={"0" : parent}
    prev = 1

    for line in file: #create the address book as you go and add into it
        line = line.split(':') #there is a delimiter collision problem here if someone includes ':' in their text, but i think we can side step that
        level = len(address) - prev
        # if address is longer its a sub node
        # if address is same its a child
        # if adress is shorter its the child of a higher node
        if level == 1:
            side = 1
        else:
            side = 0
        if level < 0:
            address = line[0].split('.')
            parent = address[-1]-1
            parent = address_book['.'.join(parent)]

        node = tree.add(get_text(line), line[-1], parent, side)
        address_book.update({line[0]:node})
        parent = node
    return(tree)
