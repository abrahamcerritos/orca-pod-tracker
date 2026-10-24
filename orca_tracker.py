import json
from datetime import date, datetime

DATA_FILE = "orcas.json"


def load_data():
    """Read orcas.json and return it as a Python dictionary."""
    with open(DATA_FILE, "r") as file:
        return json.load(file)


def save_data(data):
    """Write the data back to orcas.json."""
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=2)


def list_orcas(data):
    """Print every orca in a simple table."""
    print("\nID    Name          Pod  Sex     Born")
    print("-" * 40)
    for orca in data["orcas"]:
        print(f"{orca['id']:<6}{orca['name']:<14}{orca['pod']:<5}"
              f"{orca['sex']:<8}{orca['birth_year']}")


def search_orcas(data):
    """Find orcas by ID or name (not case-sensitive)."""
    term = input("Enter an ID or name to search: ").strip().lower()
    matches = [
        orca for orca in data["orcas"]
        if term in orca["id"].lower() or term in orca["name"].lower()
    ]

    if not matches:
        print("No orcas found.")
        return

    for orca in matches:
        print(f"{orca['id']} - {orca['name']} ({orca['pod']} pod, "
              f"{orca['sex']}, born {orca['birth_year']})")


def log_sighting(data):
    """Record a sighting of a known orca and save it."""
    orca_id = input("Orca ID (e.g. J35): ").strip().upper()
    valid_ids = [orca["id"] for orca in data["orcas"]]
    if orca_id not in valid_ids:
        print(f"Unknown ID. Valid IDs: {', '.join(valid_ids)}")
        return

    date_input = input("Date (YYYY-MM-DD, press Enter for today): ").strip()
    if date_input == "":
        sighting_date = date.today().isoformat()
    else:
        try:
            datetime.strptime(date_input, "%Y-%m-%d")
            sighting_date = date_input
        except ValueError:
            print("Invalid date format.")
            return

    location = input("Location (e.g. Haro Strait): ").strip()
    if location == "":
        print("Location can't be empty.")
        return

    data["sightings"].append({
        "orca_id": orca_id,
        "date": sighting_date,
        "location": location
    })
    save_data(data)
    print(f"Sighting of {orca_id} saved!")


def show_stats(data):
    """Show pod sizes, average ages, and sighting totals."""
    current_year = date.today().year

    print("\n=== Pod Stats ===")
    for pod in ["J", "K", "L"]:
        members = [orca for orca in data["orcas"] if orca["pod"] == pod]
        if not members:
            continue
        ages = [current_year - orca["birth_year"] for orca in members]
        avg_age = sum(ages) / len(ages)
        print(f"{pod} pod: {len(members)} orcas, average age {avg_age:.1f}")

    print("\n=== Sightings ===")
    sightings = data["sightings"]
    print(f"Total sightings: {len(sightings)}")

    if sightings:
        counts = {}
        for sighting in sightings:
            orca_id = sighting["orca_id"]
            counts[orca_id] = counts.get(orca_id, 0) + 1
        top_id = max(counts, key=counts.get)
        print(f"Most sighted: {top_id} ({counts[top_id]} sightings)")
def main():
    data = load_data()

    while True:
        print("\n=== Orca Pod Tracker ===")
        print("1. List all orcas")
        print("2. Search orcas")
        print("3. Log a sighting")
        print("4. Show stats")
        print("5. Quit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            list_orcas(data)
        elif choice == "2":
            search_orcas(data)
        elif choice == "3":
            log_sighting(data)
        elif choice == "4":
            show_stats(data)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try 1-5.")

if __name__ == "__main__":
    main()