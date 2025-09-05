Tutorial
========

``reStructuredText`` automatically detects your headings (recursively) for the TOC:

.. contents::

Section 1
---------

`Python Docs <https://docs.python.org>`_

`Python Docs`_ (Link shortcuts must be declared on *every* page)

.. This is a comment.

*This is italic*, and **this is bold**.

``This is a code block.``

::

    This is also a code block.
    This style is better for multiline blocks of code.

And now, we're back to normal text.

You can also add a multiline code block after an explanatory paragraph::

    Here is how you do it (notice the two colons above).
    Those two colons render as one colon.

And now, we're back to normal text again.

The following method enables language-specific syntax highlighting:

.. code::

    from datetime import datetime
    print(datetime.now())

And now, we're back to normal text again.

This is an unordered list:

* apple
* banana

And this is an ordered list:

#. Coke
#. Pepsi

Here is how you set up a link to another page:

See the :doc:`changelog`.

Here is how you set up a target/bookmark:

.. _tutorialsection2:

Section 2
---------

Callout boxes (if that's what they're called) grab your attention, like this:

.. note::

    Please see the `documentation <https://docs.python.org>`_.

.. attention::

    Please see the `documentation <https://docs.python.org>`_.

.. danger::

    Please see the `documentation <https://docs.python.org>`_.

As you can see, there are different levels of callout boxes.

You can also make tables:

======== ======== ========
Column A Column B Column C
======== ======== ========
Row 1A   Row 1B   Row 1C
Row 2A   Row 2B   Row 2C
======== ======== ========

There is also a ``csv-table`` way to build tables (see the documentation).

Here is how you insert an image:

.. image:: https://davo.co/wp-content/uploads/2025/07/davo_headshot_150_70.webp

Here is how you create a download link:

Download the :download:`makefile <./make.bat>`

.. _Python Docs: https://docs.python.org