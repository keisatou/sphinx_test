.. Test Documentation documentation master file, created by
   sphinx-quickstart on Sun Nov 22 17:57:19 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Test Documentation's documentation!
==============================================

Contents:

.. toctree::
   :maxdepth: 2

.. automodule:: sphinx_test.app
  :members:

Examples
=========

This is a usage of :func:`sphinx_test.app.hello`
.. code-block::python
  :linenos

  >>> import sphinx_test.app
  >>> sphinx_test.app.hello()
  hello, keisatou!
  >>> sphinx_test.app.hello('world')
  hello, world!


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

