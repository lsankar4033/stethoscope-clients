import trio
from tenacity import retry, stop_after_delay, wait_fixed

from sclients.types import ENR

async def connect_rumor(rumor, client, enr: ENR):
    await rumor.host.start(security='noise')

    enr_str = enr.enr_teku if client == 'teku' else enr.enr

    return await peer_connect(rumor, enr_str)

@retry(sleep=trio.sleep, wait=wait_fixed(0.5), stop=stop_after_delay(10))
async def peer_connect(rumor, enr_str):
    return await rumor.peer.connect(enr_str).peer_id()
