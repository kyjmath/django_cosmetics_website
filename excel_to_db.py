import pandas as pd
import MySQLdb

config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'midproject',  #변경하기
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
}


cos = pd.read_excel("cosmetics_data.xlsx")
#print(cos.columns) 
#print(cos.head(3))
try:
    for i in range(len(cos)):
        sql = """insert into cosmetics(no, brand, product, type, effect, ingredient, price, grade, gender, age, skin_type, pro_image)
        values({},"{}","{}","{}","{}","{}", {}, {},"{}","{}","{}","{}")
        """.format(i + 1, cos.iloc[i]['brand'], cos.iloc[i]['product'], cos.iloc[i]['type'], cos.iloc[i]['effect'],
                   cos.iloc[i]['ingredient'], cos.iloc[i]['price'],cos.iloc[i]['grade'],cos.iloc[i]['gender'],cos.iloc[i]['age'],
                   cos.iloc[i]['skin_type'], cos.iloc[i]['pro_image'])
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    
except Exception as e:
    print('err: ', e)

finally:
    cursor.close()
    conn.close()
