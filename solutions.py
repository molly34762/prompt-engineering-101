from names import class_names
import time

# ─────────────────────────────────────────────
# APPROACH 1: Nested Loops  — O(n²) time, O(1) space
# ─────────────────────────────────────────────
def find_duplicates_nested(names):
    duplicates = []
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            if names[i] == names[j] and names[i] not in duplicates:
                duplicates.append(names[i])
    return duplicates


# ─────────────────────────────────────────────
# APPROACH 2: Sort then Scan  — O(n log n) time, O(1) extra space
# ─────────────────────────────────────────────
def find_duplicates_sort(names):
    sorted_names = sorted(names)
    duplicates = []
    for i in range(1, len(sorted_names)):
        if sorted_names[i] == sorted_names[i - 1] and sorted_names[i] not in duplicates:
            duplicates.append(sorted_names[i])
    return duplicates


# ─────────────────────────────────────────────
# APPROACH 3: Hash Set  — O(n) time, O(n) space
# ─────────────────────────────────────────────
def find_duplicates_hashset(names):
    seen = set()
    duplicates = set()
    for name in names:
        if name in seen:
            duplicates.add(name)
        else:
            seen.add(name)
    return list(duplicates)


# ─────────────────────────────────────────────
# Run all three and compare
# ─────────────────────────────────────────────
if __name__ == "__main__":
    approaches = [
        ("Nested Loops  — O(n²)",     find_duplicates_nested),
        ("Sort + Scan  — O(n log n)", find_duplicates_sort),
        ("Hash Set     — O(n)",       find_duplicates_hashset),
    ]

    print(f"Class roster ({len(class_names)} students): {class_names}\n")

    for label, fn in approaches:
        start = time.perf_counter()
        result = fn(class_names)
        elapsed = (time.perf_counter() - start) * 1e6  # microseconds
        print(f"{label}")
        print(f"  Duplicates : {sorted(result)}")
        print(f"  Time       : {elapsed:.2f} µs\n")
