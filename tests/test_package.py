from standards import Package


def test_package():
    package = Package(name="name", resources=[])
    assert package.name == "name"
