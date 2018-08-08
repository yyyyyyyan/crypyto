Substitution Alphabets
======================
.. automodule:: crypyto.substitution_alphabets
.. currentmodule:: crypyto.substitution_alphabets

Alphabets **crypyto** supports:

* :ref:`morse-code`
* :ref:`image-substitution`
* :ref:`templar-cipher`

.. _morse-code:

`Morse Code`_
~~~~~~~~~~~~~
   .. autoclass:: Morse
      :members:

.. _image-substitution:

Image Substitution
~~~~~~~~~~~~~~~~~~
   .. autoclass:: ImageSubstitution
      :members:

.. _templar-cipher:

`Templar Cipher`_
~~~~~~~~~~~~~~~~~
   `Templar` represents an ``ImageSubstitution`` object adjusted to the Templar Cipher

   Examples:

   .. code:: python

      >>> from crypyto.substitution_alphabets import Templar
      >>> Templar.encrypt('Hello, world!', 'templar_hello.png')
      >>> Templar.encrypt('Hello, world!', 'templar_hello_max.png', 5)

   **templar_hello.png**:

   .. figure:: https://raw.githubusercontent.com/yanorestes/crypyto/master/templar_hello.png
      :alt: Encrypted hello world

      Encrypted hello world

   **templar_hello_max.png**:

   .. figure:: https://raw.githubusercontent.com/yanorestes/crypyto/master/templar_hello_max.png
      :alt: Encrypted hello world (5 letters per line)

      Encrypted hello world (5 letters per line)

.. _Morse Code: https://en.wikipedia.org/wiki/Morse_code
.. _Templar Cipher: https://en.wikipedia.org/wiki/Pigpen_cipher#Variants