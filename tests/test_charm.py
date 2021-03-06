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

# Learn more about testing at: https://juju.is/docs/sdk/testing

import unittest

from charm import ZookeeperDummyClientK8SCharm
from ops.testing import Harness


class TestCharm(unittest.TestCase):
    def setUp(self):
        self.harness = Harness(ZookeeperDummyClientK8SCharm)
        self.addCleanup(self.harness.cleanup)
        self.harness.begin()
