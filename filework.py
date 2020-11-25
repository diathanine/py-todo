import click

def get_path(name):
    path="./"+name+"/"

@click.command()
def foo():
    click.echo('foo')

@click.command()
@click.argument('name')
def new_list(name):
    click.echo('creating %s directory' %name)
    

@click.command()
@click.argument('name')
def delete_list(name):
    click.echo('deleting %s' %name)

@click.command()
@click.argument('name')
@click.argument('item')
def add(name, item):
    click.echo('adding %s to %s' %(item, name))
    #click.openfile()

@click.command()
@click.argument('name')
@click.argument('item')
def complete(name, item):
    click.echo('completing %s in %s' %(item, name))

@click.command()
@click.argument('name')
@click.argument('item')
@click.argument('target')
def move(name, item, target):
    click.echo('moving %s from %s to %s' %(item, name, target))

@click.command()
@click.argument('name', default='.')
def show(name):
    click.echo('%s' %name)

@click.command()
def clear():
    click.echo('clearing')
