import binaryTree

def convert(tree): #convert to a human readable text file
    dict=tree.address_crawl()
    array=[]
    for key in dict:
        array.append("%s:%s" %(entry, dict[key]))
    string = "\n".join(array)
    return(string)

def Save(tree, file_path):
    data = convert(tree)
    file = open(file_path, 'w')
    file.write(data)
    file.close()
    return(0)

def load(file_path):
    #split on new lines
    #use addresses to build tree
    tree=None
    return(tree)
