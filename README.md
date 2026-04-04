# Skillex
Exercise tracker on the command line. Skillex tracks your workout and gives experience points when completeing exercises. Level up and see your stats increase both in real life and digitaly. 

## How to use
1. Start by downloading the latest version and put it into a new folder.
2. Inside a terminal call `skillex init` and follow the instructions. It will create a folder with a profile json-file with the starting stats.
3. Use `skillex bodyparts` to retrieve available bodyparts and then `skillex exercises [body_part]` to get the exercises with that bodypart.
4. Start exercising and when done call `skillex add [exercise_name] [frequency] [distance]`.
5. Call `skillex stats` to see your current progress.
6. Use `skillex sleep [hours_slept]` to track your sleep. This will increase your experience points gained when using `skillex add`.

## Commands
- init NAME

Adds one user called NAME and let's you call other commands related to the user.
- add EXERCISE_NAME / EXERCISE_ID

Used to add one exercise to the current users log and gain XP. It uses partial search so the name can be partially right. Time, distance, etc is added after choosing the exercise.
- bodyparts

Shows a list of available bodyparts
- search QUERY --bodypart BODYPART

Searches exercises with the QUERY and prints out their id and name. Uses partial search. Can use the optional --bodypart to only show exercises with this bodypart
- stats

Shows the current users global and bodyparts level and sleep streak
- view EXERCISE_ID

Shows the exercise and its content. Name, bodypart, equipment, target muscle, gif link and instructions.
- sleep HOURS

Adds the amount of HOURS to the sleep log and updates the current users sleep streak. Multiple calls to this with the same user will tell you that you already have logged sleep for today.
- change NAME
Changes the current user to this user with this NAME.



## Third-party
- [ExerciseDB API](https://exercisedb.dev/) for getting body parts and exercises. It's an open-source free exercise database.
- [Click](https://click.palletsprojects.com/en/stable/) for creating command line interfaces.