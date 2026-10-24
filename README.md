# 🐋 Orca Pod Tracker

A command-line Python app for tracking the Southern Resident orcas of the Pacific Northwest — the J, K, and L pods. Look up individual whales, log sightings, and view stats about each pod.

## Features

- **List all orcas** in a formatted table
- **Search** by ID or name (case-insensitive)
- **Log sightings** with date and location, saved to JSON
- **View stats**: pod sizes, average age per pod, total sightings, and the most-sighted orca
- **Input validation** for orca IDs, dates, and empty fields

## How to Run

Requires Python 3.

```bash
git clone https://github.com/abrahamcerritos/orca-pod-tracker.git
cd orca-pod-tracker
python3 orca_tracker.py
```

## Example

```
=== Orca Pod Tracker ===
1. List all orcas
2. Search orcas
3. Log a sighting
4. Show stats
5. Quit
Choose an option: 1

ID    Name          Pod  Sex     Born
----------------------------------------
J35   Tahlequah     J    female  1998
J26   Mike          J    male    1991
K20   Spock         K    female  1986
L25   Ocean Sun     L    female  1928
```

## Project Structure

| File | Purpose |
|------|---------|
| `orca_tracker.py` | Main program: menu, search, sighting logging, stats |
| `orcas.json` | Orca records and saved sightings |
| `README.md` | Project overview |

## What I Practiced

- Reading and writing JSON files
- Working with lists, dictionaries, and list comprehensions
- Validating user input and handling errors with `try`/`except`
- Organizing code into small, single-purpose functions

## Data Note

Orca IDs and names follow the Southern Resident catalog maintained by the [Center for Whale Research](https://www.whaleresearch.com/). L25's birth year is an estimate. This dataset is a small sample, not the full population.

## Future Ideas

- Add the full Southern Resident population
- Filter sightings by date range or location
- Export stats to a CSV file