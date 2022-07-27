"""Construtor de cladograma.

Esse módulo é um construtor de cladograma, no qual espécies são agrupadas a
partir de características mais antigas que prováveis ancestrais em comum
introduziram na evolução.
"""


from typing import Dict, List
from dataclasses import dataclass, field


@dataclass(order=True)
class Species:
    """Gera uma espécie, com ID, nomes e características.

    Quando comparadas, apenas o ID é levado em consideração.

    Args:
        id:
            Número único, identificador da espécie.
        popular_name:
            Nome popular da espécie.
        scientific_name:
            Nome científico da espécie.
        traits:
            Lista de características da espécie.
    """
    id: int
    popular_name: str = field(compare=False)
    scientific_name: str = field(compare=False)
    traits: List["Trait"] = field(compare=False)

    def most_recent_trait(self) -> "Trait":
        return max(self.traits)


@dataclass(order=True)
class Trait:
    """Gera uma característica, com nome, número de mutações, e fitas de DNA.

    Quando comparadas, apenas o número de mutações é levado em consideração.

    Args:
        name:
            Nome da característica.
        mutations_count:
            Número de mutações nas fitas de DNA que define a característica.
        dna_strand_1:
            Primeira fita de DNA.
        dna_strand_2:
            Segunda fita de DNA, de tamanho igual à primeira.
    """
    name: str = field(compare=False)
    mutations_count: int = field(default=0)
    dna_strand_1: str = field(init=False, compare=False)
    dna_strand_2: str = field(init=False, compare=False)


species_list = List[Species]
traits_dict = Dict[str, Trait]


def generate_species(
        catalog: species_list,
        traits: traits_dict) -> None:
    """Dado um número n, gera n espécies e as adiciona à lista de espécies."""
    species_count = int(input())
    for _ in range(species_count):
        entry = input().split()
        id = int(entry[0])
        pop_name = entry[1]
        scientific_name = entry[2]
        traits_list = entry[4:]
        species_traits = []
        for trait in traits_list:
            if trait not in traits:
                traits[trait] = Trait(name=trait)
            species_traits.append(traits[trait])
        catalog.append(Species(id, pop_name, scientific_name, species_traits))


def set_dna_strands(traits: traits_dict) -> None:
    """Dado um número n, adiciona fitas de DNA a n características."""
    traits_count = int(input())
    for counter in range(traits_count):
        trait_name = input()
        traits[trait_name].dna_strand_1 = input()
        traits[trait_name].dna_strand_2 = input()
        if counter == 0:
            ancestral_dna_strand_1 = traits[trait_name].dna_strand_1
            ancestral_dna_strand_2 = traits[trait_name].dna_strand_2
        else:
            for letter in range(len(ancestral_dna_strand_1)):
                pair = traits[trait_name].dna_strand_1[letter]\
                    + traits[trait_name].dna_strand_2[letter]
                ancestral_pair = ancestral_dna_strand_1[letter]\
                    + ancestral_dna_strand_2[letter]
                if pair > ancestral_pair:
                    traits[trait_name].mutations_count += 1


def print_cladogram(
        species: species_list,
        traits: traits_dict) -> None:
    """Imprime o cladograma."""
    for trait in sorted(traits.values()):
        print("CARACTERÍSTICA:", trait.name)
        for spec in sorted(species):
            if trait == spec.most_recent_trait():
                print(spec.id, spec.popular_name, spec.scientific_name)


def main():
    """Executa o programa principal."""
    species = []
    traits = {}
    generate_species(species, traits)
    set_dna_strands(traits)
    print_cladogram(species, traits)


if __name__ == "__main__":
    main()
