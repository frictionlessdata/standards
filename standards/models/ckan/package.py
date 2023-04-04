from __future__ import annotations
from typing_extensions import TypedDict, Required


class IPackage(TypedDict, total=False):
    ckan_name: Required[str]
