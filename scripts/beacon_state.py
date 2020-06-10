def write_beacon_state(path):
    """
    This method outlines how we build beacon state for unit tests.
    """
    from eth2spec.config.config_util import prepare_config
    prepare_config('tests/config', 'minimal')

    from eth2spec.phase0.spec import initialize_beacon_state_from_eth1
    from eth2spec.test.helpers.deposits import prepare_genesis_deposits

    import eth2fastspec as spec

    print('preparing genesis deposits')
    deposits, deposit_root, _ = prepare_genesis_deposits(
        spec, spec.MIN_GENESIS_ACTIVE_VALIDATOR_COUNT, spec.MAX_EFFECTIVE_BALANCE, signed=True)

    print('initializing beacon state')
    eth1_block_hash = b'\x12' * 32
    eth1_timestamp = spec.MIN_GENESIS_TIME
    state = initialize_beacon_state_from_eth1(eth1_block_hash, eth1_timestamp, deposits)

    print('writing beacon state')
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'wb') as w:
        state.serialize(w)

    return state
