from setuptools import setup

setup(
    name="todo",
    version='0.1',
    py_modules=['frontend'],
    install_requires=['click'],
    entry_points='''
        [console_scripts]
        new=frontend:new_tree
        add=frontend:add_item
        status=frontend:change_status
        view=frontend:view
        move=filework:move
        new-list=filework:new_list
        delete-list=filework:delete_list
        clear=filework:clear
        '''
)
