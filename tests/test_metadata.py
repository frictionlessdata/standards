from standards import Standard, ISchema


def test_standard():
    schema = Standard(definition=ISchema)
    assert schema.to_jsonschema()
