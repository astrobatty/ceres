# Remove ThAr files which have lower exptime than 300 sec

from astropy.io import fits
import os
import glob

files = glob.glob('FEROS*.fits')
for i in range(len(files)):
    hdul = fits.open(files[i])
    if hdul[0].header['OBJECT'] == 'WAVE' and hdul[0].header['EXPTIME']<250.:
        print('Deleting... '+files[i])
        os.remove(files[i])
