workers = 2  # تقليل عدد العمال
worker_class = 'sync'
bind = "0.0.0.0:8000"
timeout = 120
max_requests = 1000
max_requests_jitter = 50
