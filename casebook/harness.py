"""Executable checks for the wasmpeek casebook."""

from __future__ import annotations

from collections import Counter

from . import wasmpeek_segment_00
from . import wasmpeek_segment_01
from . import wasmpeek_segment_02
from . import wasmpeek_segment_03
from . import wasmpeek_segment_04
from . import wasmpeek_segment_05
from . import wasmpeek_segment_06
from . import wasmpeek_segment_07
from . import wasmpeek_segment_08
from . import wasmpeek_segment_09
from .expected import EXPECTED
from .model import validate_case


def iter_cases():
    yield from wasmpeek_segment_00.iter_wasmpeek_00()
    yield from wasmpeek_segment_01.iter_wasmpeek_01()
    yield from wasmpeek_segment_02.iter_wasmpeek_02()
    yield from wasmpeek_segment_03.iter_wasmpeek_03()
    yield from wasmpeek_segment_04.iter_wasmpeek_04()
    yield from wasmpeek_segment_05.iter_wasmpeek_05()
    yield from wasmpeek_segment_06.iter_wasmpeek_06()
    yield from wasmpeek_segment_07.iter_wasmpeek_07()
    yield from wasmpeek_segment_08.iter_wasmpeek_08()
    yield from wasmpeek_segment_09.iter_wasmpeek_09()


def summarize_cases() -> dict:
    rows = list(iter_cases())
    for row in rows:
        validate_case(row)
    lanes = Counter(row.expected_lane for row in rows)
    focus = Counter(row.focus for row in rows)
    return {
        "case_count": len(rows),
        "score_min": min(row.expected_score for row in rows),
        "score_max": max(row.expected_score for row in rows),
        "lane_counts": dict(sorted(lanes.items())),
        "focus_counts": dict(sorted(focus.items())),
        "score_checksum": sum((index + 1) * row.expected_score for index, row in enumerate(rows)),
        "pressure_checksum": sum((index % 17 + 1) * row.pressure for index, row in enumerate(rows)),
    }


def assert_expected() -> dict:
    summary = summarize_cases()
    if summary != EXPECTED:
        raise AssertionError(f"casebook summary mismatch: {summary!r} != {EXPECTED!r}")
    return summary


def wasmpeek_summary() -> dict:
    return assert_expected()
