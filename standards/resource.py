from __future__ import annotations
from typing import List, Any, Dict, Optional
from typing_extensions import Literal
from .model import Model
from .dialect import Dialect
from .schema import Schema


class Resource(Model):
    name: str
    type: str
    title: Optional[str] = None
    description: Optional[str] = None
    path: Optional[str] = None
    data: Optional[Any] = None
    scheme: Optional[str] = None
    format: Optional[str] = None
    compression: Optional[str] = None
    extrapaths: Optional[List[str]] = None
    innerpath: Optional[str] = None
    encoding: Optional[str] = None
    dialect: Optional[Dialect] = None


class FileResource(Resource):
    type: Literal["file"]


class TextResource(Resource):
    type: Literal["text"]


class JsonResource(Resource):
    type: Literal["json"]
    _schema: Optional[Dict[str, Any]] = None  # Json Schema


class TableResource(Resource):
    type: Literal["table"]
    _schema: Optional[Schema] = None  # Table Schema
