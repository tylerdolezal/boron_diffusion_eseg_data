import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
import seaborn as sns

# Styling
plt.rcParams.update({'figure.figsize': [4, 5], 'axes.grid': True, 'font.family': 'Graphik'})

def plot_ridge(csv_path, target_col, solute, label):
    df = pd.read_csv(csv_path)
    sns.set_style("ticks")
    fig, ax = plt.subplots()
    
    unique_n = sorted(df["n_solute"].unique())
    colors = sns.color_palette("tab10", len(unique_n))
    offset = 1.2

    for i, n in enumerate(unique_n):
        subset = df[df["n_solute"] == n][target_col].dropna()
        if len(subset) < 2: continue

        # Dynamic Bandwidth Logic from your original scripts
        bw = 0.05 if "E_seg" in target_col else 0.01
        if solute == "cr" and n in [0, 1, 2] and "dE" in target_col:
            bw = 0.0025

        kde = gaussian_kde(subset, bw_method=bw)
        x_vals = np.linspace(df[target_col].min()-0.2, df[target_col].max()+0.2, 500)
        y_vals = kde(x_vals)
        y_scaled = y_vals / y_vals.max() * 0.85
        
        ax.fill_between(x_vals, i * offset, i * offset + y_scaled, color=colors[i])
        ax.plot(x_vals, i * offset + y_scaled, color='k', linewidth=1.0)

    ax.set_xlabel(label)
    ax.set_ylabel(f"{solute.capitalize()} Coordination")
    ax.set_yticks([i * offset for i in range(len(unique_n))])
    ax.set_yticklabels(unique_n)
    sns.despine(left=True)
    
    plt.savefig(f"plots/ridge_{solute}_{target_col.split(' ')[0]}.pdf", bbox_inches="tight")
    plt.close()

if __name__ == "__main__":
    for solute in ["cr", "mo"]:
        path = f"data/spectral_data_{solute}_S5.csv"
        plot_ridge(path, "E_seg (eV)", solute, "Segregation Energy (eV)")
        plot_ridge(path, "dE_forward (eV)", solute, "Forward Barrier (eV)")
        plot_ridge(path, "dE_reverse (eV)", solute, "Reverse Barrier (eV)")