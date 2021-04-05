# Planning Session: 4/5/2021

## General Scope and Scale

* **Game Loop** *(MVP)*
  * Two players will be shooting gates at each other
  * Two grids, one per player.
  * One ship per player.
  * Whoever has the most damage on their ship at the end of the game loop (5 turns?) loses.

* **"Advanced Features"**
  * Additional weapons (other types of gates)
    * Currently uses the Hadamard Gate and the CNOT to create Bell Pairs
    * However many bell pairs are in the 1 state are how much health you have; 0 state is how much damage you've taken.
      * i.e.) If 76/100 bell pairs are in the 0 state, then you have "76%" health

Pseudocode is as follows:

```python
hadamard = qis_kit.hadamard() # Instantiate a new Hadamard
cx = qis_kit.cx() # Instantiate a new CNOT

# TODO: Create a bunch of shots to create bell pairs

for bell_pair in bell_pairs:
  hadamard.apply(bell_pair)
  cx.apply(bell_pair)

```

## Task List

* Get this sucker compatible with QISKit
  * This might get spicy; likely going to require a full port.
* How quantum is this going to be?
  * Quantum logic gates will be used to handle the interaction between shots and