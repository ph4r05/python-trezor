# Automatically generated by pb2py
from .. import protobuf as p
if __debug__:
    try:
        from typing import List
    except ImportError:
        List = None


class MoneroGetKey(p.MessageType):
    MESSAGE_WIRE_TYPE = 334
    FIELDS = {
        1: ('address_n', p.UVarintType, p.FLAG_REPEATED),
        2: ('network_type', p.UVarintType, 0),
    }

    def __init__(
        self,
        address_n: List[int] = None,
        network_type: int = None
    ) -> None:
        self.address_n = address_n if address_n is not None else []
        self.network_type = network_type
