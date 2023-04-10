import pytest
from standards import mappers


@pytest.mark.skip
def test_resource():
    source = mappers.ckan.CkanPackage(ckan_name="name")
    target = source.to_frictionless()
    assert target.name == "name"
