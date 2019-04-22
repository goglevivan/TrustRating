
import sqlite3
def get_data_name(zap):
    '''Данная функция возвращает информацию из БД TrustData по имени'''
    con = sqlite3.connect('D:/TrustRatingSystem/TrustData.db')
    cur = con.cursor()
    cur.execute('select * from mens WHERE name ="'+zap+'";')
    res = cur.fetchall()
    con.commit()
    cur.close()
    con.close()
    analyze = res[0]
    z = []
    for i in analyze:
        z.append(i)
    return z
#print(get_data_name('leon'))

def get_size():
    '''Данная функция возвращает информацию из БД TrustData о количестве записей'''
    con = sqlite3.connect('D:/TrustRatingSystem/TrustData.db')
    cur = con.cursor()
    cur.execute('select id from mens order by id desc limit 1')
    res = cur.fetchall()
    con.commit()
    cur.close()
    con.close()
    analyze = res[0]
    z = analyze[0]
    return int(z)
#print(get_size())

def get_data_id(zap):
    '''Данная функция возвращает информацию из БД TrustData по ид'''
    zap = str(zap)
    con = sqlite3.connect('D:/TrustRatingSystem/TrustData.db')
    cur = con.cursor()
    cur.execute('select * from mens WHERE id ='+zap+';')
    res = cur.fetchall()
    con.commit()
    cur.close()
    con.close()
    analyze = res[0]
    z = []
    for i in analyze:
        z.append(i)
    return z
#print(get_data_id(1))
def get_level(zap):
    alfa = get_data_id(zap)
    return int(alfa[2])
print (get_level(1))

def get_relationships(zap):
    alfa = get_data_id(zap)
    return int(alfa[3])
print(get_relationships(1))