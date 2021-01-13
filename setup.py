from setuptools import setup

setup(
    name="todo",
    version='0.2',
    py_modules=['frontend'],
    install_requires=['click'],
    entry_points='''
        [console_scripts]
        new=frontend:new_tree
        add=frontend:add_item
        status=frontend:change_status
        view=frontend:view
        edit=frontend:change_text
        render_settings=frontend:render_settings
        render=frontend:render
        '''
)
