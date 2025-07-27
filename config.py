population_count = input("Population count: ")
if population_count == "":
    population_count = 1000
else:
    try:
        population_count = int(population_count)
    except ValueError:
        print("Your input is not a integer, 1000 will be used instead")
        population_count = 1000
        pass
generation_number = input("Generation number: ")
if generation_number == "":
    generation_number = 100
else:
    try:
        generation_number = int(generation_number)
    except ValueError:
        print("Your input is not a integer, 100 will be used instead")
        generation_number = 100
        pass
individual_gene_length = input("Individual gene length: ")
if individual_gene_length == "":
    individual_gene_length = 5
else:
    try:
        individual_gene_length = int(individual_gene_length)
    except ValueError:
        print(f"Your {individual_gene_length} input is not a integer, 5 will be used instead")
        individual_gene_length = 5
        pass

reproduction_rate = input("Reproduction Rate: ")

if reproduction_rate == "":
    reproduction_rate = 0.8
else:
    try:
        reproduction_rate = float(reproduction_rate)
    except ValueError:
        print(f"Your {reproduction_rate} input is not a float, 0.3 will be used instead")
        reproduction_rate = 0.8
        pass

last_individual_number = population_count

nucleotides = {
        "A": 1,
        "T": 2,
        "G": 2,
        "C": 1
    }

nucleotides_list = list(nucleotides.keys())
environment = {
    # min and max values
    "length": [min(nucleotides.values()) * individual_gene_length + 1, max(nucleotides.values()) * individual_gene_length - 1],
    "IQ": [min(nucleotides.values()) * individual_gene_length, max(nucleotides.values()) * individual_gene_length + 1],
    "speed": [min(nucleotides.values()) * individual_gene_length + 1, max(nucleotides.values()) * individual_gene_length + 1],
    "strongness": [min(nucleotides.values()) * individual_gene_length + 1, max(nucleotides.values()) * individual_gene_length + 1]
}
