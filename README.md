# stethoscope-clients

A process runner in python for Eth 2.0 clients. Designed for use with [stethoscope](https://github.com/lsankar4033/stethoscope).

## Background

For both simulation and testing, it's valuable to be able to programmatically start and stop each Eth 2.0 client. This repo provides a python interface for doing just that. 

To be platform independent, clients are run via Docker.

To connect with and drive clients, we use [rumor](https://github.com/protolambda/rumor), specifically the [python interface](https://github.com/protolambda/pyrum).

## Installation
```
pip install stethoscope-clients
```

## Usage
The key methods in this library are `start_instance`, `stop_instance`, and `connect_rumor`. See below for a full sample usage:

```python
import trio
from pyrum import SubprocessConn, Rumor

from sclients import start_instance, stop_instance, connect_rumor, InstanceConfig, ENR

enr_str = ...
client_config = InstanceConfig(
	client='lighthouse', 
	beacon_state_path='./genesis.ssz', 
	enr= ENR(
		private_key=...,
    	tcp=9001,
    	udp=9002,
	   	id='v4'
	   	ip: '127.0.0.1'
	   	enr: enr_str,
	   	attnets: ...
	  	eth2: ...
	)
)


try:
	start_instance(client_config)
	
	# This block will eventually be encapsulated in `connect_rumor`
	async with SubprocessConn(cmd='rumor bare') as conn:
		async with trio.open_nursery() as nursery:
       	rumor = Rumor(conn, nursery)
       	client_peer_id = await connect_rumor(rumor, enr_str)
       	
       	# Insert your rumor interactions with client_peer_id
       	
       	nursery.cancel_scope.cancel()
       	
 finally:
 	stop_instance(client_config)
```

## Client progress

| client | status |
|---|---|
| lighthouse | done |
| prysm | done |
| teku | in progress |
| nimbus | TODO |
| lodestar | TODO |
| cortex | TODO |
| trinity | TODO |
