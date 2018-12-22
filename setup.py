from setuptools import setup, find_packages

readme = ''
with open('README.md') as f:
    readme = f.read()

requirements = []
with open('requirements.txt') as f:
  requirements = f.read().splitlines()

setup(
  name = 'poro.py',
  packages = find_packages(),
  license='MIT',
  version = '1.0.0',
  description = 'An async python framework for communicating with the RiotGames API',
  long_description=readme,
  author = 'Ghostal',
  author_email = 'Zachary.Howard@outlook.com',
  url = 'https://github.com/SirGhostal/poro.py',
  keywords = ['Riot API', 'python', 'poro'],
  classifiers = [],
  install_requires=requirements
)