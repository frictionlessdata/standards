from __future__ import annotations
from typing import List, Any, Dict
from typing_extensions import Required, TypedDict, Literal
from .dialect import IDialect
from .schema import ISchema


class IResource(TypedDict, total=False):
    name: Required[str]
    #  type: required
    title: str
    description: str
    path: str
    data: Any
    scheme: str
    format: str
    compression: str
    extrapaths: List[str]
    innerpath: str
    encoding: str
    dialect: IDialect


class IFileResource(IResource, total=False):
    type: Required[Literal["file"]]


class ITextResource(IResource, total=False):
    type: Required[Literal["text"]]


class IJsonResource(IResource, total=False):
    type: Required[Literal["json"]]
    schema: Dict[str, Any]  # Json Schema


class ITableResource(IResource, total=False):
    type: Required[Literal["table"]]
    schema: ISchema  # Table Schema
