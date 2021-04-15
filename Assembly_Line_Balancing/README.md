# Assembly line balancing
## General info
This folder contains assembly line balancing problem solver. A python script that i've written for a college class. What is a line balancing problem? First let's start whats assembly line.

>An assembly line is a manufacturing process (often called a progressive assembly) in which parts (usually interchangeable parts) are added as the semi-finished assembly moves from workstation to workstation where the parts are added in sequence until the final assembly is produced. By mechanically moving the parts to the assembly work and moving the semi-finished assembly from work station to work station, a finished product can be assembled faster and with less labor than by having workers carry parts to a stationary piece for assembly.
[Assembly line Wiki](https://en.wikipedia.org/wiki/Assembly_line)

So by assembly line balancing problem, we mean finding a order of tasks, for given number of work stations, that gives as well optimized work flow. In order to solve the problem we use heuristics, to determin the rules that we use to order tasks.

Suported heuristics:
* WET - Work Element Time
* RPW - Ranked Positional Weight

Terms and Paramiters:
* K - Total number of workstations
* C - Cycle time
* LE - Line Efﬁciency
* SE - Station time
* T - Duration time


## Technologies
* Python 3.7.3

Libraries:
* Math
* Operator
* Subprocess

## Sources and helpful materials
[Mod-07 Lec-31 Line Balancing](https://www.youtube.com/watch?v=KA8jr4GLzhI)

[A Multi-Objective Genetic Algorithm for Solving Assembly LineBalancing Problem](https://www.researchgate.net/publication/2830101_A_Multi-Objective_Genetic_Algorithm_for_Solving_Assembly_Line_Balancing_Problem)