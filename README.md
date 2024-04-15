
# Met Office Technical Exercise - Binding Energy
This project can be used to calculate the total binding energy of a system of particles using the Lennard-Jones potential.

$u(r) = 4\epsilon\left((\frac{\sigma}{r})^{12} - (\frac{\sigma}{r})^{6} \right)$
  

## Getting Started

1. Create a virtual environment
	```bash
	python -mvenv venv
	```
2. Activate virtual environment
	```bash
	source venv/bin/activate
	```
3. Install dependencies
	```bash
	python3 -mpip install -r requirements.txt
	```
4. Create an input text file in the format:
	```
	x1,y1,z6
	x2,y2,z6
	x3,y3,z6
	x4,y4,z6
	x5,y5,z6
	...
	```
5. Calculate total binding energy
	```bash
	python3 binding_energy/cloud.py <path_to_input_file> -p <particle_size> -d <dispersion_energy> 
	```
