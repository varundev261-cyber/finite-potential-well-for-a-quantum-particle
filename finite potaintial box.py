import numpy as np
import matplotlib.pyplot as plt 

#parameaters 
N=400
L=1.0
hbar=1.0
m=1.0
#spartiL grid where we create the horizontal part of the well
x=np.linspace(-L,L,N)
dx=x[1]-x[0]
xp=x[1:-1]
N=len(x)
#seconf derivative matrix 
D2=np.zeros((N,N))
for i in range(N):
    D2[i,i]=-2
    if i>0:
        D2[i,i-1]=1
    if i<N-1:
        D2[i,i+1]=1
D2=D2/dx**2
#finite square well potential
v0 = 50
well_width = 0.5

v = np.zeros(N)

for i in range(N):
    if abs(x[i]) > well_width/2:
        v[i] = v0
#lets convert potential into matrix
v_matrix=np.diag(v)  #diagonal matrix
#build hamiltonian 
H=-(hbar**2)/(2*m)*D2+v_matrix
# now lets solve for the eigen value problem where we equate hamaltonian eqaution
energies,states=np.linalg.eigh(H)
# lets plot first 4 sttates
for n in range(4):
    psi=states[:,n]
    psi=psi/np.sqrt(np.sum(psi**2)*dx)
    plt.plot(x,psi+energies[n])
plt.plot(x,v,'k',linewidth=2)
plt.xlabel("x")
plt.ylabel("energy/wavefunction")
plt.show()
print("first 6 energies")
print(energies[:6])
