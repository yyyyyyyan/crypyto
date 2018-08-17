Ciphers
=======
.. automodule:: crypyto.ciphers
.. currentmodule:: crypyto.ciphers

Ciphers **crypyto** supports:

* :ref:`polybius-square-cipher`
* :ref:`atbash-cipher`
* :ref:`caesar-cipher`
* :ref:`rot13-cipher`
* :ref:`affine-cipher`
* :ref:`rail-fence-cipher`
* :ref:`keyword-cipher`
* :ref:`vigenere-cipher`
* :ref:`beaufort-cipher`

.. _polybius-square-cipher:

`Polybius Square`_
~~~~~~~~~~~~~~~~~~
   .. autoclass:: PolybiusSquare
      :members:

.. _atbash-cipher:

`Atbash`_
~~~~~~~~~
   .. autoclass:: Atbash
      :members:

.. _caesar-cipher:

`Caesar Cipher`_
~~~~~~~~~~~~~~~~
   .. autoclass:: Caesar
      :members:

.. _rot13-cipher:

`ROT13`_
~~~~~~~~
   A ``Caesar`` object with default ``key`` value of ``13``

   Examples:

   .. code:: python

      >>> from crypyto.ciphers import ROT13
      >>> ROT13.encrypt('Hello, world!')
      'URYYB, JBEYQ!'
      >>> ROT13.encrypt('URYYB, JBEYQ!')
      'HELLO, WORLD!'

.. _affine-cipher:

`Affine Cipher`_
~~~~~~~~~~~~~~~~
   .. autoclass:: Affine
      :members:

.. _rail-fence-cipher:

`Rail Fence Cipher`_
~~~~~~~~~~~~~~~~~~~~
   .. autoclass:: RailFence
      :members:

.. _keyword-cipher:

`Keyword Cipher`_
~~~~~~~~~~~~~~~~~
   .. autoclass:: Keyword
      :members:

.. _vigenere-cipher:

`Vigenère Cipher`_
~~~~~~~~~~~~~~~~~~
   .. autoclass:: Vigenere
      :members:

.. _beaufort-cipher:

`Beaufort Cipher`_
~~~~~~~~~~~~~~~~~~
   .. autoclass:: Beaufort
      :members:

.. _Polybius Square: https://en.wikipedia.org/wiki/Polybius_square
.. _Atbash: https://en.wikipedia.org/wiki/Atbash
.. _Caesar Cipher: https://en.wikipedia.org/wiki/Caesar_cipher
.. _ROT13: https://en.wikipedia.org/wiki/ROT13
.. _Affine Cipher: https://en.wikipedia.org/wiki/Affine_cipher
.. _Rail Fence Cipher: https://en.wikipedia.org/wiki/Rail_fence_cipher
.. _Keyword Cipher: https://en.wikipedia.org/wiki/Keyword_cipher
.. _Vigenère Cipher: https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher
.. _Beaufort Cipher: https://en.wikipedia.org/wiki/Beaufort_cipher