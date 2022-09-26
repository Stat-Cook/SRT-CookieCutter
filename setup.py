from setuptools import setup

setup(
    name='srt_cookiecutter',
    version='0.0.1',
    install_requires=[
    ],
    include_package_data=True,
    entry_points='''
    [console_scripts]
    srt_init=srt_cookiecutter.cli:project_init
    '''
)
