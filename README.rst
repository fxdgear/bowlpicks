Basic Project
===============

How to use
---------------

Basically this is just a skeleton of a basic project we use all the time.
What I would do is create a new virtualenv::

    mkvirtualenv --no-site-packages <project_name>

- Then copy this project into your virtualenv's src directory.
- Next get rid of the .git dir in this project.
- install the pip requirements
- Next rename ``project_name`` to what ever you project is called
- Next go through ``settings/base.py`` and change the following:

    - ADMINS
    - SECRET_KEY - Should look like this "gue&$ic-=lo+8$g^0ej(7u1oe0dsa68!qa$xqhxyfpo$bqn2e0" But make sure it's unique (random chars)
    - ROOT_URLCONF


Now you shold be at a point where you can now run ``git init`` or what ever, and create a new repo from this skeleton
Oh you should go through the .gitignore file and change ``project_name`` to what ever you project name is
enjoy


payout calculator: https://gist.github.com/08f3b6fcf36f06a619ac
