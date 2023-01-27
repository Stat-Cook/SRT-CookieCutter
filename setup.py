from setuptools import setup

setup(
    name='srt_cookiecutter',
    version='0.0.1',
    install_requires=[
        "analysis_cli @ git+https://github.com/Stat-Cook/Analysis-CookieCutter",
        "python-docx",
        "cookiecutter"
    ],
    include_package_data=True,
    entry_points='''
    [console_scripts]
    srt_init=srt_cookiecutter.cli:project_init
    srt_add_wp=srt_cookiecutter.append_wp_cli:append_wp_cli
    '''
)
