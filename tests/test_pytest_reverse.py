import pytest

pytest_plugins = ["pytester"]


@pytest.fixture
def ourtestdir(testdir):
    testdir.tmpdir.join("pytest.ini").write(
        "[pytest]\n" "console_output_style = classic"
    )
    yield testdir


def test_it_doesnt_reverse_order_if_not_called(ourtestdir):
    ourtestdir.makepyfile(
        test_one="""
        def test_a():
            pass

        def test_b():
            pass

        def test_c():
            pass
        """
    )
    out = ourtestdir.runpytest("-v")
    out.assert_outcomes(passed=3, failed=0)
    assert out.outlines[7:10] == [
        "test_one.py::test_a PASSED",
        "test_one.py::test_b PASSED",
        "test_one.py::test_c PASSED",
    ]


def test_it_reverses_order_if_called(ourtestdir):
    ourtestdir.makepyfile(
        test_one="""
        def test_a():
            pass

        def test_b():
            pass

        def test_c():
            pass
        """
    )
    out = ourtestdir.runpytest("-v", "--reverse")
    out.assert_outcomes(passed=3, failed=0)
    assert out.outlines[7:10] == [
        "test_one.py::test_c PASSED",
        "test_one.py::test_b PASSED",
        "test_one.py::test_a PASSED",
    ]


def test_it_reverses_order_but_failed_first_still_first(ourtestdir):
    ourtestdir.makepyfile(
        test_one="""
        def test_a():
            pass

        def test_b():
            assert 0

        def test_c():
            pass
        """
    )
    ourtestdir.runpytest()
    out = ourtestdir.runpytest("--failed-first", "-v", "--reverse")
    out.assert_outcomes(passed=2, failed=1)
    assert out.outlines[8:11] == [
        "test_one.py::test_b FAILED",
        "test_one.py::test_c PASSED",
        "test_one.py::test_a PASSED",
    ]
