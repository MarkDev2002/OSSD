class MovieRatings:
    @staticmethod
    def rate_movies(scanner):
        for line in scanner:
            line = line.strip()
            rates = line.split()
            num_ratings = int(rates[0])
            
            movie_ratings = [float(rating) for rating in rates[1 : ] if rating.replace('.', '', 1).isdigit()]
            
            title_index = 1 + len(movie_ratings)
            title = ' '.join(rates[title_index : ])
            
            avg_rating = sum(movie_ratings) / len(movie_ratings)
            print(f"title = {title}, ratings = {num_ratings}, score = {avg_rating:.2f}")

if __name__ == '__main__':
    input_data = [
        "4 9.2 9 8 9.5 Seven",
        "5 8.2 9.5 7 10.0 Men",
        "6 5.7 6 9 9.3 Club Streets"
    ]
    scanner = iter(input_data)
    MovieRatings.rate_movies(scanner)

