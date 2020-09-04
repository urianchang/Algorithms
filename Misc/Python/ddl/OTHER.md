# Motivation

At Domino, we use a system called Kubernetes for container orchestration. The Kubernetes API allows for memory and CPU resource to be requested. It can also return information about resources associated with a job or compute node. Unfortunately, Kubernetes returns these quantities as strings with arbitrary units. We want to be able to parse these strings, do math on them, and be able to use the results to make future requests.

# Kubernetes API

The Kubernetes API returns information about nodes, deployments, pods, and all other resources as objects. For example, this is the object for a node (note some of the values we might like to interpret are in bold):

| Quantity | Meaning                       |
|----------|-------------------------------|
| 129M     | 129 megabytes (base 10)       |
| 123Mi    | 123 megabytes (base 2)        |
| 100m     | 100 millis                    |
| 1        | 1 (could be a byte, or a cpu) |
| 129e6    | 129000000                     |


The same units can apply to both CPU and memory.

Base 2 units:

| Unit | Value  |
|------|--------|
| Ki   | 2^10   |
| Mi   | 2^20   |
| Gi   | 2^30   |
| Ti   | 2^40   |
| Pi   | 2^50   |
| Ei   | 2^60   |


Base 10 units:

| Unit | Value  |
|------|--------|
| n    | 10^-9  |
| u    | 10^-6  |
| m    | 10^-3  |
| k    | 10^3   |
| M    | 10^6   |
| G    | 10^9   |
| T    | 10^12  |
| P    | 10^15  |
| E    | 10^18  |

We want to be able to write a parser that can interpret strings in this format and a library that will help us add, subtract, and convert these quantities to other units.

# Use Case

One use case of this library would be to determine the amount of memory remaining on a node. Support the case of getting the amount of memory on a node and subtracting memory requests for each pod running on it.

For example, given:

* Node memory: 4Gi
* Pod 1: 1.5M
* Pod 2: 2097152
* Pod 3: 127378Ki

How much space is left?

# Exercises
- Write a parser
- Add the ability to convert between units
- Add operators to allow addition and subtration of values in different units
