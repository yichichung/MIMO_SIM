# main.py
from simulation import run_simulation
from plot import plot_ber

if __name__ == "__main__":
    snrs, bers = run_simulation()
    plot_ber(snrs, bers)
