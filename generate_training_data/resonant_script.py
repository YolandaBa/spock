import rebound
import numpy as np
import pandas as pd
datafolder = '/home/yba/spock/data/'

def run(filename):
    try:
        # find the corresponding file
        sa = rebound.SimulationArchive(datafolder+"resonant/simulation_archives/runs/sa"+filename)# read the file
        sim = sa[0] # read the initial condition
        m0 = sim.particles[0].m
        m1 = sim.particles[1].m
        m2 = sim.particles[2].m
        m3 = sim.particles[3].m

        vx0 = sim.particles[0].vx
        vx1 = sim.particles[1].vx
        vx2 = sim.particles[2].vx
        vx3 = sim.particles[3].vx

        vy0 = sim.particles[0].vy
        vy1 = sim.particles[1].vy
        vy2 = sim.particles[2].vy
        vy3 = sim.particles[3].vy

        vz0 = sim.particles[0].vz
        vz1 = sim.particles[1].vz
        vz2 = sim.particles[2].vz
        vz3 = sim.particles[3].vz

        x0 = sim.particles[0].x
        x1 = sim.particles[1].x
        x2 = sim.particles[2].x
        x3 = sim.particles[3].x

        y0 = sim.particles[0].y
        y1 = sim.particles[1].y
        y2 = sim.particles[2].y
        y3 = sim.particles[3].y

        z0 = sim.particles[0].z
        z1 = sim.particles[1].z
        z2 = sim.particles[2].z
        z3 = sim.particles[3].z

        data = [m0, x0, y0, z0, vx0, vy0, vz0, m1, x1, y1, z1, vx1, vy1, vz1, m2, x2, y2, z2, vx2, vy2, vz2, m3, x3, y3, z3, vx3, vy3, vz3]  # Create an example row of data
        del sa
        return data
    except:
        with open('/home/yba/spock/generate_training_data/errors.csv', 'w') as e:
            e.write("{0}\n".format(filename))
            print("Error in " + fileName)

try:
    data = np.loadtxt('data_resonant.csv', delimiter=',',dtype=np.float64)
    start = data.shape[0]+1
    print(start)
    data = list(data)
except:
    data = []
    start = 0

df = pd.read_csv('/home/yba/spock/training_data/resonant/runstrings.csv', index_col=0)
for r in df.iloc[start:start+3000]['runstring']:
    ret = run(r)
    if ret:
        data.append(ret)

with open('data_resonant.csv', 'w') as f:
    np.savetxt(f, data, delimiter=',',fmt='%0.16f')        
