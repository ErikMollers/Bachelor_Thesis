# Programming logbook

### 07/05/2020
The goal of today will be to create a good mesh for our problem. 
I found an interesting forum [discussion](https://www.cfd-online.com/Forums/openfoam-meshing/88973-simple-sphere-snappyhexmesh.html) about meshing spheres in openFoam.
Post #7 seems promising to me, he shares 2 different snappyHexMesh files (a meshing utility in openFoam to alter simple blockmeshes) and a blockmesh file.
I will first just coppy these files in the case, run them by first using the blockMesh command and then the snappyHexMesh command.
Then I will look at the meshes created in paraView and adjust from there.
