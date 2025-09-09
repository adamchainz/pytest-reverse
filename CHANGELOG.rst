=========
Changelog
=========

1.9.0 (2025-09-09)
------------------

* Support Python 3.14.

1.8.0 (2024-10-25)
------------------

* Drop Python 3.8 support.

* Support Python 3.13.

1.7.0 (2023-07-10)
------------------

* Drop Python 3.7 support.

1.6.0 (2023-06-16)
------------------

* Support Python 3.12.

1.5.0 (2022-05-11)
------------------

* Support Python 3.11.

1.4.0 (2022-01-10)
------------------

* Drop Python 3.6 support.

* Improve group name in ``pytest --help``.

1.3.0 (2021-08-12)
------------------

* Add type hints.

1.2.0 (2021-05-10)
------------------

* Support Python 3.10.

* Stop distributing tests to reduce package size. Tests are not intended to be
  run outside of the tox setup in the repository. Repackagers can use GitHub's
  tarballs per tag.

1.1.1 (2020-12-27)
------------------

* Fix entrypoint name.

1.1.0 (2020-12-13)
------------------

* Drop Python 3.5 support.
* Support Python 3.9.
* Move license from BSD to MIT License.

1.0.1 (2020-04-08)
------------------

* Run first to avoid interfering with ``--failed-first`` flag
  (`docs <https://docs.pytest.org/en/latest/cache.html>`__).

1.0.0 (2020-04-03)
------------------

* First release on PyPI.
