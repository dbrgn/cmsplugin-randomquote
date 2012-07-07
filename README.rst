cmsplugin-randomquote
=====================

This is a django-cms plugin that displays a random quote (e.g. a testimonial)
from your database.

Setup / Configuration
---------------------

- Install this plugin
- Add ``cmsplugin_randomquote`` to your ``INSTALLED_APPS``
- Run the schema migrations::
  
    python manage.py syncdb
    python manage.py migrate cmsplugin_randomquote

- Add the plugin to a placeholder
- Create some ``Quote`` Objects in the admin panel

License
-------

`MIT <http://www.opensource.org/licenses/mit-license.html>`_, see LICENSE.txt
