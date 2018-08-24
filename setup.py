from setuptools import setup

setup(
    name='click-sample',
    version='1.0',
    packages=['click_sample'],
    include_package_data=True,
    install_requires=[
        'click',
    ],
    entry_points='''
        [console_scripts]
        click=main:execute
    ''',
)
