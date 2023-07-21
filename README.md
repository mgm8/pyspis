# PySPIS

<a href="https://pypi.org/project/pyspis/">
    <img src="https://img.shields.io/pypi/v/pyspis?style=for-the-badge">
</a>
<a href="https://pypi.org/project/pyspis/">
    <img src="https://img.shields.io/pypi/pyversions/pyspis?style=for-the-badge">
</a>
<a href="https://github.com/mgm8/pyspis/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/mgm8/pyspis?style=for-the-badge">
</a>
<a href="https://github.com/mgm8/pyspis/actions">
    <img src="https://img.shields.io/github/actions/workflow/status/mgm8/pyspis/test.yml?style=for-the-badge">
</a>

## Overview

Python library of the Satellite Power Input Simulator (SPIS).

## Dependencies

* [numpy](https://pypi.org/project/numpy/) - v1.24.1
* [matplotlib](https://pypi.org/project/matplotlib/) - v3.6.3

## Installing

This library is available in the PyPI repository, and can be installed with the following command:

* ```pip install pyspis```

Or, directly from the source files:

* ```python setup.py install```

## Documentation

The documentation page is available [here](https://mgm8.github.io/pyspis/). Instructions to build the documentation page are described below.

Contributing instructions are also available [here](https://github.com/mgm8/pyspis/blob/main/CONTRIBUTING.md).

### Dependencies

* [Sphinx](https://pypi.org/project/Sphinx/) - v6.1.3
* [sphinx-rtd-theme](https://pypi.org/project/sphinx-rtd-theme/) - v1.1.1

### Building the Documentation

The documentation pages can be built with Sphinx by running the following command inside the ``docs`` folder:

* ```make html```

## Usage Example

```python
from pyspis import SPIS
import matplotlib.pyplot as plt

plt.rcParams['text.usetex'] = True

x = SPIS(1367, 0.295, 0.01005)

time, power, power_total = x.compute_orbit(10)

print("Average power:", x.get_average_power(), "W")
print("Peak power:", x.get_peak_power(), "W")
print("Average power (sunlight):", x.get_average_power_sunlight(), "W")

fig, ax = plt.subplots()
ax.plot(time, power[:, 0], time, power[:, 1], time, power[:, 2], time, power[:, 3], time, power[:, 4], time, power[:, 5], time, power_total)
ax.legend([r'$X_{+}$', r'$X_{-}$', r'$Y_{+}$', r'$Y_{-}$', r'$Z_{+}$', r'$Z_{-}$', 'Total'])
ax.set_xlabel("Time [s]")
ax.set_ylabel("Power [W]")
plt.savefig('test.jpg', bbox_inches='tight', dpi=600, transparent=True)
plt.show()
```

## License

This project is licensed under LGPLv3 license.
