from flask import Flask, render_template, request
import search_engine

app = Flask(__name__)

#index
@app.route("/")
def index():
    search_engine.update_database()
    return render_template("index.html")

#results page
@app.route('/search', methods = ["GET", "POST"])
def search():
    query = request.args.get("query")
    q_res_bool = search_engine.search_bool(query)
    q_res_tf_idf = search_engine.search_tf_idf(query)
    return render_template('index.html', query = query, q_res_bool = q_res_bool, q_res_tf_idf = q_res_tf_idf)

if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD']=True
    app.config['DEBUG'] = True
    app.config['SERVER_NAME'] = "127.0.0.1:5000"
    app.run()