import csv
import psycopg2

host = 'arjuna.db.elephantsql.com'
user = 'qgjwncfp'
password = 'DjfynfwLe5OuKO0aS1XsEiJMA2oT17e_'
database = 'qgjwncfp'

# host = 'rosie.db.elephantsql.com'
# user = 'blhrawxv'
# password = 'zwcQOCt7eYPxqw6X8CmAGxy_PQfP8WW-'
# database = 'blhrawxv'


connection = psycopg2.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

# https://api.elephantsql.com/console/003c79b5-5719-4a95-b00f-27a38da9a3e1/details


# 커서
cur = connection.cursor()

# 열 조건 (테이블 만들기)
cur.execute(""" CREATE TABLE ck_brand (
                id INTEGER PRIMARY KEY,
                brand VARCHAR(128),
                s_count INTEGER,
                s_start VARCHAR(128),
                s_year INTEGER
                
                );
            """)

try:
    with open('D:\\coding\\section3\\falsk_db\\flask_app\\ck_brand.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for i, row in enumerate(reader):
            cur.execute(f"""INSERT INTO ck_brand (id, brand, s_count, s_start, s_year) 
                            VALUES {i, row['brand'], row['s_count'], row['s_start'], row['s_year']};
                            """)


except IOError as err:
    print('File error: ' + str(err))

# 커서
cur1 = connection.cursor()

# 열 조건 (테이블 만들기)
cur1.execute("""CREATE TABLE ck_menu (
                no INTEGER PRIMARY KEY,
                brand_id INTEGER,
                brand VARCHAR(128),
                menu VARCHAR(128),
                FOREIGN KEY (brand_id) REFERENCES ck_brand(id)
                
                );
            """)

                # FOREIGN KEY (brand_id) REFERENCES ck_brand(id)
                # CONSTRAINT fk_ck_brand
                #     FOREIGN KEY(brand_id) 
                #         REFERENCES ck_brand(id)

try:
    with open('D:\\coding\\section3\\falsk_db\\flask_app\\ck_menu.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for i, row in enumerate(reader):
            cur1.execute(f"""INSERT INTO ck_menu (no, brand_id, brand, menu) 
                            VALUES {i, row['brand_id'], row['brand'], row['menu']};
                            """)

except IOError as err:
    print('File error: ' + str(err))


# Commit 
connection.commit()

"""
# 내용
cur.execute('SELECT * FROM ck_brand;')

result = cur.fetchall()

print(result)

connection.close()

"""


