"""Base classes for implementing protocol-specific clients.

"""

from __future__ import annotations

import asyncio
from dataclasses import dataclass, field
import concurrent.futures
from enum import Enum, auto
from typing import Optional


class QueryType(Enum):
    READ = auto()
    WRITE = auto()
    PARALLEL = auto()

class ExecutionMode(Enum):
    SYNC = auto()
    ASYNC = auto()


class ConnectionsNotAllowedError(Exception):
    pass

class QueryRetriesExceededError(ConnectionError):
    pass

class ConnectionErrorRetry(ConnectionError):
    pass

def api(f):
    return f

def parse_url_authority(url):
    pass

def krb_client_server_auth(servername, host, clientname):
    pass

def bytes_postprocessor(bytesdata, *, bytes_encoding="utf-8"):
    pass

def frame_postprocessor(
        df,
        *,
        typed_cols={},
        datetime_cols={},
        timedelta_cols=(),
        numeric_cols=(),
        infer_objects=True,
        convert_dtypes=True,
        transformed_cols={},
        bytes_encoding="utf-8",
        convert_tranposed_series=True
):
    pass


def _cancel_thread(tid, exctype):
    pass


@dataclass
class Query:
    value: QueryNativeT
    type: QueryType
    rawresult: Optional[QueryRawResultT] = field(
        default=None, hash=False, compare=False
    )
    id: str = field(default="", hash=False, compare=False)
