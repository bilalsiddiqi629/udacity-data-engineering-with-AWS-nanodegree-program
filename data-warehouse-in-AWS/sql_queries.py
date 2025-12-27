import configparser


"""Retrive important information about AWS cluster to be used in program."""
config = configparser.ConfigParser()
config.read('dwh.cfg')

"""Implements queries for dropping each table in database."""

staging_events_table_drop = "DROP TABLE IF EXISTS staging_events"
staging_songs_table_drop = "DROP TABLE IF EXISTS staging_songs"
songplay_table_drop = "DROP TABLE IF EXISTS songplay"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS song"
artist_table_drop = "DROP TABLE IF EXISTS artist"
time_table_drop = "DROP TABLE IF EXISTS time"

"""Implements queries for creating each table in database."""

staging_events_table_create = ("""CREATE TABLE IF NOT EXISTS staging_events (artist text, auth text, firstName text, gender text, itemInSession int, lastName text, length float, level text, location text, method text, page text, registration float, sessionId int, song text, status int, ts int, userAgent text, userId int)""")

staging_songs_table_create = ("""CREATE TABLE IF NOT EXISTS staging_songs (num_songs int, artist_id text, artist_latitude float, artist_longitude float, artist_location text, artist_name text, song_id text, title text, duration float, year int, PRIMARY KEY (song_id))""")

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays (songplay_id int, start_time timestamp, user_id int, level text, song_id int, artist_id int, session_id int, location text, user_agent text)""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS users (user_id int, first_name text, last_name text, gender text, level text)""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs (song_id int, title text, artist_id int, year int, duration float)""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists (artist_id int, name text, location text, latitude float, longitude float)""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time (start_time timestamp, hour int, day int, week int, month int, year int, weekday int )""")


"""Retrive log data of user activity and populate staging tables based on relevant data."""

staging_songs_copy = f"""
COPY staging_songs FROM 's3://udacity-dend/song_data'
CREDENTIALS 'aws_iam_role=arn:aws:iam::691316117809:role/aws-service-role/redshift.amazonaws.com/AWSServiceRoleForRedshift'
REGION 'us-west-2'
FORMAT AS JSON 'auto'
"""

staging_events_copy = f"""
COPY staging_events FROM 's3://udacity-dend/log_data'
CREDENTIALS 'aws_iam_role=arn:aws:iam::691316117809:role/aws-service-role/redshift.amazonaws.com/AWSServiceRoleForRedshift'
REGION 'us-west-2'
FORMAT AS JSON 's3://udacity-dend/log_json_path.json'
"""


"""Implement insert statements to insert data into tables."""

songplay_table_insert = ("""INSERT INTO songplay(songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
                         VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)""")

user_table_insert = ("""INSERT INTO users (user_id, first_name, last_name, gender, level) 
                     VALUES (%s, %s, %s, %s, %s)""")

song_table_insert = ("""INSERT INTO songs (song_id, title, artist_id, year, duration)
                     VALUES (%s, %s, %s, %s, %s)""")

artist_table_insert = ("""INSERT INTO artist(artist_id, name, location, latitude, longitude) 
                       VALUES (%s, %s, %s, %s, %s)""")

time_table_insert = ("""INSERT INTO time(start_time, hour, day, week, month, year, weekday)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)""")

"""Compile final query lists to be used in other programs."""

create_table_queries = [staging_events_table_create, staging_songs_table_create, songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [staging_events_table_drop, staging_songs_table_drop, songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
copy_table_queries = [staging_events_copy, staging_songs_copy]
insert_table_queries = [songplay_table_insert, user_table_insert, song_table_insert, artist_table_insert, time_table_insert]