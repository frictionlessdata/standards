from __future__ import annotations
from typing import List, Optional
from .model import Model
from .resource import Resource


class Package(Model):
    name: Optional[str] = None
    type: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    resources: List[Resource]
