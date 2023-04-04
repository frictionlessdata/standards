from __future__ import annotations
import attrs
import pydantic
from typing import Type, Dict, Any
from typing_extensions import TypedDict


@attrs.define(kw_only=True)
class Standard:
    definition: Type[TypedDict]

    def to_jsonschema(self) -> Dict[str, Any]:
        atype = pydantic.AnalyzedType(self.definition)
        return atype.json_schema()
