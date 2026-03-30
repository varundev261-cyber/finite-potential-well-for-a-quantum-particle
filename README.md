# Finite Square Well — Numerical Solution

Solves the 1D time-independent Schrödinger equation for a particle in a
finite square well using the **finite difference method**.

## Physics

The potential is defined as:

$$V(x) = \begin{cases} 0 & |x| \leq \frac{a}{2} \\ V_0 & |x| > \frac{a}{2} \end{cases}$$

The Hamiltonian is:

$$H = -\frac{\hbar^2}{2m}\frac{d^2}{dx^2} + V(x)$$

Discretized on a uniform grid and solved as a matrix eigenvalue problem $H\psi = E\psi$.

Unlike the infinite well, bound states only exist for $E < V_0$. States
with $E > V_0$ are unphysical scattering states — an artifact of the
finite grid with hard-wall boundary conditions.

## Results

| n | Energy |
|---|--------|
| 1 | 9.82997129  |
| 2 | 36.03408203 |
| 3 | 55.91646591 |
| 4 | 59.63581292 |


## Usage
```bash
pip install -r requirements.txt
python finite_square_well.py
```

## Parameters

| Parameter | Value | Meaning |
|-----------|-------|---------|
| N | 400 | Number of grid points |
| L | 1.0 | Half-width of spatial domain |
| V₀ | 50 | Potential outside the well |
| a | 0.5 | Well width |
| ℏ, m | 1.0 | Natural units |

## Method

- Builds the tridiagonal second-derivative matrix $D^2$
- Constructs the potential as a diagonal matrix $V$
- Builds $H = -\frac{\hbar^2}{2m} D^2 + V$
- Solves via `numpy.linalg.eigh`
- Normalizes and plots the first 4 eigenstates overlaid on the potentialthis is a program which simulate energies of a quantum particle in a finite potential box where we can observe the quantum tunnelling where energies get diluted 
