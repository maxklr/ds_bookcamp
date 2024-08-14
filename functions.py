from collections import defaultdict
import itertools
from itertools import product


def get_matching_event(event_condition, sample_space):
    return set([outcome for outcome in sample_space if event_condition(outcome)])

# Computing event probabilities
def compute_probability(event_condition, generic_sample_space):
    # The compute_probability function extracts the event associated with
    # an inputted event condition to compute its probability
    event = get_matching_event(event_condition, generic_sample_space)
    # Probability is equal to event size divided by sample space size
    # print(f"{event}: {len(event)} / {generic_sample_space}: {len(generic_sample_space)}")
    return len(event) / len(generic_sample_space)

def is_in_interval(number, minimum, maximum):
    return minimum <= number <= maximum

def generate_coin_sample_space(num_flips=10):
    weighted_sample_space = defaultdict(int)
    for coin_flips in product(['Heads', 'Tails'], repeat=num_flips):
        heads_count = len([outcome for outcome in coin_flips if outcome == 'Heads'])
        weighted_sample_space[heads_count] += 1
    return weighted_sample_space