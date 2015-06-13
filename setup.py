from setuptools import setup

setup(name='Kusa',
      version='1.0',
      author='TheC',
      author_email='i@thec.me',
      packages=['blog'],
      install_requires=[
      	'mistune==0.5.1',
      	'jinja2',
            'pyyaml'
      ],
      entry_points={
      	'console_scripts': ['kusa=blog.main:main']
      })