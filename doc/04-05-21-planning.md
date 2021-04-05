# Planning Session: 4/5/2021

## General Scope and Scale

* **Game Loop** (MVP)
  * Two players will be shooting gates at each other
  * Two grids, one per player.
  * One ship per player.
  * Whoever has the most damage on their ship at the end of the game loop (5 turns?) loses.

* "Advanced Features"
  * Additional weapons (other types of gates)
    * Currently uses the Hadamard Gate and the CNOT to create Bell Pairs
    * However many bell pairs are in the 1 state are how much health you have; 0 state is how much damage you've taken.
      * ie.) If 76/100 bell pairs are in the 0 state, then you have "76%" health

## Task List

* Get this sucker compatible with QISKit
  * This might get spicy; likely going to require a full port.
* How quantum is this going to be?
  * Quantum logic gates will be used to handle the interaction between shots and