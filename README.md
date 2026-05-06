# Ecology Behaviour Toolkit

A minimal, clean toolkit for analysing behavioural ecology datasets.

This project provides:
- Simple functions to load behavioural data
- Tools to compute activity budgets
- Basic visualisation utilities for behaviour over time

## Folder Structure

```
ecology-behaviour-toolkit/
│
├── data/               # Place your CSV datasets here
├── notebooks/          # Jupyter notebooks for analysis
├── src/                # Source code
│   ├── behaviour.py     # Behaviour analysis functions
│   └── visualization.py # Plotting utilities
│
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

## Getting Started

Install dependencies:

```
pip install -r requirements.txt
```

Example usage:

```python
from src.behaviour import load_behaviour_data, compute_activity_budget
from src.visualization import plot_activity_budget

df = load_behaviour_data("data/your_dataset.csv")
activity = compute_activity_budget(df, "behaviour")
plot_activity_budget(activity)
```

## Purpose

This toolkit is designed for:
- Students beginning behavioural ecology analysis
- Quick exploratory data analysis
- Lightweight, readable code for teaching or small projects

## Future Extensions

- More behaviour metrics
- Ethogram visualisation
- Individual‑level summaries

## Data from:  
Rauber, Ramona; Clutton-Brock, Tim H.; Manser, Marta B. (2019). Data from: Drought decreases cooperative sentinel behaviour and affects vocal coordination in meerkats [Dataset]. Dryad. https://doi.org/10.5061/dryad.1s73fc5
