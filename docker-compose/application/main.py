from flask import Flask, jsonify
import psycopg2, os

app = Flask(__name__)

def get_movies():
    pg_database = os.environ.get("POSTGRES_DB", "admin")
    pg_port = os.environ.get("POSTGRES_PORT", "5432")
    pg_user = os.environ.get("POSTGRES_USER", "admin")
    pg_password = os.environ.get("POSTGRES_PASSWORD", "123321")
    pg_host = os.environ.get("POSTGRES_HOST", "localhost")
    try:
        connection = psycopg2.connect(
            database = pg_database,
            user = pg_user,
            password = pg_password,
            host = pg_host,
            port = pg_port
        )
        
        cursor = connection.cursor()
        cursor.execute("SELECT name, rating FROM movies")
        movies = cursor.fetchall()

        return [{"name": movie[0], "rating": movie[1]} for movie in movies]
    
    except Exception as error:
        print("Error connecting to PostgreSQL database:", error)
        return []

    finally:
        if connection:
            cursor.close()
            connection.close()

@app.route('/movies', methods=['GET'])
def movies():
    movie_list = get_movies()
    
    return jsonify(movie_list)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
