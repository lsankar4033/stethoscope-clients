from tenacity import retry, wait_fixed, stop_after_delay
import trio

from sclients.types import ENR

@retry(sleep=trio.sleep, wait=wait_fixed(1), stop=stop_after_delay(15))
async def connect_rumor(rumor, client, enr: ENR):
    await rumor.host.start()

    enr_str = enr.enr_teku if client == 'teku' else enr.enr
    peer_id = await rumor.peer.connect(enr_str).peer_id()
    return peer_id
