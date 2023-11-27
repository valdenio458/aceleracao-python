import time

import pytest


@pytest.mark.slow
def test_slow_marker():
    time.sleep(4)


@pytest.mark.fast
def test_fast_marker():
    time.sleep(1)
