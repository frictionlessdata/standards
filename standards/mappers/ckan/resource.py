from __future__ import annotations
from ...resource import Resource
from .model import CkanModel


class CkanResource(CkanModel):
    ckan_name: str

    # Mappers

    def to_frictionless(self) -> Resource:
        resource = Resource(name=self.ckan_name, type="file")
        return resource
