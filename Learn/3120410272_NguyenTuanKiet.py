class MovieRatings:
    def rate_movies(scanner):
        for line in scanner:
            line = line.strip() # cắt khoảng trắng
            rates = line.split() # các phần tử căt ra riêng
            num_ratings = int(rates[0]) # phần tử đầu (lượt ratings film)
            movie_ratings = list(map(float,rates[1 : num_ratings + 1])) # lấy ra loạt điểm của ratings 
            avg_rating = sum(movie_ratings) / len(movie_ratings)  # tính trung bình cộng điểm
            title = ' '.join(rates[num_ratings + 1:])  # lấy ra tiêu đề của phim
            print(f"title = {title}, ratings = {num_ratings}, score = {avg_rating:.2f}") # in kết quả theo format


if __name__ == '__main__':
   
    input_data = [
        "4 9.2 9 8 9.5 Seven ",
        "5 8.2 9.5 7 10 Men ",
        "6 5.7 6 9 9 Club Streets"
    ]
    scanner = iter(input_data) # hàm iter để đọc các phần tử kế trong list
    MovieRatings.rate_movies(scanner)
