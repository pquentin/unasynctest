import pytest

import unasynctest._async
import unasynctest._sync


@pytest.mark.trio
async def test_simple():
    assert unasynctest._sync.f() == 1
    assert await unasynctest._async.f()
