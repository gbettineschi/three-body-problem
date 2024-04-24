# What is this?
This is a didactical project coded while studying Physics I with professor Luca Saglietti. It simulates and plots the trajectories on the plane of any number of bodies, each influenced by the others' gravitational force. 

The system parameters (gravitational constant, time steps, etc) can be easily customized. The code can actually run simulation and computations even in 3 dimensions, the plotting only works in 2 dimensions.

### About the physics and math behind
To work, the script clearly needs to compute forces and accelrations at each instant, i.e. it needs to solve ordinary differential equations. It solves them using numerical method; at the moment:
- the Euler method is implemented and used;
- there is an incomplete function where the more accurate Runge-Kutta methods are supposed to be implemented.

### Technologies
Lagnauge: Python.
Libraries used: numpy, matplotib.
