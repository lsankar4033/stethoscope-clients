import os

from pyrum import SubprocessConn, Rumor
import trio

from clients import start_instance, stop_instance, connect_rumor, InstanceConfig
from tests.constants import TEST_ENR, BEACON_STATE_LOCATION


async def test_lighthouse():
    config = InstanceConfig('lighthouse', BEACON_STATE_LOCATION, TEST_ENR)
    start_instance(config)

    try:
        async with SubprocessConn(cmd='rumor bare') as conn:
            async with trio.open_nursery() as nursery:
                rumor = Rumor(conn, nursery)
                peer_id = await connect_rumor(rumor, TEST_ENR.enr)

                # NOTE: this may not be the exact test
                assert peer_id is not None
                nursery.cancel_scope.cancel()

    finally:
        stop_instance(config)


async def test_prysm():
    config = InstanceConfig('prysm', BEACON_STATE_LOCATION, TEST_ENR)
    start_instance(config)

    try:
        async with SubprocessConn(cmd='rumor bare') as conn:
            async with trio.open_nursery() as nursery:
                rumor = Rumor(conn, nursery)
                peer_id = await connect_rumor(rumor, TEST_ENR.enr)

                # NOTE: this may not be the exact test
                assert peer_id is not None
                nursery.cancel_scope.cancel()

    finally:
        stop_instance(config)
