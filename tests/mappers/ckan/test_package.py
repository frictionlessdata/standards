from standards import mappers


def test_package():
    source = mappers.ckan.CkanPackage(ckan_name="name")
    target = source.to_frictionless()
    assert target.name == "name"
