from setuptools import setup

setup(name='ljbq',
      version='0.1',
      description='Parameterized Locally Cached BigQuery Queries',
      url='http://github.com/philya/ljbq',
      author='Philip Olenyk',
      author_email='philya@gmail.com',
      license='MIT',
      packages=['ljbq'],
      install_requires=[
          'pandas-gbq',
          'pandas'
      ],
      zip_safe=False)
