import os

from setuptools import setup

this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), 'r', encoding='utf-8') as f:
    readme = f.read()

setup(name='commonroad-all',
      version='0.0.2',
      description='Meta-Package for installing all CommonRoad Tools',
      long_description_content_type='text/markdown',
      long_description=readme,
      keywords='autonomous automated vehicles driving motion planning', 
      url='https://commonroad.in.tum.de/',
      author='Cyber-Physical Systems Group, Technical University of Munich',
      author_email='commonroad@lists.lrz.de',
      license='BSD',
      packages=[],
      install_requires=[
	  'commonroad-io==2022.3',
	  'commonroad-drivability-checker==2022.2.1',
	  'commonroad-vehicle-models==3.0.2',
	  'commonroad-route-planner==2022.3',
	  'sumocr==2022.4',
	  'commonroad-rl==2023.1.3',
      ],
      classifiers=["Programming Language :: Python :: 3.7",
                   "Programming Language :: Python :: 3.8",
                   "Programming Language :: Python :: 3.9",
		   "Programming Language :: C++",
                   "License :: OSI Approved :: BSD License",
                   "Operating System :: POSIX :: Linux"],
      )
