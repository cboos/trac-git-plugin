#!/usr/bin/env python

from setuptools import setup

setup(
    name='TracGit',
    install_requires='trac',
    description='GIT version control plugin for Trac 0.13',
    author='Herbert Valerio Riedel',
    author_email='hvr@gnu.org',
    maintainer='Christian Boos',
    maintainer_email='cboos@neuf.fr',
    keywords='trac scm plugin git',
    url="http://github.com/cboos/trac-git-plugin",
    version='0.13.0.0',
    license="GPL",
    long_description="""
    This Trac 0.13 plugin provides support for the GIT SCM.

    At this point, it'll still work fine with Trac 0.12.

    See http://trac-hacks.org/wiki/GitPlugin for more details.
    """,
    packages=['tracext', 'tracext.git'],
    namespace_packages=['tracext'],
    entry_points = {'trac.plugins': 'git = tracext.git.git_fs'},
    data_files=['COPYING','README'])
