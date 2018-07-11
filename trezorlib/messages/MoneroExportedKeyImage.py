# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p


class MoneroExportedKeyImage(p.MessageType):
    FIELDS = {
        1: ('iv', p.BytesType, 0),
        2: ('tag', p.BytesType, 0),
        3: ('blob', p.BytesType, 0),
    }

    def __init__(
        self,
        iv: bytes = None,
        tag: bytes = None,
        blob: bytes = None,
    ) -> None:
        self.iv = iv
        self.tag = tag
        self.blob = blob
