import subprocess
import time

# subprocess.call(" python slave.py --a=True --n=10 --s='sad'", shell=True)

if __name__ == '__main__':
    
    i = 10
    while i <= 200:
        f = open("log.txt", "a")
        s = time.time()
        subprocess.call(" python latent_ode.py --nsample=" + str(i), shell=True)
        e = time.time()
        f.write("latent_ode adjoint=false runtime={} nsample={}\n".format(e-s, i))
        f.close()
        i += 10
    print("Done for adjoint False")
    i = 10
    while i <= 200:
        f = open("log.txt", "a")
        s = time.time()
        subprocess.call(" python latent_ode.py --adjoint=True --nsample=" + str(i), shell=True)
        e = time.time()
        f.write("latent_ode adjoint=true runtime={} nsample={}\n".format(e-s, i))
        f.close()
        i += 10
    print("Done for adjoint True")
