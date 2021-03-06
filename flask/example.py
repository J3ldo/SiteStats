from flask import Flask, request

app = Flask(__name__)


requests_made = 0
unique_made = 0
amount_visited = {}
amount_unique_visited = {}
data = {}

requests_processed = 0
requests_failed = 0
unique_processed = 0
unique_failed = 0
processed_data = {}
@app.before_request
def not_important():
   global requests_made, unique_made, requests_failed, requests_processed, unique_processed, processed_data, unique_failed

   requests_made += 1
   requests_failed += 1
   try: amount_visited[request.url] += 1
   except: amount_visited[request.url] = 1

   if data.get(request.remote_addr) is None:
       unique_made += 1
       unique_failed += 1
       data[request.remote_addr] = {request.url: 1}
       amount_unique_visited[request.url] = 1

   elif data.get(request.remote_addr).get(request.url) is None:
       amount_unique_visited[request.url] = 1


@app.after_request
def not_important2(_):
    global requests_made, unique_made, requests_failed, requests_processed, unique_processed, processed_data, unique_made, unique_failed

    requests_processed += 1
    requests_failed -= 1
    if processed_data.get(request.remote_addr) is None:
        unique_processed += 1
        unique_failed -= 1
        processed_data[request.remote_addr] = 1

    return _


@app.route('/')
def index():
    return "<h1><a href="/more">Basic site</a></h1>"
  
 @app.route('/more')
def index():
    print("Exit the program (Ctrl-c) to see the final stats")
    return "<h1>Look another part of the site</h1>"

try:
    app.run("0.0.0.0", 80)
finally:
    print(
        f"Amount of total request made: {requests_made},\n"
        f"Amount of unique requests made: {unique_made},\n"
        f"Amount of requests that failed: {requests_failed},\n"
        f"Amount of unique requests that failed: {unique_failed},\n\n"
        f"Amount of requests that came through: {requests_processed},\n"
        f"Amount of unique requests that came through: {unique_processed},\n"
        f"Amout of unique visitors urls: {amount_unique_visited},\n"
        f"Amount of visited urls: {amount_visited},\n"
        f"Devices that connected ipv4 adresses (debug): {processed_data}.\n")
