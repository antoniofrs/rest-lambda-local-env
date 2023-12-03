from dataclasses import dataclass
from enum import Enum

class HttpMethod(Enum):
    GET = "get"
    POST = "post"
    PATCH = "patch"
    PUT = "put"
    DELETE = "delete"

@dataclass
class Route:
    http_method: HttpMethod
    path: str
    function: str