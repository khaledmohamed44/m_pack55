worker_class = 'sync'
workers = 1  # تقليل عدد العمال إلى واحد فقط
threads = 2
bind = "0.0.0.0:10000"
timeout = 300
max_requests = 500
max_requests_jitter = 50
preload_app = True
