import click
import os


def get_path(name):
    target=path("storage/%s" %name)

@click.command()
def foo():
    click.echo('foo')

@click.command()
@click.argument('name')
def new_list(name):
    click.echo('creating %s directory' %name)
    target_dir="storage/%s" %name
    os.mkdir(target_dir)

    os.chdir(target_dir)
    click.echo(os.getcwd())
    click.open_file('settings.txt', mode='w', encoding=None, errors='strict', lazy=False, atomic=False)
    click.open_file('active.txt', mode='w', encoding=None, errors='strict', lazy=False, atomic=False)
    click.open_file('complete.txt', mode='w', encoding=None, errors='strict', lazy=False, atomic=False)


@click.command()
@click.argument('name')
def delete_list(name):
    click.echo('deleting %s' %name)

@click.command()
@click.argument('name')
@click.argument('item')
def add(name, item):
    click.echo('adding %s to %s' %(item, name))
    target = 'storage/%s/active.txt' %name
    active=click.open_file(target, mode='a', errors='strict', lazy=True, atomic=False)
    active.write(item)

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
    target = 'storage/%s/active.txt' %name
    list=click.open_file(target, mode='r')
    click.echo(list)
    click.echo('%s' %name)

@click.command()
def clear():
    click.echo('clearing')
