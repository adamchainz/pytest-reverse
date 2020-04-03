def pytest_addoption(parser):
    group = parser.getgroup("reverse", "Reverse test order")
    group._addoption(
        "--reverse",
        action="store_true",
        dest="reverse",
        help="""Reverse test order.""",
    )


def pytest_collection_modifyitems(session, config, items):
    if config.getoption("reverse"):
        items[:] = items[::-1]
