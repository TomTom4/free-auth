from typing import Optional, List, Literal, Union
from pydantic import BaseModel, HttpUrl, Field
from jwcrypto import jwk
import json


class JWK(BaseModel):
    use: Optional[Literal["sig", "enc"]] = None
    key_ops: Optional[
        Literal[
            "sign",
            "verify",
            "encrypt",
            "decrypt",
            "wrapKey",
            "unwrapKey",
            "deriveKey",
            "deriveBits",
        ]
    ] = None
    alg: Optional[str] = None
    kid: Optional[str] = None
    x5u: Optional[HttpUrl] = None
    x5c: Optional[str] = None
    x5t: Optional[str] = None
    x5tS256: Optional[str] = Field(default=None, alias="x5t#256")


class ElipticCurveJWK(JWK):
    kty: Literal["EC"] = "EC"
    crv: Literal["P-256", "P-384", "P-521"]
    x: str
    y: Optional[str] = None


class PrivateElipticCurveJWK(ElipticCurveJWK):
    d: str


class RSAJWK(JWK):
    kty: Literal["RSA"] = "RSA"
    n: str
    e: str


class PrivateRSAJWK(RSAJWK):
    d: str
    p: str
    q: str
    dp: str
    dq: str
    qi: str
    oth: str


class JWKS(BaseModel):
    keys: List[Union[ElipticCurveJWK, PrivateElipticCurveJWK, RSAJWK, PrivateRSAJWK]]


def build_jwk():
    with open("public.pem", "rb") as pemfile:
        key = jwk.JWK.from_pem(pemfile.read())
    dict_key: dict = json.loads(key.export())
    return ElipticCurveJWK.model_validate(dict_key)
