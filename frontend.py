import binaryTree
import serializer
import click

@click.command()
@click.argument('name')
def new_tree(name):
    tree = binaryTree.Tree('name')
    serializer.save(tree, "storage/%s/tree.txt" %name)

@click.command()
@click.option('-s', '--sub_item', is_flag=True)
@click.argument('project_name')
@click.arguement('text')
def add_item(project_name, text, parent_address, sub):
    if sub:
        side=1
    else:
        side=0
    tree = serializer.load("storage/%s/tree.txt" %project_name)
    parent = tree[1][parent_address]
    binaryTree.add(text, parent, side)

@click.command()
@click.argument()
def change_status(tree, node, new_status):
    node.status = status #pseudocode

@click.command()
@click.argument('project')
def view (project):
    tree = serializer.load(file)

def get_tree(name):
