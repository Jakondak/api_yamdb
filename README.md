# Yamdb

The project collects user reviews (Review) for works (Titles). Works are divided into categories: Books, Movies, and Music. The Category list can be expanded by the administrator (e.g., the category "Fine Art" or "Jewelry" can be added).
The works themselves are not stored in YaMDb, you cannot watch a movie or listen to music here.
Each category has works: books, movies, or music. For example, the Books category may include Winnie the Pooh and Everything and The Martian Chronicles, and the Music category may include Daverday by Insects and Bach's second suite.
A work can be assigned a genre (Genre) from the preset list (for example, "Fairy Tale," "Rock," or "Art House"). New genres can only be created by the administrator.
Thanked or annoyed users leave reviews for their works and rate them from 1 to 10 (whole numbers); the users can form a rating (whole numbers) averaged score for the work. The user can leave only one review for one work.


### How to start:


Create and activate the vertual environment:

```
python3 -m venv env
```

```
source env/bin/activate
```

Install dependencies from the requirements.txt file:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Make migrations:

```
python3 manage.py migrate
```

Start the project:

```
python3 manage.py runserver
```

### API documentation:
```
http://127.0.0.1:8000/redoc/
```
