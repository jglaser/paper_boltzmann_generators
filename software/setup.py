#!/usr/bin/env python

from setuptools import setup

setup(name='deep-boltzmann',
      version='0.1',
      description='Deep Learning Methods for Sampling Boltzmann Distributions',
      author='Frank Noe',
      author_email='frank.noe@fu-berlin.de',
      url='',
      packages=['deep_boltzmann',
                'deep_boltzmann.models',
                'deep_boltzmann.networks',
                'deep_boltzmann.sampling'],
     )
