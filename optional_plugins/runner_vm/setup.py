#!/bin/env python
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
# See LICENSE for more details.
#
# Copyright: Red Hat Inc. 2017
# Author: Cleber Rosa <crosa@redhat.com>

from setuptools import setup, find_packages


setup(name='avocado-framework-plugin-runner-vm',
      description='Avocado Runner for libvirt VM Execution',
      version=open("VERSION", "r").read().strip(),
      author='Avocado Developers',
      author_email='avocado-devel@redhat.com',
      url='http://avocado-framework.github.io/',
      packages=find_packages(exclude=('tests*',)),
      include_package_data=True,
      install_requires=['avocado-framework-plugin-runner-remote', 'libvirt-python'],
      test_suite='tests',
      entry_points={
          'avocado.plugins.cli': [
              'vm = avocado_runner_vm:VMCLI',
          ],
          'avocado.plugins.runner': [
              'vm = avocado_runner_vm:VMTestRunner',
          ]},
      )
