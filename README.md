# Tools for analysis of time-dependent data

## Installation
Install the tools by running
```bash
pip install git+https://github.com/Schoyen/tdqd-tools.git -U
```

## Data format
The program assumes that data is stored in a two-column tabular format, where the first column is the time points and the second column the measured data. For example, given a an array of time points called `time_points` and an array of the dipole moment along a specified axis called `dipole_moment` we can create the data using `numpy` by
```python
import numpy as np

# Sample data
# ...

data = np.c_[time_points[:, np.newaxis], dipole_moment[:, np.newaxis]]
np.savetxt("dipole_data.dat", data) # For raw-text files
np.save("dipole_data", data) # For pickled-data
```
Note that the command-line tools accept both NumPy-pickled files and raw-text files.

## Performing spectral analysis of dipole moment
To extract the spectral lines from the time-dependent dipole moment stored in the data set above, we can use the command-line tool `get_spec`.
```bash
get_spec dipole_data.dat
```
This generates a plot of the spectral lines using Fourier transformation. This is often too wide, so in order to limit the x-axis pass in the optional argument `--xlim <x_start> <x_end>` to limit the plot. For example,
```bash
get_spec dipole_data.dat --xlim 0 6
```
If the initial data points need to be filtered out from the Fourier transformation, pass in the optional argument `--time-stop-laser <time>`. An example is shown below to only include points `time_points >= 5`.
```bash
get_spec dipole_data.dat --xlim 0 6 --time-stop-laser 5
```
Storing the spectral data (frequency in the first column and intensity in the second) can be done with the optional argument `--out <filename>`. If the extension of `<filename>` is `.npy` the data is stored as a NumPy pickled array.
