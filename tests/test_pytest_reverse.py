import pytest

pytest_plugins = ["pytester"]


@pytest.fixture
def ourtestdir(testdir):
    testdir.tmpdir.join("pytest.ini").write(
        "[pytest]\n" "console_output_style = classic"
    )
    testdir.makepyfile(
        test_one="""
        def test_a():
            pass

        def test_b():
            pass

        def test_c():
            pass
        """
    )
    yield testdir


def test_it_doesnt_reverse_order_if_not_called(ourtestdir):
    out = ourtestdir.runpytest("-v")
    out.assert_outcomes(passed=3, failed=0)
    assert out.outlines[7:10] == [
        "test_one.py::test_a PASSED",
        "test_one.py::test_b PASSED",
        "test_one.py::test_c PASSED",
    ]


def test_it_reverses_order_if_called(ourtestdir):
    out = ourtestdir.runpytest("-v", "--reverse")
    out.assert_outcomes(passed=3, failed=0)
    assert out.outlines[7:10] == [
        "test_one.py::test_c PASSED",
        "test_one.py::test_b PASSED",
        "test_one.py::test_a PASSED",
    ]
