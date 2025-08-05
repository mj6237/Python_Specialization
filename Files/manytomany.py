import json
import sqlite3

# Database se connect karein
conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

# Tables ko drop karein agar pehle se mojood hain, phir naye tables banayein
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
);
''')

# JSON file ka naam
fname = 'roster_data.json'
try:
    with open(fname) as f:
        # JSON data parhein aur parse karein
        data = json.load(f)
except FileNotFoundError:
    print(f"File '{fname}' not found. Please make sure it's in the same directory.")
    conn.close()
    exit()

# Har record ko process karein
for entry in data:
    name = entry[0]
    title = entry[1]
    role = entry[2]

    print(f"Processing: {name}, {title}, {role}")

    # User table mein data daalein (ya maujood record ki id lein)
    cur.execute('INSERT OR IGNORE INTO User (name) VALUES (?)', (name,))
    cur.execute('SELECT id FROM User WHERE name = ?', (name,))
    user_id = cur.fetchone()[0]

    # Course table mein data daalein (ya maujood record ki id lein)
    cur.execute('INSERT OR IGNORE INTO Course (title) VALUES (?)', (title,))
    cur.execute('SELECT id FROM Course WHERE title = ?', (title,))
    course_id = cur.fetchone()[0]

    # Member table mein user_id, course_id, aur role daalein.
    # REPLACE ka istemal kiya gaya hai taake agar koi record pehle se mojood ho to usay update kar diya jaye.
    cur.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id, role) VALUES (?, ?, ?)''',
        (user_id, course_id, role))

# Tabdiliyan database mein save karein
conn.commit()
print("\nDatabase updated successfully.")

# --- Verification Queries ---
print("\nRunning first verification query:")
sqlstr1 = '''
SELECT User.name, Course.title, Member.role FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY User.name DESC, Course.title DESC, Member.role DESC LIMIT 2;
'''
for row in cur.execute(sqlstr1):
    print(str(row[0]) + '|' + str(row[1]) + '|' + str(row[2]))

print("\nRunning second verification query:")
sqlstr2 = '''
SELECT 'XYZZY' || hex(User.name || Course.title || Member.role ) AS X FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY X LIMIT 1;
'''
for row in cur.execute(sqlstr2):
    print(str(row[0]))

# Connection band karein
cur.close()
conn.close()

print("\nProgram complete. 'rosterdb.sqlite' file ab grading ke liye taiyar hai.")
