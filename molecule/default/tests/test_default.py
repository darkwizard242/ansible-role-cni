import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


BINARIES_DIR = '/opt/cni/bin/'
BINARIES = ['bandwidth', 'bridge', 'dhcp', 'firewall', 'host-device',
            'host-local', 'ipvlan', 'loopback', 'macvlan', 'portmap', 'ptp',
            'sbr', 'static', 'tuning', 'vlan', 'vrf']


def test_cni_binaries_exists(host):
    for BINARY in BINARIES:
        """
        Tests if cni binaries exist.
        """
        assert host.file(BINARIES_DIR + BINARY).exists


def test_cni_binaries_file(host):
    for BINARY in BINARIES:
        """
        Tests if cni binaries are a file type.
        """
        assert host.file(BINARIES_DIR + BINARY).is_file
