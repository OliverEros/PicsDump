from setuptools import setup, find_packages

setup(
        name = 'picsdump',
        version = '0.1',
        author = 'Oliver Eros',
        description = 'Automation tool for deleting images in HTML emails',
        packages = find_packages(),
        python_requires='>=3',
        install_requires = [
                            'colorama'
                           ],
        entry_points = { 'console_scripts' : ['picsdump=main.picsdump:start']},
        )
