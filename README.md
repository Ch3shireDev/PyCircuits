# Electric Circuits

My small simulation of electric circuits in Python. Believe me or not, it took me a week to find proper solution - idea is to be able go numerically simulate circuits element by element, without looking at a bigger picture.

Calculating method:

1. Circuit is described by graph - nodes have associated potentials and lines (wires) have their own functions describing potential change depending on current, time etc. At each step each nodes potential is calculated as an arithmetic mean value from neigbouring points potentials minus potential change on associated wire.

We assume some inertia of current (change of I described by di), so one should also take some inductance value L. Calculating method does not require capacity value C.

TODO:

Wire class - any part of the circuit (with given resistance and other parameters, not necessary linear) is described as a simple object. Example is commented, it didn't work exactly well.
