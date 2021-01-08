import binaryTree
import copy

def convert(tree): #convert to a human readable text file
    dict = tree.address_map() #dictionary of addresses and node objects
    array=[tree.title]
    for key in dict:
        array.append("%s:%s:%s" %(key, dict[key].text, dict[key].status))
    string = "\n".join(array)
    return(string)
    #should give something like:
    #title
    #0:item0:status
    #1:item1:status
    #1.0:subitem0:status
    #1.1:subitem1:status

def save(tree, file_path):
    data = convert(tree)
    file = open(file_path, 'w')
    file.write(data)
    file.close()
    return(0)

def get_text(line_array): #this is a dodge to circumnavigate potential delimiter collision in text (someone could put a colon in there)
    text = copy.deepcopy(line_array)
    text.pop(0)     #in order to do this without fucking everything up we need to either make a deepcopy or use immuteable datatypes
    text.pop(-1)
    text = ':'.join(text)
    return(text)

def load(file_path):
    file = open(file_path, 'r').readlines()
    address_book={}
    tree = binaryTree.Tree(file[0].strip())#create tree with title
    file.pop(0)
    if file:
        line = file[0].split(':')
        parent = tree.add(get_text(line), None, 0, line[-1].strip()) #create root node
        file.pop(0)
        address_book={"0" : parent}

    prev = 1

    for line in file: #create the address book as you go and add into it
        line = line.split(':') #there is a delimiter collision problem here if someone includes ':' in their text, but i think we can side step that
        address = str(line[0]).split('.')
        level = len(address) - prev
        # if address is longer its a sub node (it can only be longer by 1)
        # if address is same its a child
        # if adress is shorter its the child of a higher node (can be shorter by a lot)
        if level == 1:
            side = 1
        else:
            side = 0
        if level < 0:
            last_digit = int(address[-1]) -1
            parent = address[0:len(address)-1] + [str(last_digit)]
            parent = address_book['.'.join(parent)]

        node = tree.add(get_text(line), parent, side, line[-1].strip())
        address_book.update({line[0]:node})
        parent = node
        prev = len(address)
    return([tree, address_book])
