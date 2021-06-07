# zookeeper-k8s

[![Charmhub](https://img.shields.io/badge/Charmhub-orange)](https://charmhub.io/zookeeper-dummy-client-k8s)
[![GitHub](https://img.shields.io/badge/GitHub-orange)](https://github.com/AurelienLourot/charm-zookeeper-dummy-client-k8s)

## Description

This [Juju Charmed Operator](https://juju.is/docs) deploys a dummy client for
[zookeeper-k8s](https://charmhub.io/zookeeper-k8s). It is implemented using the
[Charmed Operator Framework](https://juju.is/docs/sdk), designed to deploy a
standard [OCI](https://opencontainers.org/) (e.g. Docker) image alongside a
sidecar container containing the Juju operator logic.

## Usage

### Deploying

```
$ juju add-model myzookeeper
$ juju deploy zookeeper-k8s -n 3
$ juju deploy zookeeper-dummy-client k8s
$ juju add-relation zookeeper-k8s:client zookeeper-dummy-client-k8s:zookeeper
```

### Inspecting

```
$ juju status
Model        Controller  Cloud/Region        Version  SLA          Timestamp
myzookeeper  micro       microk8s/localhost  2.9.0    unsupported  12:27:29Z

App                         Version  Status  Scale  Charm                       Store     Channel  Rev  OS          Address  Message
zookeeper-k8s                        active      3  zookeeper-k8s               charmhub  stable     4  kubernetes
zookeeper-dummy-client-k8s           active      1  zookeeper-dummy-client-k8s  charmhub  stable     3  kubernetes

Unit                           Workload  Agent  Address    Ports  Message
zookeeper-k8s/0                active    idle   10.1.0.47
zookeeper-k8s/1*               active    idle   10.1.0.49
zookeeper-k8s/2                active    idle   10.1.0.48
zookeeper-dummy-client-k8s/0*  active    idle   10.1.0.55
```

## Developing

Create and activate a virtualenv with the development requirements:

```
$ git clone https://github.com/AurelienLourot/charm-zookeeper-dummy-client-k8s
$ cd charm-zookeeper-dummy-client-k8s/
$ virtualenv -p python3 venv
$ source venv/bin/activate
$ pip install -r requirements-dev.txt
```

### Testing

The Python operator framework includes a very nice harness for testing
operator behaviour without full deployment. Just `run_tests`:

```
$ ./run_tests
```

### Deploying from source

```
$ charmcraft pack
$ juju deploy ./zookeeper-dummy-client-k8s.charm --resource ubuntu-image=ubuntu
```
