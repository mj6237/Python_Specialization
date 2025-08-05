import sqlite3
import re

# Database se connect karein. Agar file maujood na ho to banayein.
conn = sqlite3.connect('itunes.sqlite')
cur = conn.cursor()

# Tables ko naye सिरे se banayein.
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

# tracks.csv file ko parhein
fname = 'tracks.csv'
try:
    fh = open(fname)
except IOError:
    print(f"File '{fname}' not found. Please make sure it's in the same directory.")
    conn.close()
    exit()

# File se data read karein
data = fh.read()

# CSV file ko lines mein alag karein
lines = data.strip().split('\n')

# Pehli line (header) ko parh kar columns ka index maloom karein
header = lines[0].strip().split(',')
header_map = {column: index for index, column in enumerate(header)}
lines = lines[1:] # Baqi data

# Har line ko process karein
for line in lines:
    line = line.strip().split(',')
    
    # Header map ka istemal kar ke har column ki value ko uske naam se hasil karein
    track_title = line[header_map.get('Track', 0)].strip()
    artist_name = line[header_map.get('Artist', 1)].strip()
    album_title = line[header_map.get('Album', 2)].strip()
    genre_name = line[header_map.get('Genre', 3)].strip()
    
    # Count, Rating, aur Length ko integer mein tabdeel karne se pehle check karein
    try:
        track_count = int(line[header_map.get('Count', 4)].strip())
        track_rating = int(line[header_map.get('Rating', 5)].strip())
        track_length = int(line[header_map.get('Length', 6)].strip())
    except (ValueError, IndexError):
        # Agar koi value integer mein tabdeel na ho sake ya column mojood na ho to is record ko chhor dein
        print(f"Skipping malformed row: {line}")
        continue

    if len(track_title) < 1 or len(artist_name) < 1 or len(album_title) < 1 or len(genre_name) < 1:
        print(f"Skipping incomplete row: {line}")
        continue # Agar koi value missing ho to is record ko chhor dein
        
    print(f"Processing: {track_title}, {artist_name}, {album_title}, {genre_name}")

    # Artist table mein data daalein (ya maujood record ki id len)
    cur.execute('INSERT OR IGNORE INTO Artist (name) VALUES (?)', (artist_name,))
    cur.execute('SELECT id FROM Artist WHERE name = ?', (artist_name,))
    artist_id = cur.fetchone()[0]

    # Genre table mein data daalein (ya maujood record ki id len)
    cur.execute('INSERT OR IGNORE INTO Genre (name) VALUES (?)', (genre_name,))
    cur.execute('SELECT id FROM Genre WHERE name = ?', (genre_name,))
    genre_id = cur.fetchone()[0]

    # Album table mein data daalein (ya maujood record ki id len)
    cur.execute('INSERT OR IGNORE INTO Album (title, artist_id) VALUES (?, ?)', (album_title, artist_id))
    cur.execute('SELECT id FROM Album WHERE title = ?', (album_title,))
    album_id = cur.fetchone()[0]

    # Track table mein data daalein
    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, genre_id, len, rating, count)
        VALUES (?, ?, ?, ?, ?, ?)''',
        (track_title, album_id, genre_id, track_length, track_rating, track_count))

conn.commit()
print("\nDatabase updated successfully.")

# Final query chala kar natija check karein
sqlstr = '''
SELECT Track.title, Artist.name, Album.title, Genre.name 
    FROM Track JOIN Genre JOIN Album JOIN Artist 
    ON Track.genre_id = Genre.ID and Track.album_id = Album.id 
        AND Album.artist_id = Artist.id
    ORDER BY Artist.name LIMIT 3
'''

print("\nRunning verification query...")
for row in cur.execute(sqlstr):
    print(row)

# Database connection ko band karein
conn.close()

print("\nProgram run ho chuka hai. Ab aap 'itunes.sqlite' file ko grading ke liye upload kar sakte hain.")
