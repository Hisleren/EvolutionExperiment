import random
import config
import generate_population

def simulate_life(population):
    return {
        individual_id: traits
        for individual_id, traits in population.items()
        if all(
            config.environment[trait][0] < traits[trait][-1] < config.environment[trait][1]
            for trait in config.environment.keys()
        )
    }

def check_generation_number(population, generation_number):
    if not population:
        return population

    generation_to_remove = generation_number - 5
    if generation_to_remove < 0:
        return population

    keys_to_remove = [key for key in population.keys() if key[1] == generation_to_remove]

    for key in keys_to_remove:
        del population[key]
    return population

def exposure_to_radiation(population, exposure_level):
    ratio = 0
    environment = config.environment
    for key in list(population.keys()):
        individual = population[key]
        for trait in environment.keys():
            randomness = 120 - 20 * exposure_level
            if random.choice(range(randomness)) == 19:
                gene_index = random.choice(range(config.individual_gene_length))
                individual[trait][gene_index] = random.choice(list(config.nucleotides.keys()))
                ratio += 1
            individual[trait][-1] = generate_population.calculate_score(individual[trait][:config.individual_gene_length])
        population[key] = individual
    return population

if __name__ == "__main__":
    avg_alive = 0
    try_count = 400
    for i in range(try_count):
        population = generate_population.generate_population()
        simulate_life(population)
        population = exposure_to_radiation(population,config.exposure_level)
        simulate_life(population)
        avg_alive += len(population)
    print(avg_alive/try_count)




