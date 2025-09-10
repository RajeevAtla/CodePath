def trilogy(year):
	movie_years = {
		2005: "Batman Begins",
		2008: "The Dark Knight",
		2012: "The Dark Knight Rises"
	}
	
	if year in movie_years:
		return movie_years[year]
	else:
		return f"Christopher Nolan did not release a Batman movie in {year}."

year = 2008
print(trilogy(year))

year = 1998
print(trilogy(year))
