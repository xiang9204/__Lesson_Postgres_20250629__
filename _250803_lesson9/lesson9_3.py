#請幫我建立一個 function
#連線至 postgres DB
#建立連線環境參數的樣版

import psycopg2


def execute_query(connection, query):
    """
    執行 SQL 查詢並回傳結果
    connection: PostgreSQL 連線物件
    query: SQL 查詢字串
    """
    cursor = None
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except psycopg2.Error as e:
        print(f"Error executing query: {e}")
        return None
    finally:
        if cursor:
            cursor.close()


def create_connection():
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="raspberry",
        host="host.docker.internal",
        port="5432"
    )
    return conn

#main function
def main():
    conn = create_connection()

    if conn:
        print("Connection to PostgreSQL DB successful")

        query = """
        SELECT count(*) AS "總筆數"
        FROM "台鐵車站資訊"
        """
        print(f"SQL Query: {query}")
        result = execute_query(conn, query)
        if result:
            print(f"Query result: {result}")

        conn.close()
    else:
        print("Connection to PostgreSQL DB failed")

if __name__ == "__main__":
    main()