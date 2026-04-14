# 🔵 Chord P2P Lookup Protocol Simulation

* **Name:** Madhumitha S
* **Register Number:** 22MID0154

##  Objective
The objective of this project is to simulate the **Chord Peer-to-Peer (P2P) Lookup Protocol**, which is used in **Distributed Hash Tables (DHTs)**. The system demonstrates efficient key lookup using a **ring topology** and **finger tables**, achieving logarithmic search complexity.

### 🔹 Chord Protocol
Chord is a distributed protocol that enables efficient lookup of keys in a decentralized network. It organizes nodes in a circular identifier space and distributes keys among them.

### 🔹 Consistent Hashing

Chord uses **consistent hashing** to assign:
* Nodes → positions in the identifier space
* Keys → mapped to nodes
This ensures load balancing and scalability.

### 🔹 Ring Topology
All nodes are arranged in a circular structure (ring), where each node maintains information about its successor and predecessor.

### 🔹 Finger Table
Each node maintains a **finger table** to speed up lookup operations.
* It stores references to nodes at specific intervals
* Helps reduce lookup complexity to **O(log N)**

### 🔹 Lookup Process
To find a key:
1. Start from a node
2. Forward the request using finger table entries
3. Continue until the responsible node is found

##  System Architecture
The system consists of:
* **Nodes:** Represent peers in the network
* **Ring Structure:** Circular arrangement of nodes
* **Finger Tables:** Used for efficient routing
* **Lookup Mechanism:** Finds the node responsible for a key
* **Visualization:** Displays ring and lookup path

##  Technologies Used
* Python
* Streamlit (UI)
* NetworkX (Graph Visualization)
* Matplotlib

##  Implementation Details
### 🔹 Features
* Ring topology visualization
* Finger table generation for each node
* Lookup animation showing path traversal
* Dynamic node generation
* Demonstration of O(log N) lookup complexity

##  Sample Output
### 🔹 Ring Topology
* Nodes arranged in circular structure
* Each node assigned an ID
### 🔹 Finger Table
Example:
```
Entry 0: 5
Entry 1: 5
Entry 2: 7
Entry 3: 14
Entry 4: 19
```
### 🔹 Lookup Animation
* Shows path taken to locate a key
* Highlighted using edges (red lines)

## ▶️ How to Run
### Step 1: Install dependencies
```
pip install -r requirements.txt
```
### Step 2: Run the application
```
python -m streamlit run app.py
```
### Step 3: Open in browser


##  Advantages
* Efficient lookup using O(log N) complexity
* Scalable distributed architecture
* Visual understanding of Chord protocol

##  Limitations
* Simulation-based (not real network)
* Limited node size
* No real-time network communication

##  Future Enhancements
* Handle node join/leave dynamically
* Improve visualization animations
* Add real network simulation
* Enhance UI design

## Conclusion
This project successfully demonstrates the working of the Chord P2P Lookup Protocol. The use of ring topology and finger tables enables efficient key lookup, and the visualization provides a clear understanding of how distributed systems perform scalable search operations.



