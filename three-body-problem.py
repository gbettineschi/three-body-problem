import numpy as np
import matplotlib.pyplot as plt

def norm(r):
    return np.sqrt(np.sum(r**2))

def initial_conditions(num_of_planets):
    positions = np.zeros((num_of_planets, DIMENSIONS))
    velocities = np.zeros((num_of_planets, DIMENSIONS))
    angle = 2 * np.pi / num_of_planets

    for i in range(num_of_planets):
        # distribute positions uniformly on the unit circle on the plane x,y
        positions[i, 0] = np.cos(angle * i)
        positions[i, 1] = np.sin(angle * i)

        # set unitary velocity tangent to the circle on the plane x,y
        # note: /masses[i] cancels out the momentum of the system to make the center of mass stationary; see Physics notes
        velocities[i, 0] = 1.0 * -np.sin(angle * i) / masses[i] 
        velocities[i, 1] = 1.0 * np.cos(angle * i) / masses[i]
        

    return positions, velocities
    



def compute_accelerations(masses, num_of_planets, positions): # rs is plural of r, i.e. a matrix in which each row it's an r (a position vector of a planet); ms for MASSES
    accelerations = np.zeros(positions.shape) # as for accelerations

    for i in range(num_of_planets):
        for j in range(num_of_planets):
            if i == j: continue # go to the next iteration of the loop
            dist_i_j = positions[j] - positions[i]
            accelerations[i] += G * masses[j] * (dist_i_j) / norm(dist_i_j)**3 # calculating acceleration from the gravitational force
    return accelerations



def integration_step_Euler(velocities, accelerations): # see Physics equation
    d_positions = velocities * D_T
    d_velocities = accelerations * D_T
    
    return d_positions, d_velocities

def integration_step_RK4(masses, num_of_planets, velocities, accelerations): # NOT COMPLETE
    k1v = compute_accelerations(masses, num_of_planets, positions)
    k1p = velocities

    k2v = compute_accelerations(masses, num_of_planets)
    pass



def compute_trajectories(masses, num_of_planets, positions, velocities): # how many planets, how many steps, etc.

    positions_traj = np.zeros((T, num_of_planets, DIMENSIONS)) #trajectories, i.e. positions at each instant across T; to be returned

    for t in range(T): # for each instant
        # compute position and velocity at this instant
        accelerations = compute_accelerations(masses, num_of_planets, positions)
        d_positions, d_velocities = integration_step_Euler(velocities, accelerations)

        # update positions and velocities
        positions += d_positions
        velocities += d_velocities

        # store positions in positions_traj
        positions_traj[t, :, :] = positions

        # plot, show info
        if t % PLOT_ITER == 0:
            plt.pause(0.005)
            plt.clf() # clear the figure
            plt.gca().set_aspect('equal', adjustable='box')
            
            # plot: each planet with a small colored circle, the whole trajectory with a continuous line for each planet
            for i in range(num_of_planets):
                plt.plot(positions_traj[0:t+1, i, 0], positions_traj[0:t+1, i, 1], c = cmap[i])
                plt.plot(positions_traj[t, i, 0], positions_traj[t, i, 1], 'o', c = cmap[i])
        
    plt.show()
            
            

    return positions_traj
    

G = 1
T = 1000000
D_T = 0.0005
DIMENSIONS = 2
PLOT_ITER = 100

cmap = {0: 'r', 1: 'b', 2: 'g'}

masses = np.array([1,1,2])
num_of_planets = len(masses)
positions, velocities = initial_conditions(num_of_planets)

compute_trajectories(masses, num_of_planets, positions, velocities)