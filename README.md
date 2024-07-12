# dcs-talaria
A python interface to the REST API exposed by the DCS Olympus mod

## Quick Start

So far, only `spawnGroundUnits` is implemented, but the `main.py` script will spawn in a car on the ramp at Batumi (with hard-coded coordinates).

To try it out, make sure you have a python 3 executable, install [DCS Olympus](https://github.com/Pax1601/DCSOlympus), and start a DCS mission where you can observe Batumi.

Then from this directory run:

```
export DCS_OLYMPUS_PORT=3001
export DCS_OLYMPUS_USERNAME=your_username
export DCS_OLYMPUS_PASSWORD=your_password
python src/main.py
```
