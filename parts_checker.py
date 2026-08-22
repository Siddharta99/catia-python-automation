import pandas as pd


def load_parts(filename):
    """Load part data from CSV into a DataFrame."""
    df = pd.read_csv(filename)
    return df


def count_heavy_parts(df, threshold):
    """Count parts with qty greater than threshold."""
    return (df["qty"] > threshold).sum()


def get_heavy_parts(df, threshold):
    """Return names of parts with qty greater than threshold."""
    return df.loc[df["qty"] > threshold, "name"].tolist()


def analyze_heavy_parts(df, threshold):
    """Return count + names of parts with qty greater than threshold."""
    matches = df.loc[df["qty"] > threshold, "name"]
    return {"count": len(matches), "names": matches.tolist()}


def get_parts_by_material(df, material):
    """Return names of parts matching a given material."""
    return df.loc[df["material"] == material, "name"].tolist()


def get_parts_by_length(df, min_length):
    """Return names of parts longer than min_length."""
    return df.loc[df["length_mm"] > min_length, "name"].tolist()


def get_parts_by_qty_range(df, min_qty, max_qty):
    """Return names of parts with qty within [min_qty, max_qty]."""
    mask = (df["qty"] >= min_qty) & (df["qty"] <= max_qty)
    return df.loc[mask, "name"].tolist()


def get_total_qty(df):
    """Sum all part quantities."""
    return df["qty"].sum()


def get_total_length_mm(df):
    """Sum all part lengths."""
    return df["length_mm"].sum()


def summarize_by_material(df):
    """Group parts by material: total qty and average length per group."""
    return df.groupby("material").agg(
        total_qty=("qty", "sum"),
        avg_length_mm=("length_mm", "mean"),
        part_count=("name", "count"),
    ).reset_index()


# --- example usage ---
if __name__ == "__main__":
    df = load_parts("machine_log.csv")

    sorted_df = df.sort_values("length_mm")
    print(sorted_df[["name", "length_mm"]])

    print("\nHeavy parts (qty > 20):", get_heavy_parts(df, 20))
    print("Total qty:", get_total_qty(df))

    print("\nSummary by material:")
    print(summarize_by_material(df))

    summarize_by_material(df).to_csv("material_summary.csv", index=False)
