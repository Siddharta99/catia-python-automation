import csv

def load_parts(filename):
    parts = []
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                row["qty"] = int(row["qty"])
            except:
                row["qty"] = 0
                print("warning")
            row["length_mm"] = int(row["length_mm"])
            parts.append(row)
    return parts

def count_heavy_parts(parts, threshold):
    count = 0
    for part in parts:
        if part["qty"] > threshold:
            count = count + 1
    return count

def get_heavy_parts(parts, threshold):
    matches = []
    for part in parts:
        if part["qty"] > threshold:
            matches.append(part["name"])
    return matches

def analyze_heavy_parts(parts, threshold):
    matches = []
    for part in parts:
        if part["qty"] > threshold:
            matches.append(part["name"])
    return {"count": len(matches), "names": matches}

def get_parts_by_material(parts, material):
    matches = []
    for part in parts:
        if part["material"] == material:
            matches.append(part["name"])
    return matches

def get_parts_by_length(parts, min_length):
    matches = []
    for part in parts:
        if part["length_mm"] > min_length:
            matches.append(part["name"])
    return matches

def get_parts_by_qty_range(parts, min_qty, max_qty):
    matches = []
    for part in parts:
        if part["qty"] >= min_qty and part["qty"] <= max_qty:
            matches.append(part["name"])
    return matches

def get_total_qty(parts):
    total = 0
    for part in parts:
        total = total + part["qty"]
    return total

def get_total_length_mm(parts):
    total = 0
    for part in parts:
        total = total + part["length_mm"]
    return total

# --- example usage ---
result = load_parts("machine_log.csv")
sorted_parts = sorted(result, key=lambda part: part["length_mm"])
for part in sorted_parts:
    print(part["name"], part["length_mm"])