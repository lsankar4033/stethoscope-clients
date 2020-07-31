import trio

from sclients.types import ENR

async def connect_rumor(rumor, client, enr: ENR):
    await rumor.host.start(security='noise')

    enr_str = enr.enr_teku if client == 'teku' else enr.enr
    peer_id = await rumor.peer.connect(enr_str).peer_id()
    return peer_id
