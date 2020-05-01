## Installation of OpenFOAM and rheoTool on windows10

Getting rheoTool compiled and working was a long and frustrating journey. 
I’m writing this document to help make this process a bit smoother. 
I used ubuntu 18.04 as a windows subsystem for linux, which can be downloaded from the [microsoft store](https://docs.microsoft.com/en-us/windows/wsl/install-win10). 
I’ll divide this document in 2 sections: the ﬁrst section will describe the way that I managed to get rheoTool working and the second section will describe everything that didn’t work.
On a side note, if you are not interested in the rheoTool extension and just want to work with OpenFOAM. 
Downloading the .tgz ﬁle from www.openfoam.com as described in the beginning of section 2 is the quickest way I found to install OpenFOAM.

### Getting rheoTool to work
There are three main variations of OpenFOAM. 
[OpenFOAM](https://www.openfoam.org) which is maintained by the OpenFOAM Foundation, [OpenFOAM+](https://www.openfoam.com) which is maintained by ESI-OpenCFD and foam-extend which is maintained by Wikki Ltd. 
after having failed to compile rheoTool with versions of the OpenFOAM+ and OpenFOAM variations, as described in section 2, I decided to give the foam-extend variation a shot. 

To download the source ﬁles of foam-extend and compile it follow [these](https://openfoamwiki.net/index.php/Installation/Linux/foam-extend-4.0) instructions. 
The compilation of foam-extend in step 4 of the guide froze in my terminal. 
I managed to ﬁx this using the steps in post 27-30 of [this](https://www.cfd-online.com/Forums/openfoam-installation/216670-problems-compilingfoam-extend-4-0-fsifoam-ubuntu-wsl-2.html) forum thread. 
After having installed foam-extend succesfully follow the [user guide](https://github.com/fppimenta/rheoTool/tree/master/doc) of [rheoTool](https://github.com/fppimenta/rheoTool). 

### Things that didn’t work
I ﬁrst followed [these](https://www.openfoam.com/download/install-windows-10.php) instructions. 
This was the quickest way of installing OpenFOAM. 
OpenFOAM itself worked ﬁne but when trying to get rheoTool running I ran into issues. 
In step 2.4.3 of the rheoTool [user guide](https://github.com/fppimenta/rheoTool/tree/master/doc), during the conﬁguration of the PETSc library, I kept running into errors that I couldn’t ﬁx. 

Next I tried to install the same version but then from its source code to see if this would ﬁx the problem. 
I followed [these](https://openfoamwiki.net/index.php/Installation/Linux/OpenFOAM-v1806/Ubuntu) steps, each time replacing v1806 by v1912. 
This actually got me past the conﬁguration of the PETSc library. 
When i tried to compile rheoTool in step 2.4.4 of the guide I ran into a similar error as shown in the paragraph bellow. 

Next I tried to install OpenFOAM v6 since this is the featured version in the rheoTool user guide. 
To install this openfoam version I followed [these](https://openfoamwiki.net/index.php/Installation/Linux/OpenFOAM-6/Ubuntu) steps. 
Trying to compile rheoTool I ran into the same error as with OpenFOAM v1912. 
the error on the bash terminal was: 

```
/home/erik/OpenFOAM/OpenFOAM6/src/OpenFOAM/lnInclude/List.C:211:39: error: no matching function for call to ‘distance(int, int)’ 
List< T >(ﬁrst, last, std::distance(ﬁrst, last))
/usr/include/c++/7/bits/stliteratorbasefuncs.h:138:5: error: no type named ‘diﬀerencetype’ in ‘struct std::iteratortraits¡int¿’ 
/home/erik/OpenFOAM/OpenFOAM6/wmake/rules/General/transform:25: recipe for target ’Make/linux64GccDPInt64Opt/operators/blockOperators.o’ failed make:
*** [Make/linux64GccDPInt64Opt/operators/blockOperators.o] Error 1
```
