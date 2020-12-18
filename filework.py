import click
import os
import shutil

def pull_line(path, search_phrase):
    click.echo("searching %s for %s" %(path, search_phrase))
    with click.open_file(path, mode='r') as file:
        lines=file.readlines()
        item_text= False
        for i, line in enumerate(lines):
            if search_phrase in line:
                item_text= line
                click.echo(item_text)
                lines.pop(i)
    with click.open_file(path, mode='w') as file:
        updated_list = "".join(lines)
        file.write(updated_list)
    return item_text


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
    target_dir = "storage/%s" %name
    shutil.rmtree(target_dir)

@click.command()
@click.argument('name')
@click.argument('item')
def add(name, item):
    click.echo('adding %s to %s' %(item, name))
    target = 'storage/%s/active.txt' %name
    active=click.open_file(target, mode='a', errors='strict', lazy=True, atomic=False)
    #check for dupes here
    active.write(item + "\n")




@click.command()
@click.argument('name')
@click.argument('item')
def complete(name, item):
    click.echo('completing %s in %s' %(item, name))
    active_file = "storage/%s/active.txt" %name
    complete_file = "storage/%s/complete.txt" %name
    item = pull_line(active_file, item)
    if item:
        complete_file = click.open_file(complete_file, mode="a")
        complete_file.write(item)
    else:
        click.echo("sorry couldn't find your item")

#border
@click.command()
@click.argument('name')
@click.argument('item')
@click.argument('target')
def move(name, item, target):
    click.echo('moving %s from %s to %s' %(item, name, target))
    active_file = "storage/%s/active.txt" %name
    complete_file = "storage/%s/complete.txt" %name

    line = pull_line(active_file, item)
    if line:
        target_path = "storage/%s/active.txt" %target
        target_file = click.open_file(target_path, mode="a")
        target_file.write(line)
    else:
        line = pull_line(complete_file, item)
        if line:
            target_path = "storage/%s/complete.txt" %target
            target_file = click.open_file(target_path, mode="a")
            target_file.write(line)
        else:
            click.echo("sorry, that item can't be found")



@click.command()
@click.argument('name', default='.')
def show(name):
    if name == '.':
        target = 'storage'
        lists = os.listdir(target)
        for list in lists:
            click.echo(list)
    else:
        target = 'storage/%s/active.txt' %name
        list=click.open_file(target, mode='r')
        lines=list.readlines()
        click.echo(str(name))
        for line in lines:
            click.echo(line)
        click.echo("end of list")

@click.command()
@click.argument('name')
def clear(name):
    click.echo('clearing')
    path = "storage/%s/complete.txt" %name
    os.remove(path)
