# Changelog

## [1.1.3] - 2025-03-20
- First correctly functioning release

## [1.2.0] - 2025-03-26
### Added
- Step response
- Nyquist diagram
### Changed
- Added a dark_mode option for the plots

## [1.2.5] - 2025-03-26
### Fixed
- Corrected a typo in pyproject.toml

## [1.3.0] - 2025-04-04
### Added
- Solver class including:
  - Euler
  - Runge Kutta 2
  - Runge Kutta 4
### Changed
- Diffeq now supports exponents.
Also, PySysControl now officially has requirements
## [1.3.1] - 2025-04-06
### Fixed
- Fixed error in DiffEq.find_factors() that incorrectly turned "t" into "t**2"
## [1.4.0] - 2025-04-10
### Added
- PDiffEq. DiffEqs brother for PDEs
## How to update
Run the folowing command to update:
- pip install --upgrade pysyscontrol
