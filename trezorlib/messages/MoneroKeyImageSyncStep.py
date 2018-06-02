# Automatically generated by pb2py
from .. import protobuf as p
if __debug__:
    try:
        from typing import List
    except ImportError:
        List = None
from .MoneroTransferDetails import MoneroTransferDetails


class MoneroKeyImageSyncStep(p.MessageType):
    FIELDS = {
        1: ('tdis', MoneroTransferDetails, p.FLAG_REPEATED),
    }

    def __init__(
        self,
        tdis: List[MoneroTransferDetails] = None
    ) -> None:
        self.tdis = tdis if tdis is not None else []
