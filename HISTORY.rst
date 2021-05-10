=======
History
=======

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
