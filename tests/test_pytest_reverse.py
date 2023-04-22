from __future__ import annotations

import pytest

pytest_plugins = ["pytester"]


@pytest.fixture
def ourtester(pytester):
    pytester.makefile(
        ".ini",
        pytest="""
            [pytest]
            console_output_style = classic
            """,
    )
    yield pytester


def test_it_doesnt_reverse_order_if_not_called(ourtester):
    ourtester.makepyfile(
        test_one="""
        def test_a():
            pass

        def test_b():
            pass

        def test_c():
            pass
        """
    )
    out = ourtester.runpytest("-v")
    out.assert_outcomes(passed=3, failed=0)
    assert out.outlines[8:11] == [
        "test_one.py::test_a PASSED",
        "test_one.py::test_b PASSED",
        "test_one.py::test_c PASSED",
    ]


def test_it_reverses_order_if_called(ourtester):
    ourtester.makepyfile(
        test_one="""
        def test_a():
            pass

        def test_b():
            pass

        def test_c():
            pass
        """
    )
    out = ourtester.runpytest("-v", "--reverse")
    out.assert_outcomes(passed=3, failed=0)
    assert out.outlines[8:11] == [
        "test_one.py::test_c PASSED",
        "test_one.py::test_b PASSED",
        "test_one.py::test_a PASSED",
    ]


def test_it_reverses_order_but_failed_first_still_first(ourtester):
    ourtester.makepyfile(
        test_one="""
        def test_a():
            pass

        def test_b():
            assert 0

        def test_c():
            pass
        """
    )
    ourtester.runpytest()
    out = ourtester.runpytest("--failed-first", "-v", "--reverse")
    out.assert_outcomes(passed=2, failed=1)
    assert out.outlines[9:12] == [
        "test_one.py::test_b FAILED",
        "test_one.py::test_c PASSED",
        "test_one.py::test_a PASSED",
    ]
