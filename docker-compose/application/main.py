from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

def get_movies():
    try:
        connection = psycopg2.connect(
            database="movies",
            user="moviemaker",
            password="SuPerSeCrETPassWORD",
            host="postgres",
            port="5432"
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
