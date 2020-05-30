import subprocess

from lib.types import InstanceConfig


def start_arg_list(config: InstanceConfig):
    return [
        f'--tcp={config.enr.tcp}',
        f'--udp={config.enr.udp}',
        f'--ip={config.enr.ip}',
        f'--private-key={config.enr.private_key}',
        f'--beacon-state-path={config.beacon_state_path}',
    ]


def start_instance(instance_config: InstanceConfig, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL):
    start_script = f'clients/{instance_config.client}/start.sh'
    output = subprocess.run(
        ['sh', start_script] + start_arg_list(instance_config),
        stdout=stdout,
        stderr=stderr,
        text=True
    )
    if output.stdout is not None and len(output.stdout) > 0:
        print(output.stdout)


def stop_instance(instance_config: InstanceConfig, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL):
    output = subprocess.run(
        ['sh', f'clients/{instance_config.client}/stop.sh'],
        stdout=stdout,
        stderr=stderr,
        text=True
    )
    if output.stdout is not None and len(output.stdout) > 0:
        print(output.stdout)
