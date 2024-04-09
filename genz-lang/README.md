# GenzLang Compiler

# To activate Virtual enviornment

$ Scripts/activate

$ flask --app server run

## Setup Instructions


So, the requirements for this project are:

- [Anaconda](https://www.anaconda.com/download) (way simpler to install LLVMlite through conda than pip)

- LLVMlite

> $ conda install --channel=numba llvmlite

- RPLY (same as PLY but with a better API)

> $ conda install -c conda-forge rply

- LLC (LLVM static compiler)

- GCC (or other linking tool)

### Creating and Activating a Conda Environment

> conda create -n <env-name>

> conda activate <env-name>

### Ply Lex Yacc

<https://www.dabeaz.com/ply/ply.html>

### Rply docs

Link  to docs: <https://rply.readthedocs.io/_/downloads/en/latest/pdf/>

### LLVM Reference Manual

Link: <https://releases.llvm.org/11.0.0/docs/LangRef.html#introduction>

Link to LLVMLite docs: <https://llvmlite.readthedocs.io/en/latest/>

## Commands to Generate Output file & Run Executable

$ llc -filetype=obj output.ll

$ gcc output.o -o output

$ ./output

