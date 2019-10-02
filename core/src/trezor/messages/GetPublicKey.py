# Automatically generated by pb2py
# fmt: off
import protobuf as p

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
        EnumTypeInputScriptType = Literal[0, 1, 2, 3, 4]
    except ImportError:
        pass


class GetPublicKey(p.MessageType):
    MESSAGE_WIRE_TYPE = 11

    def __init__(
        self,
        address_n: List[int] = None,
        ecdsa_curve_name: str = None,
        show_display: bool = None,
        coin_name: str = None,
        script_type: EnumTypeInputScriptType = None,
    ) -> None:
        self.address_n = address_n if address_n is not None else []
        self.ecdsa_curve_name = ecdsa_curve_name
        self.show_display = show_display
        self.coin_name = coin_name
        self.script_type = script_type

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('address_n', p.UVarintType, p.FLAG_REPEATED),
            2: ('ecdsa_curve_name', p.UnicodeType, 0),
            3: ('show_display', p.BoolType, 0),
            4: ('coin_name', p.UnicodeType, 0),  # default=Bitcoin
            5: ('script_type', p.EnumType("InputScriptType", (0, 1, 2, 3, 4)), 0),  # default=SPENDADDRESS
        }
