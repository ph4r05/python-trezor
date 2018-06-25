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


#@pytest.mark.xfail(TREZOR_VERSION == 2, reason="T2 support is not yet finished")
@pytest.mark.monero
class TestMsgMoneroGetAddress(TrezorTest):

    def test_monero_get_address(self):
        self.setup_mnemonic_nopin_nopassphrase()

        response = self.client.monero_get_address(parse_path(monero.DEFAULT_BIP32_PATH))
        assert response.address == b'45PwgoUKaDHNqLL8o3okzLL7biv7GqPVmd8LTcTrYVrMEKdSYwFcyJfMLSRpfU3nh8Z2m81FJD4sUY3nXCdGe61k1HAp8T1'
