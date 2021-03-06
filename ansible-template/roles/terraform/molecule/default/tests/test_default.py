import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_terraform_binary_exists(host):
    assert host.file('/usr/local/bin/terraform').exists


def test_terraform_binary_file(host):
    assert host.file('/usr/local/bin/terraform').is_file


def test_terraform_binary_which(host):
    assert host.check_output('which terraform') == '/usr/local/bin/terraform'
