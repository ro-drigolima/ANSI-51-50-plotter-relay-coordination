# Relay Coordination: Plotting ANSI 51/50, 51N/50N Curves with Python and Matplotlib

This project is a tool to plot inverse-time overcurrent protection curves (ANSI 51 and 50) for both phase and neutral relays using Python and Matplotlib. The tool helps in visualizing and analyzing relay settings and coordination in power systems.

## Features

- Plot ANSI 51 (Inverse Time Overcurrent) and 50 (Instantaneous Overcurrent) curves.
- Supports multiple curve types (Normal Inverse, Very Inverse, and Extremely Inverse).
- Visualize phase and neutral protection curves.
- Automatic identification and marking of crossover points between ANSI 51 and 50 curves.
- Log-log scale for both axes, with grid and labeled ticks for easy reading.

## Getting Started

### Prerequisites

- Python 3.6+
- Matplotlib
- NumPy

### Installation

1. Clone this repository:
    ```sh
    git clone https://github.com/ro-drigolima/relay-coordination-plotter.git
    cd relay-coordination-plotter
    ```

2. Install the required Python packages:
    ```sh
    pip install matplotlib numpy
    ```

### Usage

1. Run the `main.py` script:
    ```sh
    python main.py
    ```

2. Modify the `main` function in `main.py` to customize the relay settings and curves as needed.

### Functions

- `curve_51(dial, curve, Is, N)`: Generates the time-current curve for ANSI 51 based on the dial setting, curve type, and current settings.
- `curve_50(Imax, N)`: Generates the time-current curve for ANSI 50 based on the maximum current.
- `cross_51_50(curve_51, curve_50)`: Identifies the crossover points between ANSI 51 and 50 curves.
- `plot_config(...)`: Configures and plots the curves on a log-log scale.

### Example

Here’s an example of how to generate and plot the ANSI 51 and 50 curves:

```python
import matplotlib.pyplot as plt
import numpy as np

def main():
    relay_51F = curve_51(dial=0.1, curve="VI", Is=200, N=1000)
    relay_50F = curve_50(Imax=3000, N=1000)
    relay_51N = curve_51(dial=0.15, curve="VI", Is=200, N=800)
    relay_50N = curve_50(Imax=2000, N=1000)

    plot_config(
        curve_51F=relay_51F, label_51F="51F",
        curve_50F=relay_50F, label_50F="50F",
        curve_51N=relay_51N, label_51N="51N",
        curve_50N=relay_50N, label_50N="50N",
    )

# Additional functions: curve_51, curve_50, cross_51_50, plot_config as defined above

if __name__ == "__main__":
    main()
