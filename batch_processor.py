import glob
import pandas as pd

from parts_checker import (
    get_heavy_parts,
    get_total_qty,
    get_total_length_mm,
    summarize_by_material,
)


def load_all_logs(folder):
    """Read every CSV in a folder and combine them into one DataFrame.

    Adds a 'source_file' column so we can trace each row back to
    which file (which "part batch") it came from.
    """
    all_files = glob.glob(f"{folder}/*.csv")
    frames = []

    for filepath in all_files:
        df = pd.read_csv(filepath)
        df["source_file"] = filepath.split("/")[-1].split("\\")[-1]  # just the filename
        frames.append(df)

    combined = pd.concat(frames, ignore_index=True)
    return combined


# --- example usage ---
if __name__ == "__main__":
    df = load_all_logs("batch_data")

    print(f"Loaded {len(df)} rows from multiple files\n")

    print("Total qty across all files:", get_total_qty(df))
    print("Total length across all files:", get_total_length_mm(df))

    print("\nHeavy parts (qty > 20) across all files:")
    print(get_heavy_parts(df, 20))

    print("\nSummary by material (across ALL files combined):")
    print(summarize_by_material(df))

    # Bonus: which file contributed the most parts?
    print("\nRow count per source file:")
    print(df["source_file"].value_counts())

    df.to_csv("combined_batch_report.csv", index=False)
