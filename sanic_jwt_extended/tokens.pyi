# Stubs for tokens (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import datetime
import uuid
from typing import Any, Dict, Optional

class Token:
    raw_jwt: str
    raw_data: Dict[str, Any] = ...
    type: str = ...
    role: Optional[str] = ...
    fresh: Optional[bool] = ...
    identity: str = ...
    csrf: str = ...
    iss: Optional[str] = ...
    sub: str = ...
    aud: Optional[str] = ...
    exp: Optional[datetime.datetime] = ...
    nbf: datetime.datetime = ...
    iat: datetime.datetime = ...
    jti: uuid.UUID = ...
    public_claims: Dict[str, Any] = ...
    private_claims: Dict[str, Any] = ...
    def __post_init__(self) -> None: ...
    def _get_private_claims(self) -> Dict[str, Any]: ...
    def _get_public_claims(self) -> Dict[str, Any]: ...
    def _get_type(self) -> str: ...
    def _decode_jwt(self) -> Dict[str, Any]: ...
    def __init__(self, raw_jwt: Any) -> None: ...
    async def revoke(self, token: Token): ...

