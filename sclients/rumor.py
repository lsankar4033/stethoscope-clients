from tenacity import retry, wait_fixed, stop_after_delay
import trio


@retry(sleep=trio.sleep, wait=wait_fixed(1), stop=stop_after_delay(10))
async def connect_rumor(rumor, enr):
    await rumor.host.start()
    peer_id = await rumor.peer.connect(enr).peer_id()
    return peer_id
