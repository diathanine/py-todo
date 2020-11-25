from setuptools import setup

setup(
    name="todo",
    version='0.1',
    py_modules=['filework'],
    install_requires=['click'],
    entry_points='''
        [console_scripts]
        test=filework:foo
        add=filework:add
        complete=filework:complete
        move=filework:move
        show=filework:show
        new-list=filework:new_list
        delete-list=filework:delete_list
        clear=filework:clear
        '''
)
