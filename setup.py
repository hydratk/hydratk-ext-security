# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from sys import argv, version_info
import hydratk.lib.install.task as task

with open("README.rst", "r") as f:
    readme = f.read()

classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Environment :: Console",
    "Environment :: Other Environment",
    "Intended Audience :: Developers",
    "License :: Freely Distributable",
    "Operating System :: OS Independent",
    "License :: OSI Approved :: BSD License",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2.6",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3.3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: Implementation",
    "Programming Language :: Python :: Implementation :: CPython",
    "Programming Language :: Python :: Implementation :: PyPy",
    "Topic :: Software Development :: Libraries :: Application Frameworks",
    "Topic :: Utilities"
]

def version_update(cfg, *args):

    major, minor = version_info[0], version_info[1]

    if (major == 2 and minor == 6):
        cfg['modules'].append({'module': 'simplejson', 'version': '==3.8.2'})
    else:
        cfg['modules'].append({'module': 'simplejson', 'version': '>=3.8.2'})

config = {
    'pre_tasks': [
        version_update,
        task.install_modules
    ],

    'post_tasks': [
        task.set_config,
        task.set_manpage
    ],

    'modules': [
        {'module': 'hydratk', 'version': '>=0.4.0'},
        {'module': 'python-owasp-zap-v2.4', 'version': '>=0.0.10'}
    ],

    'files': {
        'config': {
            'etc/hydratk/conf.d/hydratk-ext-security.conf': '/etc/hydratk/conf.d'
        },
        'manpage': 'doc/security.1'
    }
}

task.run_pre_install(argv, config)

entry_points = {
    'console_scripts': [
        'security = hydratk.extensions.security.bootstrapper:run_app'
    ]
}

setup(
    name='hydratk-ext-security',
    version='0.1.0a.dev0',
    description='Interface to security testing tools',
    long_description=readme,
    author='Petr Rašek, HydraTK team',
    author_email='bowman@hydratk.org, team@hydratk.org',
    url='http://extensions.hydratk.org/security',
    license='BSD',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    classifiers=classifiers,
    zip_safe=False,
    entry_points=entry_points,
    keywords='hydratk,security testing,msf,zap',
    requires_python='>=2.6,!=3.0.*,!=3.1.*,!=3.2.*',
    platforms='Linux'
)

task.run_post_install(argv, config)