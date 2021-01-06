import binaryTree
import serializer
import click
import os

@click.command()
@click.argument('name')
def new_tree(name):
    tree = binaryTree.Tree('name')
    os.mkdir("storage/%s" %name)
    serializer.save(tree, "storage/%s/tree.txt" %name)

@click.command()
@click.option('-s', '--sub_item', is_flag=True)
@click.argument('project_name')
@click.argument('text')
def add_item(project_name, text, parent_address, sub):
    if sub:
        side=1
    else:
        side=0
    tree = get_tree(project_name)
    parent = tree[1][parent_address]
    binaryTree.add(text, parent, side)

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
    address_book = tree.address_map()
    for key in address_book:
        string = len(key.split('.'))*'-' + key + ') ' + address_book[key]
        click.echo(string)

def get_tree(name):
    return(serializer.load("storage/%s/tree.txt" %project_name))
