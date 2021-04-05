# Planning Session: 4/5/2021

## General Scope and Scale

* **Essential Game Loop** *(MVP)*
  * Two players will be shooting gates at each other
  * Two grids, one per player.
  * One ship per player.
  * Whoever has the most damage on their ship at the end of the game loop (5 turns?) loses.

Pseudocode for the game loop is as follows:

```python
hadamard = qis_kit.hadamard() # Instantiate a new Hadamard
cx = qis_kit.cx() # Instantiate a new CNOT

# TODO: Create a bunch of shots to create bell pairs

for bell_pair in bell_pairs:
  hadamard.apply(bell_pair)
  cx.apply(bell_pair)

```

* **"Advanced Features"**
  * Additional weapons (other types of gates)
    * Currently uses the Hadamard Gate and the CNOT to create Bell Pairs
    * However many bell pairs are in the 1 state are how much health you have; 0 state is how much damage you've taken.
      * i.e.) If 76/100 bell pairs are in the 0 state, then you have "76%" health
  * Bomb candidates
    * We could use the RY gate to throw off the basis
      * Could be dangerous; would add to the amount of "weather" that the qbits experience and potentially prematurely collapse the wavefunction.
    * We could use *another* CNOT gate on the entangled qbit to create potential for half of the bell pairs to disagree with each other
      * EZ-PZ implementation ==> Good target!
    * The magical mystery gate: Tack an X on at the end of the circuit
      * Just slap it on there with the might of Zeus
      * Maybe it's a tactical nuke? Maybe not? The world won't know until you try!
  * "Health Steal" Attack
    * Uses quantum teleportation to "steal" bell pairs from the opponent.
    * Depending upon which bell pairs you steal your health could go up or down!
  * Map propositions

    ```text
    Ex. 1: The "classic" quantum battleship map
    o-----o
    |\   /|
    | \ / |
    |  o  |
    | / \ |
    |/   \|
    o-----o

    Ex. 2: The "less-classic" quantum battleship map
    o-----o
    |     |
    |     |
    |     |
    |     |
    |     |
    o-----o
    ```

Pseudocode for shooting:

```python
if ship.location is location: # If the ship is here
  # You've found the ship. Shoot!
else:
  # Miss!
```

## Task List

* Get this sucker compatible with QISKit
  * This might get spicy; likely going to require a full port.
* How quantum is this going to be?
  * See the above. Very quantum. Honestly just getting this implemented is ambitious enough.
* Wait for Marc to emerge from under 308/350 rock before he starts contributing actively to this repo :))))))
