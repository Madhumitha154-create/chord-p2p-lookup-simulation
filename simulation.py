import simpy
import random
from chord import Node

def lookup_process(env, node, key, nodes, results, paths):
    yield env.timeout(1)
    hops = node.find_successor(key, nodes)
    results.append(len(hops))
    paths.append(hops)

def run_simulation(num_nodes, m):
    env = simpy.Environment()

    nodes = sorted(random.sample(range(2**m), num_nodes))
    node_objs = {n: Node(n, m) for n in nodes}

    # Build finger tables
    for node in node_objs.values():
        node.build_finger_table(nodes)

    results = []
    paths = []

    # Run multiple lookups
    for _ in range(15):
        node_id = random.choice(nodes)
        key = random.choice(nodes)
        env.process(lookup_process(env, node_objs[node_id], key, nodes, results, paths))

    env.run()

    return nodes, node_objs, results, paths