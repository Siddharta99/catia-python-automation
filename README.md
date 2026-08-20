# CATIA Part Data Automation Toolkit

Python scripts that connect to CATIA V5, read live part/parameter data,
flag out-of-spec values, and export results to a CSV report — built as
part of transitioning from mechanical design engineering into CATIA
automation + Python.

## What it does

- **parts_checker.py** — Core data-processing functions (filter, count,
  sort, sum) tested against CSV part data. Simulates the shape of real
  CATIA export data.
- **catia_reader.py** — Connects to a live, running CATIA V5 session via
  `pycatia`, reads all parameters from the active part, filters them
  by keyword and value threshold (e.g. "flag any Radius under 2.5mm"),
  and writes flagged results to `flagged_report.csv`.

## Example

Running `catia_reader.py` on a part called `Round_Locator` flagged:

| Parameter | Value |
|---|---|
| Inner_diameter\Sketch.2\Radius.1\Radius | 2.0 |
| Resting_Rib\EdgeFillet.1\CstEdgeRibbon.1\Radius | 1.0 |

## Requirements

- CATIA V5 (script connects to a currently open session)
- `pip install pycatia`

## Usage

1. Open a part in CATIA V5
2. Run `catia_reader.py`
3. Check `flagged_report.csv` for any parameters below your threshold

## Background

Built while transitioning from a mechanical design engineering role
into CATIA automation scripting, applying Python fundamentals directly
to real CATIA part data.