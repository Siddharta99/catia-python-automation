import pandas as pd
from pycatia import catia

caa = catia()

document = caa.active_document
part = document.part
print(part.name)

parameters = part.parameters


def get_parameter_records(parameters):
    """Pull every numeric parameter into a list of dicts (name, value)."""
    records = []
    for param in parameters:
        try:
            value = param.value
            if isinstance(value, (int, float)) and not isinstance(value, bool):
                records.append({"parameter": param.name, "value": value})
        except:
            pass
    return records


def flag_by_keyword(df, keyword, max_value):
    """Return rows where the parameter name contains keyword and value < max_value."""
    mask = df["parameter"].str.contains(keyword) & (df["value"] < max_value)
    return df.loc[mask]


# --- build the full parameter table ---
records = get_parameter_records(parameters)
df = pd.DataFrame(records)

# --- apply flags ---
radius_flags = flag_by_keyword(df, "Radius", 2.5)
length_flags = flag_by_keyword(df, "Length", 10)

flagged = pd.concat([radius_flags, length_flags], ignore_index=True)
print(flagged)

flagged.to_csv("flagged_report.csv", index=False)
