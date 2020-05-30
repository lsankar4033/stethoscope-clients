import os

from pyrum import SubprocessConn, Rumor
import trio

from lib.runner import start_instance, stop_instance
from lib.types import ENR, InstanceConfig
from tests.helpers import connect_rumor, TEST_ENR, BEACON_STATE_LOCATION


async def test_connect():
    config = InstanceConfig('lighthouse', BEACON_STATE_LOCATION, TEST_ENR)
    start_instance(config)

    try:
        async with SubprocessConn(cmd='rumor bare') as conn:
            async with trio.open_nursery() as nursery:
                rumor = Rumor(conn, nursery)
                peer_id = await connect_rumor(rumor, TEST_ENR.enr)
                print(f'lighthouse peer_id: {peer_id}')

                # NOTE: this may not be the exact test
                assert peer_id is not None
                nursery.cancel_scope.cancel()

    finally:
        stop_instance(config)
