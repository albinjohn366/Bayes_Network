from model import *
from collections import Counter


def make_sample():
    # Dictionary for storing each sample
    sample = dict()

    # Dictionary for storing each parent
    parents = dict()

    for node in model.states:
        if isinstance(node.distribution, ConditionalProbabilityTable):
            sample[node.name] = node.distribution.sample(parent_values=parents)
        else:
            sample[node.name] = node.distribution.sample()
        parents[node.distribution] = sample[node.name]

    return sample


# Adding samples to a data list
data = []
# Defining sample count
N = 1000
for i in range(N):
    result = make_sample()
    if result['train'] == 'delayed':
        data.append(result['appointment'])
print(Counter(data))
