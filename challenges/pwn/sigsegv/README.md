# SIGSEGV

**`Author:`** [hfz](https://github.com/hfz1337)

## Description

A gentle introduction to Stack-based Buffer Overflows.  
SIGSEGV (Segmentation Fault) is the signal sent to a process when it tries to access a non allocated memory region.  
Finding a way to crash a program often means that there's a bug somewhere to be exploited in order to do LPE (Local Privilege Escalation) on the system, or to get RCE (Remote Code Execution) over the network.  
Through this 3 parter, you'll hopefully learn the basics of BOF exploitation on x86-64 bit platforms.

When compiling the program, GCC threw the following warning at my face:
> warning: the `gets' function is dangerous and should not be used

Use `man 3 gets` to know why.

## Solution

Solution of the challenge can be found [here](solution/).
