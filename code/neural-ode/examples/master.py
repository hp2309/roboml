import subprocess
import numpy as np

# subprocess.call(" python slave.py --a=True --n=10 --s='sad'", shell=True)

if __name__ == '__main__':
    i = 500
    while i <= 5000:
        subprocess.call(" python latent_ode.py --adjoint=True --niters=" + str(i), shell=True)
        i += 500
    print("Done")