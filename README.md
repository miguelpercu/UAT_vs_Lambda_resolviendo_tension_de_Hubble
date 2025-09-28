# Unified Applicable Time (UAT) Cosmological Framework

[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![arXiv](https://img.shields.io/badge/arXiv-Cosmology-b31b1b.svg)](https://arxiv.org/)

## 🌌 Overview

The **Unified Applicable Time (UAT) Framework** represents a groundbreaking approach in cosmological modeling that successfully resolves the Hubble tension through physically motivated Loop Quantum Gravity (LQG) corrections. This framework provides a minimal extension to the standard ΛCDM model while maintaining full consistency with observational data.

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- Jupyter Notebook

### Installation

```bash
# Clone the repository
git clone https://github.com/miguelpercu/UAT_vs_Lambda_resolviendo_tension_de_Hubble.git
cd UAT_vs_Lambda_resolviendo_tension_de_Hubble

# Install dependencies
pip install numpy pandas matplotlib scipy seaborn astropy corner jupyter

# Launch Jupyter Notebook
jupyter notebook

Verify Installation
# Run dependency check
python check_uat_dependencies.py

📚 Study Repositories
1. First Study: Framework Validation
Repository: uat_explicacion_con_datos_reales
Focus: Statistical validation against H(z) data
Key Finding: UAT demonstrates equivalence with ΛCDM (χ² = 14.8)

2. Latest Study: Hubble Tension Resolution
Repository: UAT_vs_Lambda_resolviendo_tension_de_Hubble
Focus: Resolution of 4.8σ Hubble tension using BAO data
Breakthrough: H₀ = 73.0 km/s/Mpc with Δχ² = +0.006 vs ΛCDM

Core Dependencies
# Essential packages
numpy>=1.19.0      # Numerical computations
pandas>=1.3.0      # Data manipulation
matplotlib>=3.3.0  # Visualization
scipy>=1.6.0       # Scientific computing

# Enhanced functionality
seaborn>=0.11.0    # Advanced plotting
astropy>=4.3.0     # Astronomical constants
corner>=2.2.0      # Parameter space visualization

Framework Architecture
class UATModel:
    """Unified Applicable Time Framework Implementation"""
    
    def E_UAT_early(self, z, k_early):
        """UAT-modified expansion for early universe"""
        return np.sqrt(k_early * self.cosmo.Om_r * (1+z)**4 + 
                      k_early * self.cosmo.Om_m * (1+z)**3 + 
                      self.cosmo.Om_de)
    
    def calculate_rd(self, k_early=1.0, H0=67.36):
        """Calculate sound horizon with UAT corrections"""
        # Numerical integration of modified expansion history

Key Equations
Modified Expansion History
E_{\text{UAT}}(z,k_{\text{early}}) = \sqrt{k_{\text{early}}\Omega_{r0}(1+z)^4 + k_{\text{early}}\Omega_{m0}(1+z)^3 + \Omega_{\Lambda 0}}

Sound Horizon Calculation
r_d^{\text{UAT}} = \frac{c}{H_0^{\text{target}}} \int_{z_{\text{drag}}}^{\infty} \frac{dz'}{E_{\text{UAT}}(z', k_{\text{early}}) \sqrt{3(1 + R(z'))}}

Hubble Tension Resolution
Model	H₀ [km/s/Mpc]	r_d [Mpc]	χ²	Δχ² vs ΛCDM	Resolution
ΛCDM (Planck)	67.36	147.09	2.449	0.000	No
ΛCDM (SH0ES)	73.00	147.09	87.085	-84.636	No
UAT Solution	73.00	142.9	2.455	+0.006	Yes
Optimal Parameters
k_early = 1.0739 (7.39% early universe density enhancement)

r_d = 142.9 Mpc (2.85% reduction from Planck)

Transition redshift: z > 300 (smooth transition to standard evolution)

📁 Project Structure
UAT_Framework/
│
├── 📊 Analysis_Notebooks/
│   ├── UAT_cosmology_framework.ipynb      # First study: H(z) validation
│   └── UAT_BAO_tension_resolution.ipynb   # Latest study: Hubble tension
│
├── 🔧 Source_Code/
│   ├── uat_model.py                       # Core UAT implementation
│   ├── cosmological_functions.py          # Utility functions
│   └── visualization_tools.py             # Plotting utilities
│
├── 📈 Results/
│   ├── UAT_realistic_analysis/            # Generated output structure
│   │   ├── analysis/                      # Configuration & summaries
│   │   ├── data/                          # Observational datasets
│   │   ├── figures/                       # Publication-quality plots
│   │   └── tables/                        # Detailed results
│   └── validation_reports/                # Statistical validation
│
└── 📚 Documentation/
    ├── check_uat_dependencies.py          # Environment verification
    ├── theoretical_background.pdf         # Mathematical foundations
    └── replication_guide.md               # Step-by-step instructions

Example Usage
# Initialize UAT model
from uat_model import UATModel
from cosmological_parameters import CosmologicalParameters

cosmo = CosmologicalParameters()
uat = UATModel(cosmo)

# Calculate UAT predictions
rd_uat = uat.calculate_rd(k_early=1.0739, H0=73.0)
predictions = [uat.calculate_DM_rd(z, 73.0, rd_uat) for z in [0.38, 0.51, 0.61]]

Development Setup
# Create virtual environment
python -m venu uat_env
source uat_env/bin/activate  # Linux/Mac
# OR
uat_env\Scripts\activate     # Windows

# Install development dependencies
pip install -r requirements_dev.txt

# Run tests
python -m pytest tests/

📜 Citation
@article{percudani2025uat,
  title={Unified Applicable Time Framework: Resolving the Hubble Tension},
  author={Percudani, Miguel Angel},
  journal={Preprint},
  year={2025},
  url={https://github.com/miguelpercu/UAT_vs_Lambda_resolviendo_tension_de_Hubble}
}
📞 Contact & Support
Author: Miguel Angel Percudani

Email: miguel_percudani@yahoo.com.ar
