#!/usr/bin/python3
"""Generates a .tgz archive from the contents of the web_static folder
of your AirBnB Clone repo, using the function do_pack.
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder"""
    try:
        # Create the folder if it doesn't exist
        local("mkdir -p versions")

        # Create the file name
        now = datetime.now()
        file_name = "web_static_{}{}{}{}{}{}.tgz".format(
            now.year, now.month, now.day, now.hour, now.minute, now.second)

        # Create the archive
        local("tar -cvzf versions/{} web_static".format(
            file_name))

        # Return the path to the archive
        return "versions/{}".format(file_name)

    except Exception as e:
        return None
