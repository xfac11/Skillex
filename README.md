# Skillex
Exercise tracker on the command line. Skillex tracks your workout and gives experience points when completeing exercises. Level up and see your stats increase both in real life and digitaly. 

## How to use
1. Start by cloning the latest version: `git clone URL`.

2. Then run sync_exercises.py script in the scripts folder. This downloads the exercises.

3. When that is done, call `uv run skillex init` to create a user

4. Now you can use `add` and `stats` and more to start tracking exercises.

## Commands
- `init NAME`

Adds one user called ``NAME`` and let's you call other commands related to the user.

- `add EXERCISE_NAME / EXERCISE_ID`

Used to add one exercise to the current users log and gain XP. It uses partial search so the name can be partially right. Time, distance, etc is added after choosing the exercise.

- `bodyparts`

Shows a list of available bodyparts

- `search QUERY --bodypart BODYPART`

Searches exercises with the ``QUERY`` and prints out their id and name. Uses partial search. Can use the optional ``--bodypart`` to only show exercises with this bodypart

- `stats`

Shows the current users global and bodyparts level and sleep streak

- `view EXERCISE_ID`

Shows the exercise and its content. Name, bodypart, equipment, target muscle, gif link and instructions.

- `sleep HOURS`

Adds the amount of ``HOURS`` to the sleep log and updates the current users sleep streak. Multiple calls to this with the same user will tell you that you already have logged sleep for today.

- `change NAME`

Changes the current user to this user with this ``NAME``.



## Third-party
- [ExerciseDB API](https://exercisedb.dev/) for getting body parts and exercises. It's an open-source free exercise database.
- [Click](https://click.palletsprojects.com/en/stable/) for creating command line interfaces.
- [SQLite 3](https://docs.python.org/3/library/sqlite3.html) for creating SQLite databases and executing SQL queries.
- [Requests](https://pypi.org/project/requests/) for downloading exercises from the ExerciseDB API
