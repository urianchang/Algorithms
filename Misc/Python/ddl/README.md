# Motivation

At Domino, we use the Kubernetes to run user code as web services. A Kubernetes cluster is made up of **nodes**, each with a capacity for memory, CPUs, and potentially other resources such as GPUs. The user code is run as part of a **deployment** which manages a set of **pods**, each of which contains a set of containers for running the user’s code. To scale out a deployment, one can increase the number of replicas, which will in turn create more pods, which will be spread out amongst the pods.

When defining a pod, we allow the user to define a set of resource requests to indicate the amount of memory their code will need to run. To ensure that the user chooses a sensible value, we would like to examine a node and determine the maximum resources a single node can satisfy (in this example, we will assume the nodes are heterogeneous).

Unfortunately, when we talk to the Kubernetes API, the values returned for memory and cpu can be in arbitrary units. In fact, there turn out to be a few use cases where we will need to interpret various quantities from Kubernetes in arbitrary units.

Internally we will generally want to work with CPU units in millicpu (which is indicated by the suffix "m" in the Kubernetes API) and memory in bytes, since both of these may be represented as integers rather than floating point. We would like to create a library that makes dealing with these values easy for the application developer.

Our goal here is to create working code. Since we only have an hour, it is fine to be pragmatic about design choices.

# Kubernetes API

The Kubernetes API returns information about nodes, deployments, pods, and all other resources as objects. For example, this is the object for a node (note some of the values we might like to interpret are in bold):

```
Name:                   minikube
Role:
Labels:                 beta.kubernetes.io/arch=amd64
                        beta.kubernetes.io/os=linux
                        domino/build-node=true
                        domino/model-node=true
                        kubernetes.io/hostname=minikube
Annotations:            alpha.kubernetes.io/provided-node-ip=192.168.42.84
                        node.alpha.kubernetes.io/ttl=0
                        volumes.kubernetes.io/controller-managed-attach-detach=true
Taints:                 <none>
CreationTimestamp:      Sat, 02 Sep 2017 18:20:10 -0700
Conditions:
 Type           Status  LastHeartbeatTime                LastTransitionTime               Reason                     Message
 ----           ------  -----------------                ------------------               ------                     -------
 OutOfDisk      False   Tue, 05 Sep 2017 21:52:03 -0700  Tue, 05 Sep 2017 20:17:59 -0700  KubeletHasSufficientDisk   kubelet has sufficient disk space available
 MemoryPressure False   Tue, 05 Sep 2017 21:52:03 -0700  Tue, 05 Sep 2017 20:17:59 -0700  KubeletHasSufficientMemory kubelet has sufficient memory available
 DiskPressure   False   Tue, 05 Sep 2017 21:52:03 -0700  Tue, 05 Sep 2017 20:17:59 -0700  KubeletHasNoDiskPressure   kubelet has no disk pressure
 Ready          True    Tue, 05 Sep 2017 21:52:03 -0700  Tue, 05 Sep 2017 20:17:59 -0700  KubeletReady               kubelet is posting ready status
Addresses:
  InternalIP:   192.168.42.84
  Hostname:     minikube
Capacity:
 cpu:           **2**
 memory:        **2048380Ki**
 pods:          110
Allocatable:
 cpu:           **2**
 memory:        **1945980Ki**
 pods:          110
System Info:
 Machine ID:                    1c5f26c32aa14ff5b183ea0ee6982c28
 System UUID:                   56EB4F55-71A9-4655-A78E-FF257D74350B
 Boot ID:                       4d032212-e8e4-4de1-8aad-37410fdbae67
 Kernel Version:                4.9.13
 OS Image:                      Buildroot 2017.02
 Operating System:              linux
 Architecture:                  amd64
 Container Runtime Version:     docker://1.12.6
 Kubelet Version:               v1.7.0
 Kube-Proxy Version:            v1.7.0
ExternalID:                     minikube


Non-terminated Pods:            (9 in total)
  Namespace                     Name                                                    CPU Requests    CPU Limits      Memory Requests         Memory Limits
  ---------                     ----                                                    ------------    ----------      ---------------         -------------
  default                       domino-watch-event-pump-3808124255-g2jzb                **0** (0%)          **0** (0%)          **0** (0%)                  **0** (0%)
  default                       fluentd-es-7zj42                                        **0** (0%)          **0** (0%)          **0** (0%)                  **0** (0%)
  default                       model-59af27a095c85cfef9cf0cce-339589512-vjj7q          **1735m** (86%)     **1735m** (86%)     **1350767214** (67%)        **1350767214** (67%)
  default                       rabbitmq-cluster-3810249292-gdrhd                       **0** (0%)          **0** (0%)          **0** (0%)                  **0** (0%)
  default                       replicator-l3xhx                                        **0** (0%)          **0** (0%)          **0** (0%)                  **0** (0%)
  default                       traefik-ingress-2599205384-nr21c                        **0** (0%)          **0** (0%)          **0** (0%)                  **0** (0%)
  kube-system                   kube-addon-manager-minikube                             **5m** (0%)         **0** (0%)          **50Mi** (2%)               **0** (0%)
  kube-system                   kube-dns-910330662-k6hb6                                **260m** (13%)      **0** (0%)          **110Mi** (5%)              **170Mi** (8%)
  kube-system                   kubernetes-dashboard-144gj                              **0** (0%)          **0** (0%)          **0** (0%)                  **0** (0%)
Allocated resources:
  (Total limits may be over 100 percent, i.e., overcommitted.)
  CPU Requests  CPU Limits      Memory Requests         Memory Limits
  ------------  ----------      ---------------         -------------
  **2** (100%)      **1735m** (86%)     **1518539374** (76%)        **1529025134** (76%)
Events:         <none>
```


