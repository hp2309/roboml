import subprocess
import numpy as np

# subprocess.call(" python slave.py --a=True --n=10 --s='sad'", shell=True)

if __name__ == '__main__':
    i = 100
    while i <= 1000:
        subprocess.call(" python latent_ode.py --nsample=" + str(i), shell=True)
        i += 100
    print("Done for adjoint False")
    i = 100
    while i <= 1000:
        subprocess.call(" python latent_ode.py --adjoint=True --nsample=" + str(i), shell=True)
        i += 100
    print("Done for adjoint True")
