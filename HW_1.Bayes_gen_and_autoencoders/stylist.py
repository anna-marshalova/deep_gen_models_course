import itertools
import random
from typing import Dict, List, Tuple


class Combination:
    def __init__(self, attributes: List[str],
                 values_probs: List[Tuple[str, float]]):
        assert len(attributes) == len(values_probs)
        self.attributes = attributes
        p = 1
        style = {}
        for attribute, (value, prob) in zip(attributes, values_probs):
            style.update({attribute: value})
            p *= prob
        self.style = style
        self.p = p

    def __str__(self):
        return "\n".join(
            f"{attribute.capitalize()}: {value}"
            for attribute, value in self.style.items()
        )

    def get_prob(self):
        return self.p


class Stylist:
    def __init__(
            self,
            styles: Dict[str, List[str]],
            styles_count: Dict[str, List[int]],
            epsilon: int = 1,
    ):
        self.styles = styles
        self.styles_count = styles_count
        self.epsilon = epsilon
        self.attributes = list(styles.keys())
        self.styles_probs = self.get_probs()
        self.combinations = self.generate_combinations()
        self.combination_probs = [
            combination.get_prob() for combination in self.combinations
        ]

    def get_probs(self):
        styles_probs = {}
        for attribute in self.attributes:
            styles_probs.update({attribute: {}})
            variants = self.styles[attribute]
            freqs = self.styles_count.get(attribute,
                                          [self.epsilon for _ in variants])
            for variant, freq in zip(variants, freqs):
                N = sum(freqs)
                d = len(freqs)
                prob = (freq + self.epsilon) / (N + d * self.epsilon)
                styles_probs[attribute].update({variant: prob})
        return styles_probs

    def generate_combinations(self):
        all_variants_probs = [
            variants.items() for variants in self.styles_probs.values()
        ]
        combinations = list(itertools.product(*all_variants_probs))
        return [
            Combination(self.attributes, values_probs) for values_probs in
            combinations
        ]

    def suggest_style(self):
        choice = random.choices(
            population=self.combinations, weights=self.combination_probs, k=1
        )[0]
        prob = round(choice.get_prob(), 5)
        print(f"Here is your style:\n\n{choice}")
        print(f"\nProbability of this combination: {prob}")


if __name__ == "__main__":
    from styles import styles, styles_count

    stylist = Stylist(styles, styles_count)
    stylist.suggest_style()
