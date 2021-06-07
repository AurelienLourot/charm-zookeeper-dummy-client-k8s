#!/usr/bin/env python3
# Copyright 2021 Canonical Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Learn more at: https://juju.is/docs/sdk

"""Charm the service.

Refer to the following post for a quick-start guide that will help you
develop a new k8s charm using the Operator Framework:

    https://discourse.charmhub.io/t/4208
"""

import logging

from contextlib import contextmanager

from charms.zookeeper_k8s.v0.zookeeper import (
    ZookeeperRelationCharmEvents, ZookeeperRequires)
from kazoo.client import KazooClient
from ops.charm import CharmBase
from ops.framework import StoredState
from ops.main import main
from ops.model import ActiveStatus

logger = logging.getLogger(__name__)


class ZookeeperDummyClientK8SCharm(CharmBase):
    on = ZookeeperRelationCharmEvents()
    _stored = StoredState()

    def __init__(self, *args):
        super().__init__(*args)
        self.zookeeper = ZookeeperRequires(self, self._stored)
        self.framework.observe(self.on.zookeeper_relation_updated,
                               self._on_zookeeper_config_changed)

    def _on_zookeeper_config_changed(self, _):
        hosts = self.__known_zookeeper_hosts()
        logging.debug(f'Known zookeeper hosts: {hosts}')
        with self.__zookeeper_client(hosts) as _:
            self.unit.status = ActiveStatus()

    @contextmanager
    def __zookeeper_client(self, hosts):
        zk = KazooClient(hosts=hosts)
        zk.start()
        try:
            yield zk
        finally:
            zk.stop()

    def __known_zookeeper_hosts(self):
        """Return list of hosts to pass to the zookeeper client.
        """
        return ','.join(f'{address}:{self._stored.zookeeper_port}' for
                        address in self._stored.zookeeper_addresses)


if __name__ == "__main__":
    main(ZookeeperDummyClientK8SCharm)
