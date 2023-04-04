from __future__ import annotations
from ...package import Package
from .model import CkanModel


class CkanPackage(CkanModel):
    ckan_name: str

    # Mappers

    def to_frictionless(self) -> Package:
        package = Package(resources=[])
        package.name = self.ckan_name
        return package
