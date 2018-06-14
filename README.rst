ValidateEmail
=============

`Build Status <https://travis-ci.org/bhargavrpatel/py-validate-email>`__
`License: MIT <https://opensource.org/licenses/MIT>`__

   Validate if an email is a disposable email.

.. code:: python

   from py_validate_email import is_valid_email

   def register(email, password):
       if not is_valid_email(email):
           raise ValueError('Cannot register email with invalid email')

Contributing
~~~~~~~~~~~~

**Pull requests welcome**

1. Fork the repository
2. Create a new branch
3. Make the necessary changes including your tests
4. Lint your code via ``make lint``
5. Check the coverage report via ``make test``
6. Create a `Pull
   Request <https://github.com/bhargavrpatel/py-validate-email/compare?expand=1>`__

Acknowledgements
~~~~~~~~~~~~~~~~

Email list was sourced from
`hallelujah/valid_email <https://github.com/hallelujah/valid_email>`__,
licensed under MIT.

License
~~~~~~~

`Reference <https://github.com/bhargavrpatel/py-validate-email>`__
