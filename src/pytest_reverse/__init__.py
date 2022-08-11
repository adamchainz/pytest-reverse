from __future__ import annotations

from typing import Generator

import pytest
from _pytest.config import Config
from _pytest.config.argparsing import Parser
from _pytest.nodes import Item


def pytest_addoption(parser: Parser) -> None:
    group = parser.getgroup("reverse", "pytest-reverse")
    group._addoption(
        "--reverse",
        action="store_true",
        dest="reverse",
        help="""Reverse test order.""",
    )


# pytest missing type hints for @hookimpl
@pytest.hookimpl(hookwrapper=True, tryfirst=True)  # type: ignore [misc]
def pytest_collection_modifyitems(
    config: Config, items: list[Item]
) -> Generator[None, None, None]:
    if config.getoption("reverse"):
        items[:] = items[::-1]

    yield
