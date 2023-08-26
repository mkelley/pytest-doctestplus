:orphan:

Combined directives
*******************

Marking code with two directives:

.. code-block::
.. deprecated:: 1.0

    >>> 1 + 3
    4

switch the order:

.. deprecated:: 1.0
.. code-block::

    >>> 1 + 3
    4

with a single doctest-requires:

.. doctest-requires:: sbpy

    >>> 1 + 3
    2

also mark this deprecated:

.. deprecated:: 1.0
.. doctest-requires:: sbpy

    >>> 1 + 3
    2

switch the order and the documentation build crashes:

.. doctest-requires:: sbpy
.. deprecated:: 1.0

    >>> 1 + 3
    2

.. and if that is too contrived, what I really want to do is:

.. .. doctest-requires:: sbpy
.. .. doctest-remote-data::

..     >>> 1 + 3
..     2
