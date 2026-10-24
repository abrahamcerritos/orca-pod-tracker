import json

DATA_FILE = "orcas.json"


def load_data():
    """Read orcas.json and return it as a Python dictionary."""
    with open(DATA_FILE, "r") as file:
        return json.load(file)


def list_orcas(data):
    """Print every orca in a simple table."""
    print("\nID    Name          Pod  Sex     Born")
    print("-" * 40)
    for orca in data["orcas"]:
        print(f"{orca['id']:<6}{orca['name']:<14}{orca['pod']:<5}"
              f"{orca['sex']:<8}{orca['birth_year']}")


if __name__ == "__main__":
    data = load_data()
    list_orcas(data)