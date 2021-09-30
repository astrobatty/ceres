# Description:

The original ferospipe pipeline has been developed to precisely measure the radial velocity of
stars using cross correlation technique. To do so, it traces and extracts all the 33 available
Echelle orders, but calibrates only 25 of them, excluding the first 8 orders that covers the
~6730-8230 A wavelength. As this range carries several useful spectral features, we modified
the code to expand the wavelength coverage. We identified the emission lines in the corresponding
ThAr spectra, which are used to carry out the new wavelength calibration. The pipeline fits
polynomials to the beforehand identified pixel value-wavelength pairs in each orders to
iteratively sigma clip the outliers. Then, these cleaned orders are fitted simultaneously
using Chebyshev functions to improve the precision of the wavelength solution. To fit the
pixel value-wavelength pairs in the newly added orders as well, we tested a wide range of
coefficients and picked the ones where the standard deviation of the residual was approximately
the same as if only the last 25 orders were used. Unfortunately, in the first 2 orders the
low number of features in the ThAr spectra makes the line identification unreliable,
thus it is strongly recommended to exclude the ~8230-9000 A range from further spectral
analysis.

For precise radial velocity measurements, use the original CERES pipeline!

# Installation:

Get this updated code:
```bash
git clone https://github.com/astrobatty/ceres.git --single-branch --branch feros_extended_wavelength

cd ./ceres
```

As `ceres` is written in Python 2, it is suggested to install it within a conda environment:
```bash
conda create -n ceres python=2.7 numpy scipy matplotlib astropy pycurl PyAstronomy ephem

conda activate ceres
```

Before installation the python path must be set in `ceres/utils/SSephem/Makefile`. To find out the path use:
```bash
which python
```
and copy the path without the `/bin/python` at the end, and paste it to the PY_PREFIX in the makefile:
```bash
PY_PREFIX := /path/to/your/conda/envs/ceres
```

After this the package can be install via:
```bash
python install.py
```

Finally install the stable version of `statsmodels`:
```bash
conda install -c anaconda statsmodels
```

## Common fails:
If `gcc` fails due to missing `-lgls`, check GSL path:
```bash
pkg-config --cflags --libs gsl && gsl-config --version
```

and add the printed paths to -I and -L options within the problematic setup.py file.

If there is no GSL installed, install it on Linux via
```bash
sudo apt-get install libgsl-dev
```

or on OSX via
```bash
sudo port install gsl
```

# Usage:

The first step is to remove the low S/N spectra. There is a simple python script, called `remove_faint_ThAr_files.py`.
This should be run in the data folder, where all the spectra can be found. This will _permanently_ remove
the "useless" files, thus be sure that there is a back up, because it uses rm!

After this `ferospipe` can be used as usual.
