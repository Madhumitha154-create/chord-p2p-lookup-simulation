import random

class Node:
    def __init__(self, node_id, m):
        self.id = node_id
        self.m = m
        self.finger_table = []

    def build_finger_table(self, nodes):
        self.finger_table = []
        for i in range(self.m):
            start = (self.id + 2**i) % (2**self.m)
            successor = self.find_successor_simple(start, nodes)
            self.finger_table.append(successor)

    def find_successor_simple(self, key, nodes):
        nodes = sorted(nodes)
        for n in nodes:
            if n >= key:
                return n
        return nodes[0]

    def closest_preceding_node(self, key):
        for finger in reversed(self.finger_table):
            if self.id < finger < key:
                return finger
        return self.id

    def find_successor(self, key, nodes):
        hops = [self.id]
        current = self.id

        while True:
            if current == key:
                break

            next_node = None
            for finger in reversed(self.finger_table):
                if (finger - current) % (2**self.m) < (key - current) % (2**self.m):
                    next_node = finger
                    break

            if next_node is None or next_node == current:
                next_node = self.find_successor_simple(key, nodes)

            hops.append(next_node)

            if next_node == key or next_node == current:
                break

            current = next_node

        return hops