# EvolutionExperiment
A Python-based simulation of population genetics, modeling evolution through natural selection, reproduction, and mutation. This project visualizes how generations adapt to environmental constraints, tracking fitness scores, survival rates, and genetic diversity.

## Overview

This project simulates a genetic algorithm that models population evolution over multiple generations. The simulation includes key biological concepts such as reproduction, natural selection, and mutation (via radiation exposure). The system tracks fitness scores across generations and provides visualizations of evolutionary trends.

## Key Features

- *Population Generation*: Creates an initial population with randomized genetic traits
- *Fitness Evaluation*: Scores individuals based on their genetic makeup
- *Natural Selection*: Filters individuals based on environmental constraints
- *Reproduction*: Combines genes from top-performing individuals to create offspring
- *Mutation*: Simulates radiation-induced genetic mutations
- *Generational Analysis*: Tracks population statistics across generations
- *Data Visualization*: Provides graphical representations of evolutionary trends

## Installation

1. Clone this repository
2. Ensure you have Python 3.8+ installed
3. Install dependencies:
   bash
   pip install -r requirements.txt
   

## Configuration

Modify config.py to adjust simulation parameters:

- population_count: Initial number of individuals (default: 1000)
- generation_number: Total generations to simulate (default: 100)
- individual_gene_length: Length of genetic sequences (default: 5)
- reproduction_rate: Percentage of population that reproduces (default: 0.8)
- exposure_level: Radiation exposure intensity (default: 5)

## Usage

Run the simulation:
bash
python main.py


The program will:
1. Generate an initial population
2. Simulate life cycles with natural selection
3. Apply radiation-induced mutations
4. Track population statistics across generations
5. Display visualizations of evolutionary trends

## Output

The simulation produces two main visualizations:

1. *Fitness Score by Generation*:
   - Average, maximum, and minimum fitness scores
   - Score range visualization

2. *Population Count by Generation*:
   - Bar chart showing surviving individuals per generation

Additionally, the console displays:
- Population counts at key simulation stages
- Final evolutionary trend analysis

## Customization

To modify the simulation:
- Adjust environmental constraints in config.py (environment dictionary)
- Change nucleotide values and their impact on traits
- Modify selection criteria in life_simulation.py
- Alter reproduction logic in generate_population.py

## Dependencies

- Python 3.8+
- numpy (2.3.2)
- matplotlib (3.10.3)

## License

This project is open-source and available under the MIT License.
