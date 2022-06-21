from flask import request

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
trajectory = data
all = {"requests made": requests_made, "unique requests": unique_made, "visited urls": amount_visited, "unique visited urls": amount_unique_visited, "failed requests": requests_failed, "processed requests": requests_processed, "unique processed requests": unique_processed, "unique failed requests": unique_failed, 'trajectory': trajectory}
def start(app):
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
         data[request.remote_addr] = [request.url]
         amount_unique_visited[request.remote_addr] = {}
         amount_unique_visited[request.remote_addr][request.url] = 1


     if amount_unique_visited.get(request.remote_addr).get(request.url) is None:
        amount_unique_visited[request.url] = 1
        if request.url not in str(data[request.remote_addr]):
            data[request.remote_addr].append(request.url)



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
