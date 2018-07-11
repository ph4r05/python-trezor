# This file is part of the TREZOR project.
#
# This library is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this library.  If not, see <http://www.gnu.org/licenses/>.
import pytest

from .common import TrezorTest
from .conftest import TREZOR_VERSION
from trezorlib import stellar
from trezorlib import monero
from trezorlib.tools import parse_path
import binascii

#@pytest.mark.xfail(TREZOR_VERSION == 2, reason="T2 support is not yet finished")
@pytest.mark.monero
class TestMsgMoneroGetWatchOnly(TrezorTest):

    def test_monero_get_address(self):
        self.setup_mnemonic_nopin_nopassphrase()

        response = self.client.monero_get_watch_only(parse_path(monero.DEFAULT_BIP32_PATH))
        assert response.address == b'49zNnuxjZFtDERsJHTNgMg3KpxLA8oUWbLqaEm6P1FL8U2eicixSZEnbR6J5DkV9xLfepggB9VZa7C3wcucjETo2UhKgnnW'
        assert binascii.hexlify(response.watch_key) == b'6f5417180f7c4c6742b0c7d0e8ba8e465bb892ee199d4b1d0bce857319681a0c'
