import binaryTree
import serializer
import render as textify #for some reason the name render pisses it off, theres a namespace collision somewhere i guess
import click
import os

@click.command()
@click.argument('name')
def new_tree(name):
    render_settings = open("storage/default_render_settings.txt",'r')
    tree = binaryTree.Tree(name)
    os.mkdir("storage/%s" %name)
    serializer.save(render_settings, "storage/%s/render_settings.txt" %name)
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
@click.argument('node_address')
@click.argument('new_status')
def change_status(project_name, node_address, new_status):
    tree = get_tree(project_name)
    address_book = tree[1]
    node = address_book[node_address]
    node.status = new_status
    serializer.save(tree[0], "storage/%s/tree.txt" %project_name)

@click.command()
@click.argument('project_name')
@click.argument('node_address')
@click.argument('new_text')
def change_text(project_name, node_address, new_text):
    tree = get_tree(project_name)
    node = tree[1][node_address]
    node.text = new_text
    serializer.save(tree[0], "storage/%s/tree.txt" %project_name)

@click.command()
@click.argument('project_name')
def view (project_name):
    tree = get_tree(project_name)
    address_book = tree[1]
    tree = tree[0]
    # print('load ver:\n' + str(book_load_version))
    # print('crawl ver:\n' + str(address_book))
    for key in address_book:
        node = address_book[key]
        indent_level = len(str(key).split('.')) -1
        string = indent_level*'-' + str(key) + ') ' + node.text + ' | ' + node.status
        click.echo(string)

@click.command()
@click.argument('project_name')
@click.argument('file', type=click.File('w'), default = '-')
def render(project_name, file): #print to console when not specified
    tree = get_tree(project_name)
    address_book = tree[1]
    settings_dict = serializer.load_settings('storage/%s/render_settings.txt' %project_name)
    string = textify.render(address_book, settings_dict)
    file.write(string)
    return(0)

@click.command()
@click.argument('project_name')
def render_settings(project_name):
    string = 'settings updated here'
    click.echo(string)
    return(0)

def get_tree(name):
    return(serializer.load("storage/%s/tree.txt" %name))
