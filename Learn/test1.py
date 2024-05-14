def input_movie_data():
    title = input("Nhập tiêu đề của phim: ")
    rates = input("Nhập số lượng đánh giá phim : ")
    ratings = []
    for i in range(3):
        rating = float(input(f"Nhập điểm đánh giá thứ {i + 1} của phim: "))
        ratings.append(rating)
    return rates, ratings, title

def calculate_average_rating(ratings):
    return sum(ratings) / len(ratings)

def print_movie_info(rates, title, num_ratings, avg_rating):
    print(f"rates = {rates}, title = {title}, ratings = {num_ratings}, score = {avg_rating:.2f}")

def main():
    movie_list = []

    num_movies = int(input("Nhập số lượng phim bạn muốn quản lý : "))
    for i in range(num_movies):
        print(f"\nNhập thông tin cho phim {i + 1}")
        rates, ratings, title = input_movie_data()
        num_ratings = len(ratings)
        avg_rating = calculate_average_rating(ratings)
        movie_list.append((rates, title, num_ratings, avg_rating))

    print("\nThông tin các phim : ")
    for movie in movie_list:
        print_movie_info(*movie)

if __name__ == "__main__":
    main()
