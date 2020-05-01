# Project outline

The goal of this bachelor thesis will be to simulate the forces on an small charged sphere in an electrolyte solution near a charged electrode. 
This simulation will be performed using the openFOAM toolbox. 
First I will simulate the static case, if this can be done quick and time permits it I’ll move on to the dynamic case. 

It will be important to understand the openFOAM toolbox and get used to the diﬀerent capabilities it has.
Rheo-tool, another open source toolbox based on openFOAM, has a promising solver for our case.
It will be important for me to understand this solver so I can work with it.
Besides understanding the software I also need to get a better grasp of the physical models needed to describe the simulation.
The Poisson-Nernst-Planck model coupled to the Navier-Stokes equations will be best suited to describe this simulation. 
The Debye-H&#252;ckel and Poisson-Boltzmann models can also be implemented, Since they are a bit easier to understand it might be useful to ﬁrst run a simulation based on these models. 
