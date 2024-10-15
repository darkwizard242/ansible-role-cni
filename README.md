[![build-test](https://github.com/darkwizard242/ansible-role-cni/workflows/build-and-test/badge.svg?branch=master)](https://github.com/darkwizard242/ansible-role-cni/actions?query=workflow%3Abuild-and-test) [![release](https://github.com/darkwizard242/ansible-role-cni/workflows/release/badge.svg)](https://github.com/darkwizard242/ansible-role-cni/actions?query=workflow%3Arelease) ![Ansible Role](https://img.shields.io/ansible/role/d/darkwizard242/cni) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-cni&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=ansible-role-cni) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-cni&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=ansible-role-cni) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-cni&metric=security_rating)](https://sonarcloud.io/dashboard?id=ansible-role-cni) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-cni?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-cni?color=orange&style=flat-square)

# Ansible Role: cni

Role to install (_by default_) [cni](https://github.com/containernetworking/plugins) plugins on **Debian/Ubuntu** and **EL** systems to support Kubernetes Cluster setup.

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables list:

```yaml
cni_app: cni
cni_version: 1.6.0
cni_os: linux
cni_arch: amd64
cni_dl_url: "https://github.com/containernetworking/plugins/releases/download/v{{ cni_version }}/cni-plugins-{{ cni_os }}-{{ cni_arch }}-v{{ cni_version }}.tgz"
cni_plugins_dir: /opt/cni/bin
cni_plugins_dir_mode: '0755'
```

### Variables table:

Variable             | Description
-------------------- | --------------------------------------------------------------------------------------------------------------------------------
cni_app              | Defines the app to install i.e. **cni**
cni_version          | Defined to dynamically fetch the desired version to install. Defaults to: **1.6.0**
cni_os               | Defines OS type. Defaults to: **linux**
cni_arch             | Defines os architecture. Used for obtaining the correct type of binaries based on OS System Architecture. Defaults to: **amd64**
cni_dl_url           | Defines URL to download the cni binaries archive from.
cni_plugins_dir      | Defined to dynamically set the appropriate path to store cni binaries into.
cni_plugins_dir_mode | Mode for the binaries file of cni.

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **cni**) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.cni
```

For customizing behavior of role (i.e. specifying the desired **cni** version) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.cni
  vars:
    cni_version: 1.0.0
```

For customizing behavior of role (i.e. setting filemode for binaries of **cni**) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.cni
  vars:
    cni_file_mode: '0775'
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-cni/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.alimuhammad.dev/)
