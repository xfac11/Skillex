# Skillex
Exercise tracker on the command line. Skillex tracks your workout and gives experience points when completeing exercises. Level up and see your stats increase both in real life and digitaly. 

## How to use
1. Start by downloading the latest version and put it into a new folder.
2. Inside a terminal call `skillex init` and follow the instructions. It will create a folder with a profile json-file with the starting stats.
3. Use `skillex bodyparts` to retrieve available bodyparts and then `skillex exercises [body_part]` to get the exercises with that bodypart.
4. Start exercising and when done call `skillex add [exercise_name] [frequency] [distance]`.
5. Call `skillex stats` to see your current progress.
6. Use `skillex sleep [hours_slept]` to track your sleep. This will increase your experience points gained when using `skillex add`.


## Third-party
- [ExerciseDB API](https://exercisedb.dev/) for getting body parts and exercises. It's an open-source free exercise database.
- [Click](https://click.palletsprojects.com/en/stable/) for creating command line interfaces.