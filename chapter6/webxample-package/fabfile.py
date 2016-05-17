# -*- coding: utf-8 -*-
import os

from fabric.api import *  # noqa
from fabric.contrib.files import exists


# Let's assume we have private package repository created
# using 'devpi' project
PYPI_URL = 'http://devpi.webxample.example.com'

# This is arbitrary location for storing instaled releases.
# Each release is a separate virtual environment directory
# which is named after project version. There is also a
# symbolic link 'current' that points to recently deployed
# version. This symlink is an actual path that will be used
# for configuring the process supervision tool e.g.:
# .
# ├── 0.0.1
# ├── 0.0.2
# ├── 0.0.3
# ├── 0.1.0
# └── current -> 0.1.0/

REMOTE_PROJECT_LOCATION = "/var/projects/webxample"

env.project_location = REMOTE_PROJECT_LOCATION

# roledefs map out environment types (staging/production)
env.roledefs = {
    'staging': [
        'staging.webxample.example.com',
    ],
    'production': [
        'prod1.webxample.example.com',
        'prod2.webxample.example.com',
    ],
}


def prepare_release():
    """ Prepare a new release by creating source distribution and uploading
    to out private package repository
    """
    local('python setup.py build sdist upload -r {}'.format(
        PYPI_URL
    ))


def get_version():
    """ Get current project version from setuptools """
    return local(
        'python setup.py --version', capture=True
    ).stdout.strip()


def switch_versions(version):
    """ Switch versions by replacing symlinks atomically """
    new_version_path = os.path.join(REMOTE_PROJECT_LOCATION, version)
    temporary = os.path.join(REMOTE_PROJECT_LOCATION, 'next')
    desired = os.path.join(REMOTE_PROJECT_LOCATION, 'current')

    # force symlink (-f) since probably there is a one already
    run(
        "ln -fsT {target} {symlink}"
        "".format(target=new_version_path, symlink=temporary)
    )
    # mv -T ensures atomicity of this operation
    run("mv -Tf {source} {destination}"
        "".format(source=temporary, destination=desired))


@task
def uptime():
    """
    Run uptime command on remote host - for testing connection.
    """
    run("uptime")


@task
def deploy():
    """ Deploy application with packaging in mind """
    version = get_version()
    pip_path = os.path.join(
        REMOTE_PROJECT_LOCATION, version, 'bin', 'pip'
    )

    prepare_release()

    if not exists(REMOTE_PROJECT_LOCATION):
        # it may not exist for initial deployment on fresh host
        run("mkdir -p {}".format(REMOTE_PROJECT_LOCATION))

    with cd(REMOTE_PROJECT_LOCATION):
        # create new virtual environment using venv
        run('python3 -m venv {}'.format(version))

        run("{} install webxample=={} --index-url {}".format(
            pip_path, version, PYPI_URL
        ))

    switch_versions(version)
    # let's assume that Circus is our process supervision tool
    # of choice.
    run('circusctl restart webxample')