The kubernetes website says the following about CPU and Memory resources:

**Meaning of CPU**

Limits and requests for CPU resources are measured in cpu units. One cpu, in Kubernetes, is equivalent to:
* 1 AWS vCPU
* 1 GCP Core
* 1 Azure vCore
* 1 Hyperthread on a bare-metal Intel processor with Hyperthreading

Fractional requests are allowed. A Container with spec.containers[].resources.requests.cpu of 0.5 is guaranteed half as much CPU as one that asks for 1 CPU. The expression 0.1 is equivalent to the expression 100m, which can be read as "one hundred millicpu". Some people say “one hundred millicores”, and this is understood to mean the same thing. A request with a decimal point, like 0.1, is converted to 100m by the API, and precision finer than 1m is not allowed. For this reason, the form 100m might be preferred.
CPU is always requested as an absolute quantity, never as a relative quantity; 0.1 is the same amount of CPU on a single-core, dual-core, or 48-core machine.


**Meaning of memory**

Limits and requests for memory are measured in bytes. You can express memory as a plain integer or as a fixed-point integer using one of these suffixes: E, P, T, G, M, K. You can also use the power-of-two equivalents: Ei, Pi, Ti, Gi, Mi, Ki. For example, the following represent roughly the same value:
128974848, 129e6, 129M, 123Mi

This piece of code from the Kubernetes source is more illuminating:

```
type bePair struct {
	base, exponent int32
}

func newSuffixer() suffixer {

	sh := &suffixHandler{}

	// IMPORTANT: if you change this section you must change fastLookup

	sh.binSuffixes.addSuffix("Ki", bePair{2, 10})

	sh.binSuffixes.addSuffix("Mi", bePair{2, 20})

	sh.binSuffixes.addSuffix("Gi", bePair{2, 30})

	sh.binSuffixes.addSuffix("Ti", bePair{2, 40})

	sh.binSuffixes.addSuffix("Pi", bePair{2, 50})

	sh.binSuffixes.addSuffix("Ei", bePair{2, 60})

	// Don't emit an error when trying to produce

	// a suffix for 2^0.

	sh.decSuffixes.addSuffix("", bePair{2, 0})

	sh.decSuffixes.addSuffix("n", bePair{10, -9})

	sh.decSuffixes.addSuffix("u", bePair{10, -6})

	sh.decSuffixes.addSuffix("m", bePair{10, -3})

	sh.decSuffixes.addSuffix("", bePair{10, 0})

	sh.decSuffixes.addSuffix("k", bePair{10, 3})

	sh.decSuffixes.addSuffix("M", bePair{10, 6})

	sh.decSuffixes.addSuffix("G", bePair{10, 9})

	sh.decSuffixes.addSuffix("T", bePair{10, 12})

	sh.decSuffixes.addSuffix("P", bePair{10, 15})

	sh.decSuffixes.addSuffix("E", bePair{10, 18})

	return fastLookup{sh}

}
```
