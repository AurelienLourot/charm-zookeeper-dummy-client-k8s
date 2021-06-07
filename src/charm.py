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

from kazoo.client import KazooClient
from ops.charm import CharmBase
from ops.framework import StoredState
from ops.main import main
from ops.model import ActiveStatus

logger = logging.getLogger(__name__)


class ZookeeperDummyClientK8SCharm(CharmBase):
    _stored = StoredState()

    def __init__(self, *args):
        super().__init__(*args)
        self.framework.observe(self.on.zookeeper_pebble_ready,
                               self._on_zookeeper_pebble_ready)

        self._stored.set_default(things=[])  # FIXME

    def _on_zookeeper_pebble_ready(self, _):
        self.unit.status = ActiveStatus()

    @contextmanager
    def __zookeeper_client(self):
        client_port = self.config[self.__CLIENT_PORT_CONFIG_KEY]
        zk = KazooClient(hosts='127.0.0.1:{}'.format(client_port))
        zk.start()
        try:
            yield zk
        finally:
            zk.stop()


if __name__ == "__main__":
    main(ZookeeperDummyClientK8SCharm)
