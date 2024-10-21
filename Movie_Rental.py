class movie:
  
  def __init__(self, title, director, release_year):
    self.title = title
    self.director = director
    self.release_year = release_year
    self.is_checked_out = False
    
  def check_out(self):
    if not self.is_checked_out:
      self.is_checked_out = True
    else:
      return f"The movie {self.title} is already checked out"
  
  def check_in(self):
    if self.is_checked_out:
      self.is_checked_out = False
    else:
      return f"The movie {self.title} is not checked out yet"
    
  def __str__(self) -> str:
    status = "Not Available" if self.is_checked_out else "Available"
    return f"\n\nMovie Details: \n\n Name: {self.title} \n Director: {self.director} \n Year released: {self.release_year} \n Status: {status}"


class customer:
  
  def __init__(self, name, customer_id):
    self.name = name
    self.customer_id = customer_id
    self.rented_movie = []
  
  def rent_movie(self, movie):
    if movie.is_checked_out:
      return f"The movie is already checked out"
    else:
      self.rented_movie.append(movie)
      movie.check_out()
  
  def return_movie(self, movie):
    if movie in self.rented_movie:
      self.rented_movie.remove(movie)
      movie.check_in()
    else:
      return f"The customer never rented the movie"

  def __str__(self) -> str:
    #movie_title_list = [movie.title for movie in self.rented_movied]
    rented_movies_list = (", ").join(movie.title for movie in self.rented_movie)
    return f" \n Customer Details: \n  Name: {self.name} \n Customer ID: {self.customer_id} \n Rented Movies: {rented_movies_list}"
  
class MovieRentalSystem:
  
  def __init__(self):
    self.movies = []
    self.customers = []
    
  def add_movie(self, movie):
    if movie not in self.movies:
      self.movies.append(movie)
    else:
      return f"Movie is already in the system"
    
  def register_customer(self, customer):
    if customer not in self.customers:
      self.customers.append(customer)
    else:
      return f"Customer {customer.name} is already in the system"
    
  def find_movie_by_title(self, title) -> str:
    for movie in self.movies:
      if movie.title.lower() == title.lower():
        return title
    
    return f"{title} not found"
  
  def __str__(self) -> str:
    print_movies = ("\n").join(str(movie) for movie in self.movies) 
    print_customers = ("\n").join(str(customer) for customer in self.customers)
    return f"\n\n Movie Rental System: \n {print_movies}  \n {print_customers}"
  

if __name__ == "__main__":
  
  FullertonMovieRental = MovieRentalSystem()
  
  movie1 = movie("Shrek", "David A", "1999")
  movie2 = movie("Titanic", "Steven Spielberg", "1996")
  
  FullertonMovieRental.add_movie(movie1)
  FullertonMovieRental.add_movie(movie2)
  
  customer1 = customer("Parth Sharma", "805587359")
  
  FullertonMovieRental.register_customer(customer1)
  customer1.rent_movie(movie1)
  customer1.rent_movie(movie2)
  
  print(FullertonMovieRental)
  
    
    