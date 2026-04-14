import streamlit as st
import matplotlib.pyplot as plt
import time
import random

from simulation import run_simulation
from utils import draw_ring

st.set_page_config(page_title="Chord Simulation", layout="centered")

st.title("🔵 Chord P2P Lookup Protocol Simulation")
st.markdown("""
**Name:** Madhumitha S  
**Register Number:** 22MID0154  
""")
st.markdown("Simulating distributed hash table using Chord Protocol")

# Inputs
num_nodes = st.slider("Number of Nodes", 5, 100, 15)
m = st.slider("Identifier Space (m)", 3, 8, 5)

if "nodes" not in st.session_state:
    st.session_state.nodes = []
    st.session_state.node_objs = {}
    st.session_state.paths = []

# Run Simulation
if st.button("🚀 Run Simulation"):
    nodes, node_objs, results, paths = run_simulation(num_nodes, m)

    st.session_state.nodes = nodes
    st.session_state.node_objs = node_objs
    st.session_state.paths = paths

    st.success("Simulation Completed!")

    # Show average hops
    st.subheader("📊 Performance")
    st.write("Average hops:", round(sum(results)/len(results), 2))

    # Plot graph
    plt.figure()
    plt.plot(results, marker='o')
    plt.xlabel("Lookup Requests")
    plt.ylabel("Number of Hops")
    st.pyplot(plt)

# Show Ring
if st.session_state.nodes:
    st.subheader("🔄 Ring Topology")
    fig = draw_ring(st.session_state.nodes)
    st.pyplot(fig)

# Finger Table Viewer
if st.session_state.nodes:
    st.subheader("📋 Finger Table")

    selected_node = st.selectbox("Select Node", st.session_state.nodes)

    node = st.session_state.node_objs[selected_node]

    for i, finger in enumerate(node.finger_table):
        st.write(f"Entry {i}: {finger}")

# Animate Lookup
if st.session_state.paths:
    st.subheader("🎥 Lookup Animation")

    path = random.choice(st.session_state.paths)

    if st.button("▶ Animate Lookup"):
        placeholder = st.empty()

        for i in range(len(path)):
            fig = draw_ring(st.session_state.nodes, highlight_path=path[:i+1])
            placeholder.pyplot(fig)
            time.sleep(0.7)

        st.success(f"Lookup path: {path}")

