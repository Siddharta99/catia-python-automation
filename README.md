# CATIA Part Data Automation Toolkit

Python scripts that connect to CATIA V5, read live part/parameter data,
flag out-of-spec values using pandas, and export results to CSV reports —
built as part of transitioning from mechanical design engineering into
CATIA automation + Python.

## What it does

- **catia_reader.py** — Connects to a live, running CATIA V5 session via
  `pycatia`, pulls all numeric parameters from the active part into a
  pandas DataFrame, flags values by keyword and threshold (e.g. "any
  Radius under 2.5mm"), and writes flagged results to `flagged_report.csv`.
- **parts_checker.py** — pandas-based data-processing functions (filter,
  count, sort, sum, group-by-material summary) tested against CSV part
  data. Simulates the shape of real CATIA export data.
- **batch_processor.py** — Combines multiple CSV exports (e.g. from
  several parts or machine batches, stored in `batch_data/`) into a
  single dataset using pandas, then reuses the same filtering/summary
  functions from `parts_checker.py` across all of them at once.
  Exports results to both CSV and Excel (`.xlsx`) formats.
  Demonstrates scaling from single-part checks to project-wide analysis.
  

## Example

Running `catia_reader.py` on a part called `Round_Locator` flagged:

| Parameter | Value |
|---|---|
| Inner_diameter\Sketch.2\Radius.1\Radius | 2.0 |
| Resting_Rib\EdgeFillet.1\CstEdgeRibbon.1\Radius | 1.0 |
| Resting_Rib\Pad.3\SecondLimit\Length | 0.0 |

Running `batch_processor.py` on three sample machine logs combined
373 total quantity across 15 parts and summarized totals by material
(Steel, Aluminum, Plastic) in a single report.

## Requirements

- CATIA V5 (only needed for `catia_reader.py`, which connects to a
  currently open session)
- `pip install pycatia pandas`

## Usage

**Single-part parameter check:**
1. Open a part in CATIA V5 and make sure its window is focused
2. Run `catia_reader.py`
3. Check `flagged_report.csv` for any parameters below your threshold

**Batch processing across multiple files:**
1. Place CSV exports in the `batch_data/` folder
2. Run `batch_processor.py`
3. Check `combined_batch_report.csv` or `combined_batch_report.xlsx` for the combined summary

## Background

Built while transitioning from a mechanical design engineering role
into CATIA automation scripting — starting with plain Python loops,
then rebuilt on pandas for cleaner filtering, aggregation (e.g.
summarizing parts by material), and scaling to multi-part/batch
workflows.
