import mysql.connector, os
from dotenv import load_dotenv


def box(data):
    load_dotenv(os.path.join(os.getcwd(), '.env'))
    load_dotenv(os.path.join(os.getcwd(), '.credentials', '.env'))
    try:
        with mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            username=os.getenv("DB_USERNAME"),
            port='3306',
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
            charset='utf8mb4',
        ) as connection:
            print("Connected to MySQL database ", connection._host, " as ", connection._user, " on port ", connection._port, " with database ", connection._database)
            cursor = connection.cursor(buffered=True)
            try:
                unpack(data, cursor)
                remove_duplicate_rows(cursor)
                connection.commit()
                connection.close()
            except Exception as e:
                print("Error unpacking data: ", e)
    except:
        print("Error connecting to MySQL database")


def unpack(data, c):
    insert = data['data']
    title = insert['title']
    description = insert['description']
    eq_image = insert['eq_image']
    parent_cat = insert['parent_cat']
    product_id = insert['product_id']
    technical_specs = insert['technical_specs']
    equip_link = data['url']
    table = os.getenv("DB_TABLE")
    
    #check if a row with this product_id already exists
    product_id_check = c.execute("SELECT * FROM "+table+" WHERE product_id = %s", (product_id,))
    # if it does, update the row; if not, add a new row
    if product_id_check:
        c.execute("UPDATE "+table+" SET title = %s, description = %s, eq_image = %s, parent_cat = %s, technical_specs = %s, equip_link = %s WHERE product_id = %s", (title, description, eq_image, parent_cat, technical_specs, equip_link, product_id))
    else: 
        c.execute("INSERT INTO "+table+" (title, description, eq_image, parent_cat, product_id, technical_specs, equip_link) VALUES (%s, %s, %s, %s, %s, %s, %s)", (title, description, eq_image, parent_cat, product_id, technical_specs, equip_link))

def remove_duplicate_rows(c):
    table = os.getenv("DB_TABLE")
    #find duplicate rows where the product_id is the same and delete all but the first
    c.execute("DELETE t1 FROM "+table+" t1 INNER JOIN "+table+" t2 WHERE t1.id < t2.id AND t1.product_id = t2.product_id")
    