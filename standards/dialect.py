from __future__ import annotations
from typing import List, Union, Optional
from .model import Model


class Control(Model):
    name: Optional[str] = None
    # type: implicit
    title: Optional[str] = None
    description: Optional[str] = None


class CsvControl(Control):
    delimiter: Optional[str] = None
    lineTerminator: Optional[str] = None
    quoteChar: Optional[str] = None
    doubleQuote: Optional[bool] = None
    escapeChar: Optional[str] = None
    nullSequence: Optional[str] = None
    skipInitialSpace: Optional[bool] = None


class JsonControl(Control):
    keys: Optional[List[str]] = None
    keyed: Optional[bool] = None
    property: Optional[str] = None


class ExcelControl(Control):
    sheet: Optional[Union[str, int]] = None
    fillMergedCells: Optional[bool] = None
    preserveFormatting: Optional[bool] = None
    adjustFloatingPointError: Optional[bool] = None
    stringified: Optional[bool] = None


class Dialect(Model):
    name: Optional[str] = None
    type: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    header: Optional[bool] = None
    headerRows: Optional[List[int]] = None
    headerJoin: Optional[str] = None
    headerCase: Optional[bool] = None
    commentChar: Optional[str] = None
    commentRows: Optional[List[int]] = None
    skipBlankRows: Optional[bool] = None
    csv: Optional[CsvControl] = None
    _json: Optional[JsonControl] = None
    excel: Optional[ExcelControl] = None
