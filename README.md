
chmod 644 prometheus.yml alert_rules.yml

# Build and deploy services.
docker-compose up --build
