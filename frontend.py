import binaryTree
import serializer
import click
import os

@click.command()
@click.argument('name')
def new_tree(name):
    tree = binaryTree.Tree(name)
    os.mkdir("storage/%s" %name)
    serializer.save(tree, "storage/%s/tree.txt" %name)

@click.command()
@click.option('-s', '--sub_item', is_flag=True)
@click.argument('project_name')
@click.argument('text')
@click.argument('parent_address')
def add_item(project_name, text, parent_address, sub_item):
    if sub_item: # it think we can get rid of this actually since 1=true
        side=1
    else:
        side=0
    tree = get_tree(project_name)
    if parent_address == 'None':
        parent = None
    else:
        parent = tree[1][parent_address]

    tree[0].add(text, parent, side, 'to do')
    serializer.save(tree[0], "storage/%s/tree.txt" %project_name)

@click.command()
@click.argument('project_name') #might break this into 3 different functions
def change_status(project_name, node_address, new_status):
    tree = get_tree(project_name)
    address_book = tree.address_map()
    node = address_book[node_address]
    node.status = new_status

@click.command()
@click.argument('project_name')
def view (project_name):
    tree = get_tree(project_name)
    # book_load_version = tree[1]
    address_book = tree[1] #not sure how to fix crawl, and the load version works so
    tree = tree[0]
    # print('load ver:\n' + str(book_load_version))
    # print('crawl ver:\n' + str(address_book))
    for key in address_book:
        node = address_book[key]
        indent_level = len(str(key).split('.')) -1
        string = indent_level*'-' + str(key) + ') ' + node.text + ' | ' + node.status
        click.echo(string)

def get_tree(name):
    return(serializer.load("storage/%s/tree.txt" %name))
