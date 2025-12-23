# Data and Kinetics Analysis Repository (Acta Materialia)
This repository contains the consolidated datasets and plotting scripts required to reproduce the energy barrier and segregation energy distributions for the manuscript. 

> **Spectral Sampling of Boron Diffusion in Ni Alloys: Cr and Mo Effects on Bulk and Grain Boundary Transport**  
> Tyler D. Doležal, Rodrigo Freitas, Ju Li

## 📂 Repository Structure

* **`data/`**: Consolidated `.csv` files containing $E_{seg}$ and migration barrier statistics.
* **`plots/`**: Output directory for publication-quality ridge plots (PDF format).
* **`scripts/`**: Python scripts for generating figures from the provided datasets.
* **`generate_spectra/`**: **[NOTE]** The original sampling scripts used to generate the raw `spectral_log.csv` files from atomistic configurations are provided in this standalone directory, kept separate from the main plotting repository.

---

## 📊 Dataset Descriptions (`data/`)

The data in this directory has been processed to correlate local atomic coordination with thermodynamic and kinetic properties.

| File Name | Description | Related Figures |
| :--- | :--- | :--- |
| `spectral_data_cr_s5.csv` | Segregation energies and Cr-migration barriers ($dE_{fwd}$, $dE_{rev}$) for the $\Sigma 5$ GB. | Fig. 6, 8 |
| `spectral_data_mo_s5.csv` | Segregation energies and Mo-migration barriers ($dE_{fwd}$, $dE_{rev}$) for the $\Sigma 5$ GB. | Fig. 6, 8 |

---

## 🐍 Plotting Scripts (`scripts`)

The following scripts allow for the immediate reproduction of the ridge plots used in the manuscript:

* **`plot_acta_ridges.py`**: This is the master plotting script. It reads the consolidated CSV files and generates:
    1. **Segregation Energy Ridge Plots**: Distributions of $E_{seg}$ relative to local solute coordination ($n$).
    2. **Kinetic Barrier Ridge Plots**: Distributions of forward and reverse migration barriers across different local environments.

### Key Features:
* **Dynamic Bandwidth**: Uses specialized KDE bandwidths ($bw$) to capture sharp peaks in low-coordination environments while maintaining smooth distributions for high-coordination sites.
* **$n=0$ Baseline**: Includes a combined Ni-Cr and Ni-Mo baseline for the zero-solute coordination limit to ensure a consistent reference across all alloy systems.

---

## 📝 Citation

If you use this data or these scripts in your research, please cite the following paper:

> **[Author Names]**, "[Full Title of the Acta Materialia Paper]," *Acta Materialia*, **[Year]**, [Volume], [Page Numbers/DOI].
