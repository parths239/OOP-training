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
    return f" Movie Details: \n\n  Name: {self.title} \n Director: {self.director} \n Year released: {self.release_year} \n Status: {status}"


  