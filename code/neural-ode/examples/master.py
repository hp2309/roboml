import subprocess
import numpy as np

# subprocess.call(" python slave.py --a=True --n=10 --s='sad'", shell=True)

if __name__ == '__main__':
    i = 500
    while i <= 5000:
        subprocess.call(" python latent_ode.py --nspiral=" + str(i), shell=True)
        i += 500
    print("Done for adjoint False")
    i = 500
    while i <= 5000:
        subprocess.call(" python latent_ode.py --adjoint=True --nspiral=" + str(i), shell=True)
        i += 500
    print("Done for adjoint True")
