from importlib import resources

from sclients import ENR

BEACON_STATE_LOCATION = './tests/ssz/tests.ssz'

# NOTE: currently identical to the ENR in single_client_genesis suite, but maybe not this in the future
TEST_ENR_DICT = {
    'enr': 'enr:-LK4QJCIZoViytOOmAzAbdOJODwQ36PhjXwvXlTFTloTzpawVpvPRmtrM6UZdPmOGck5yPZ9AbgmwyZnE3jm4jX0Yx0Bh2F0dG5ldHOIAAAAAAAAAACEZXRoMpBGMkSJAAAAAf__________gmlkgnY0gmlwhH8AAAGJc2VjcDI1NmsxoQOnBq2PcxFfkFACZvJz91cd-UKaTPtLv7zYJSJyAtq60YN0Y3CCIyiDdWRwgiMp',
    'enr_teku': 'enr:-KG4QF9w4w5DORl2-AtVaqK6n-VF3e-2p5fm4uqDLwlR8cQ4MVk2yJ68YkEUTASbbJJ123CKYDDY1KdfBWOuVrmsZtUChGV0aDKQGK5MywAAAAH__________4JpZIJ2NIJpcIR_AAABiXNlY3AyNTZrMaEDpwatj3MRX5BQAmbyc_dXHflCmkz7S7-82CUicgLautGDdGNwgiMog3VkcIIjKA',
    'private_key': 'eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee',
    'udp': 9001,
    'tcp': 9000,
    'id': 'v4',
    'ip': '127.0.0.1',
    'attnets': '0x0000000000000000',
    'eth2': '0x4632448900000001ffffffffffffffff'
}
TEST_ENR = ENR(**TEST_ENR_DICT)
