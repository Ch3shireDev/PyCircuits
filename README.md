# Electric Circuits

My small simulation of electric circuits in Python. Believe me or not, it took me a week to find proper solution - idea is to be able go numerically simulate circuits element by element, without looking at a bigger picture.

14.03: I have completed first version of object-oriented circuit system. First example was put into simple_example.py file, whole OO circuit system is in circuit.py file.

15.03: I have introduced inheritance in circuits. Thanks for that I no longer need auxiliary flags telling me if I should change potential of single nodes. Also I have regorganized nodes and lines into separated files.

Calculating method:

Circuit is described by graph - nodes have associated potentials and lines (wires) have their own functions describing potential change depending on current, time etc. At each step each nodes potential is calculated as an arithmetic mean value from neigbouring points potentials minus potential change on associated wire.

We assume some inertia of current (change of I described by di), so one should also take some basic inductance value L. For now taken value is equal to 1, probably should be much smaller.

TODO: Add diode class. Also, I have in plans transistor class.
