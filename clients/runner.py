import subprocess

from clients.types import InstanceConfig


def _start_arg_list(config: InstanceConfig):
    return [
        f'--tcp={config.enr.tcp}',
        f'--udp={config.enr.udp}',
        f'--ip={config.enr.ip}',
        f'--private-key={config.enr.private_key}',
        f'--beacon-state-path={config.beacon_state_path}',
    ]


def start_instance(instance_config: InstanceConfig, stdout=subprocess.PIPE):
    start_script = f'bin/{instance_config.client}/start'
    output = subprocess.run(
        ['bash', start_script] + _start_arg_list(instance_config),
        stdout=stdout,
        stderr=subprocess.STDOUT,
        text=True
    )
    if output.returncode != 0:
        print(output.stdout)


def stop_instance(instance_config: InstanceConfig, stdout=subprocess.PIPE):
    output = subprocess.run(
        ['bash', f'bin/{instance_config.client}/stop'],
        stdout=stdout,
        stderr=subprocess.STDOUT,
        text=True
    )
    if output.returncode != 0:
        print(output.stdout)
