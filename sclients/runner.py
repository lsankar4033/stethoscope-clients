from importlib import resources
import subprocess

from sclients.types import InstanceConfig


def _start_arg_list(config: InstanceConfig):
    return [
        f'--tcp={config.enr.tcp}',
        f'--udp={config.enr.udp}',
        f'--ip={config.enr.ip}',
        f'--private-key={config.enr.private_key}',
        f'--beacon-state-path={config.beacon_state_path}',
    ]


def start_instance(instance_config: InstanceConfig, stdout=subprocess.PIPE):
    with resources.path(f'sclients.bin', f'{instance_config.client}_start') as start_path:
        output = subprocess.run(
            ['bash', start_path] + _start_arg_list(instance_config),
            stdout=stdout,
            stderr=subprocess.STDOUT,
            text=True
        )
        if output.returncode != 0:
            print(output.stdout)


def stop_instance(instance_config: InstanceConfig, stdout=subprocess.PIPE):
    with resources.path(f'sclients.bin', f'{instance_config.client}_stop') as stop_path:
        output = subprocess.run(
            ['bash', stop_path],
            stdout=stdout,
            stderr=subprocess.STDOUT,
            text=True
        )
        if output.returncode != 0:
            print(output.stdout)
