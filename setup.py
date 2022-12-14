from setuptools import setup, find_packages

setup(
  name='healthcheck-cli',
  packages=find_packages(),
  install_requires=[
    'click',
    'requests',
    'datetime',
  ],
  version='0.0.1',
  entry_points='''
  [console_scripts]
  health-watch=health:health
  '''
)
