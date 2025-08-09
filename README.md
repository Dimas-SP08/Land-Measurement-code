# Land Measurement Automation  
*by Dimas S.P*  
(Vocational High School Student – Modeling Design & Building Information)

---

## Introduction

Automated land measurement tool combining Python programming with vocational surveying knowledge.  
Created to simplify elevation calculation and land surveying tasks.

---

## Features

- Mid-thread validation (top, mid, bottom input)
- Automatic elevation & height difference calculation
- Distance input between points
- Auto status labeling: RISE, FALL, FLAT
- Clean tabular results and interactive graphic display
- Export results to:
  - Excel (.xlsx) with embedded graphs
  - CSV file
  - PNG plots: elevation profile, bar chart, scatter plot

---

## Versions

| Version | Highlights                                                        | Docs                                   | Script Path                                   |
| ------- | ----------------------------------------------------------------- | -------------------------------------- | ---------------------------------------------- |
| **v1.0**  | Basic elevation & status (RISE/FALL) + Excel export               | [v1/README.md](./v1/README.md)         | [`v1/Land_Measurement_v1.py`](./v1/Land_Measurement_v1.py) |
| **v2.0**  | Added elevation graphs (profile, bar chart, scatter plot) & code efficiency | [v2/README.md](./v2/README.md)         | [`v2/Land_Measurement_v2.py`](./v2/Land_Measurement_v2.py) |
| **v3.0**  | Refactored to OOP modules, CLI & tools directory structure | [v3/README.md](./v3/README.md)         | [`v3/main.py`](./v3/main.py) |
| **v4.0**  | GUI version with PyQt5, multi-page interface, export to `.exe` | [v4/README.md](./v4/README.md)         | [`v4/main.py`](./v4/main.py) |

---

## How It Works (GUI v4.0 Preview)

- Input number of measurement points & initial AMSL elevation
- Enter backsight/foresight readings + distance between points
- Real time calculation and visual graph display
- Export results to Excel, CSV, and PNG

[See the complete explanation and screenshot at](./v4/README.md#how-it-works)

---

## Download App and Security App (GUI v4.0)

[See the explanation and link at](./v4/README.md#Download-App)



