#!/usr/bin/env python3

from setuptools import setup

setup(name='africayellowpage',
      version='1.0',
      description='Scraping Africa yellow Page',
      #url='http://github.com/storborg/funniest',
      author='Aminou Moussa',
      author_email='aminou455@yahoo.fr',
      license='MIT',
      entry_points="""
      [console_scripts]
      africayellowpage-scraper=africayellowpage:main
      """,
      classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
      ],
      python_requires='>=3.6.0',
      packages=['africayellowpage'],
      zip_safe=False)