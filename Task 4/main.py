# Sukurkite klasę "Movie", kuri gebės sukurti objektus 3 savybėm ir 1 metodu. 
# Naudojant šią klasę sukurkite bent du skirtingus objektus.

# Savybės:
# title: string
# director: string
# budget: number

# Metodas: 
# was_expensive() - jeigu filmo "budget" yra daugiau nei 100 000 000 mln USD, tada grąžins True, kitu atveju False.

class Movie:
    def __init__(self, title, director, budget):
        self.title = title
        self.director = director
        self.budget = budget

    def was_expensive(self):
        if self.budget > 100000000:
            print(True)
        else:
            print(False)


movie1 = Movie("QUEEN OF THE DESERT", "Werner Herzog", 120000000)
movie1.was_expensive()

movie2 = Movie("KNOR", " Mascha Halberstad", 90000000)
movie1.was_expensive()
print(movie2.title)