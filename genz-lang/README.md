# GenzLang Compiler


## Setup Instructions
So, the requirements for this project are:

Anaconda (way simpler to install LLVMlite through conda than pip)

LLVMlite
> $ conda install --channel=numba llvmlite

RPLY (same as PLY but with a better API)
> $ conda install -c conda-forge rply

LLC (LLVM static compiler)
GCC (or other linking tool)

### Creating and Activating a Conda Environment

> conda create -n <env-name>
> conda activate <env-name>

## Commands to Generate Output file & Run Executable
$ llc -filetype=obj output.ll

$ gcc output.o -o output

$ ./output

