import mysql.connector

Info = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    db="music_player"
)
cursor = Info.cursor(buffered=True)

def registerUser(data):
    try:
        cursor.execute('INSERT INTO `login` (`uname`, `upass`, `umail`) VALUES (%s,%s,%s)', data)
        Info.commit()
        return True
    except Exception as e:
        print('Error registering user.')
        return False
    
def loginUser(data):
    try:
        cursor.execute('select * from login where uname=%s and upass=%s',data)
        return cursor.fetchone()
    except:
        return False
