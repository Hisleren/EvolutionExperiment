import generate_population
import life_simulation
import config
import matplotlib.pyplot as plt
import numpy as np


def calculate_generation_stats(population):
    generation_stats = {}

    for (individual_id, generation), traits in population.items():
        if generation not in generation_stats:
            generation_stats[generation] = []
        total_score = sum(traits[trait][-1] for trait in config.environment.keys())
        generation_stats[generation].append(total_score)
    stats = {}
    for gen, scores in generation_stats.items():
        if scores:
            stats[gen] = {
                'average': np.mean(scores),
                'max': np.max(scores),
                'min': np.min(scores),
                'count': len(scores)
            }
    return stats


def plot_generation_scores(generation_data):
    generations = sorted(generation_data.keys())
    averages = [generation_data[gen]['average'] for gen in generations]
    maxes = [generation_data[gen]['max'] for gen in generations]
    mins = [generation_data[gen]['min'] for gen in generations]
    counts = [generation_data[gen]['count'] for gen in generations]

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

    ax1.plot(generations, averages, 'b-', label='Avg Score', linewidth=2)
    ax1.plot(generations, maxes, 'g-', label='Max Score', linewidth=2)
    ax1.plot(generations, mins, 'r-', label='Min Score', linewidth=2)
    ax1.fill_between(generations, mins, maxes, alpha=0.2, color='gray', label='Score Range')

    ax1.set_xlabel('Generation Number')
    ax1.set_ylabel('Fitness Score')
    ax1.set_title('Fitness Score By Generations')
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    ax2.bar(generations, counts, alpha=0.7, color='orange')
    ax2.set_xlabel('Generation Number')
    ax2.set_ylabel('Individual Count')
    ax2.set_title('Indıvidual Count By Generations')
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()


def try_all_functions_with_visualization(generation_count=100):
    generation_number = 0
    population = generate_population.generate_population()
    print(f"Start population: {len(population)}")

    population = life_simulation.simulate_life(population)
    print(f"After simulation: {len(population)}")

    population = life_simulation.exposure_to_radiation(population, 5)
    population = life_simulation.simulate_life(population)
    print(f"After radiation: {len(population)}")

    all_generation_data = {}

    for i in range(generation_count):
        population, config.last_individual_number = generate_population.reproduce(
            population, config.last_individual_number, generation_number
        )
        population = life_simulation.check_generation_number(population, generation_number)
        population = life_simulation.exposure_to_radiation(population, 5)
        population = life_simulation.simulate_life(population)

        current_stats = calculate_generation_stats(population)
        all_generation_data.update(current_stats)

        generation_number += 1
        print(f"Generation {generation_number}: {len(population)} individuals")


    print("\n=== Simulation Finished ===")
    plot_generation_scores(all_generation_data)

    return population, all_generation_data


def analyze_evolution_trends(generation_data):
    generations = sorted(generation_data.keys())
    if len(generations) < 2:
        return

    print("\n=== EVOLUTION TRENDS ===")
    first_gen = generations[0]
    last_gen = generations[-1]

    avg_improvement = generation_data[last_gen]['average'] - generation_data[first_gen]['average']
    max_improvement = generation_data[last_gen]['max'] - generation_data[first_gen]['max']

    print(f"First generation avg score: {generation_data[first_gen]['average']:.2f}")
    print(f"Last generation avg score: {generation_data[last_gen]['average']:.2f}")
    print(f"Avg score improvement: {avg_improvement:.2f}")
    print(f"Max score improvement: {max_improvement:.2f}")

    if len(generations) > 5:
        recent_avg = np.mean([generation_data[gen]['average'] for gen in generations[-5:]])
        early_avg = np.mean([generation_data[gen]['average'] for gen in generations[:5]])
        print(f"Last 5 generations average: {recent_avg:.2f}")
        print(f"First 5 generations average: {early_avg:.2f}")

if __name__ == "__main__":
    population, generation_data = try_all_functions_with_visualization(config.generation_number)
    analyze_evolution_trends(generation_data)


