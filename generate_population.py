import random
import config
import life_simulation

def generate_population():
    nucleotides_list = config.nucleotides_list
    population_count = config.population_count
    individual_gene_length = config.individual_gene_length
    environment = config.environment
    nucleotides = config.nucleotides
    population = {}
    for individual in range(population_count):
        population[individual,0] = {}
        for criterion in environment.keys():
            gene = []
            score = 0
            for _ in range(individual_gene_length):
                gene.append(random.choice(nucleotides_list))
            gene.append(calculate_score(gene))
            population[individual,0][criterion] = gene
    return population

def calculate_score(gene):
    score = 0
    nucleotides = config.nucleotides
    for x in gene:
        score += nucleotides[x]
    return score

def sort_population(population):
    fitness_scores = {
        individual_id: sum(traits[trait][-1] for trait in config.environment.keys())
        for individual_id, traits in population.items()
    }
    return sorted(fitness_scores.items(), key=lambda x: x[1], reverse=True)

def calculate_count_of_parents(population):
    count_of_parents = int(config.reproduction_rate * len(population))
    if count_of_parents % 2 != 0:
        count_of_parents += 1
    return count_of_parents


def reproduce(population, last_individual_number,generation_number):
    count_of_parents = calculate_count_of_parents(population)
    n = last_individual_number
    sorted_population = sort_population(population)
    gene_length = config.individual_gene_length
    for i in range(0, count_of_parents, 2):
        if i + 1 >= len(sorted_population):
            break
        n += 1
        population[n,generation_number] = {}
        parent1_id = sorted_population[i][0]
        parent2_id = sorted_population[i + 1][0]

        for criterion in config.environment.keys():
            parent1_gene = population[parent1_id][criterion][:gene_length]
            parent2_gene = population[parent2_id][criterion][:gene_length]

            combined_genes = parent1_gene + parent2_gene
            new_gene = make_new_individual_genes(combined_genes)
            new_gene.append(calculate_score(new_gene))
            population[n,generation_number][criterion] = new_gene

    population = life_simulation.simulate_life(population)
    return population, n

def make_new_individual_genes(genetic_code):
    nucleotides = []
    for i in range(config.individual_gene_length):
        nucleotides.append(random.choice(genetic_code))
    return nucleotides

if __name__ == "__main__":
    population = {}
    population_count = 1000
    individual_gene_length = 5
    nucleotides = {
        "A": 1,
        "T": 2,
        "G": 1,
        "C": 2
    }
    environment = {
        "length": [6, 8],
        "IQ": [5, 11],
        "speed": [7, 11],
        "strongness": [6, 11]
    }
    population = generate_population()
    print(reproduce(population,1000))







