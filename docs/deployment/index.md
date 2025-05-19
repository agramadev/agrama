# Deployment Guide

This guide provides instructions for deploying Agrama in production environments.

## Deployment Options

Agrama can be deployed in several ways:

1. **Docker Compose** - Simplest option for single-host deployments
2. **Kubernetes** - For scalable, multi-node deployments
3. **Manual Installation** - For custom environments

## Docker Compose Deployment

### Prerequisites

- Docker Engine 20.10+
- Docker Compose 2.0+
- 4GB RAM minimum (8GB recommended)
- 20GB disk space

### Deployment Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/agrama.git
   cd agrama
   ```

2. Configure environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

3. Start the services:
   ```bash
   docker compose -f docker-compose.prod.yml up -d
   ```

4. Verify deployment:
   ```bash
   docker compose -f docker-compose.prod.yml ps
   ```

### Production Configuration

For production deployments, consider the following configurations:

#### Security

- Enable TLS for all services
- Set up authentication for API endpoints
- Use secrets management for sensitive information

#### Persistence

Configure volume mounts for persistent data:

```yaml
services:
  valkey:
    volumes:
      - valkey-data:/data
  faiss:
    volumes:
      - faiss-data:/data
  ollama:
    volumes:
      - ollama-models:/root/.ollama/models

volumes:
  valkey-data:
  faiss-data:
  ollama-models:
```

#### Resource Allocation

Adjust resource limits based on your workload:

```yaml
services:
  valkey:
    deploy:
      resources:
        limits:
          cpus: '2'
          memory: 2G
  faiss:
    deploy:
      resources:
        limits:
          cpus: '2'
          memory: 4G
  ollama:
    deploy:
      resources:
        limits:
          cpus: '4'
          memory: 8G
```

## Kubernetes Deployment

For Kubernetes deployments, we provide Helm charts in the `k8s/` directory.

### Prerequisites

- Kubernetes cluster 1.22+
- Helm 3.0+
- kubectl configured to access your cluster

### Deployment Steps

1. Add the Agrama Helm repository:
   ```bash
   helm repo add agrama https://yourusername.github.io/agrama/charts
   helm repo update
   ```

2. Install the Helm chart:
   ```bash
   helm install agrama agrama/agrama -f values.yaml
   ```

3. Verify the deployment:
   ```bash
   kubectl get pods -l app=agrama
   ```

## Scaling Considerations

### Valkey Scaling

For high-availability Valkey deployments, consider using Valkey Cluster with multiple nodes.

### Faiss Scaling

Faiss can be scaled horizontally by partitioning the index across multiple instances.

### API Server Scaling

The API server can be scaled horizontally behind a load balancer.

## Monitoring

### Health Checks

All services expose health check endpoints:

- Valkey: `valkey-cli ping`
- API Server: `GET /health`

### Metrics

Prometheus metrics are available at:

- API Server: `GET /metrics`

### Logging

All services log to stdout/stderr, which can be collected by your logging infrastructure (e.g., ELK, Loki).

## Backup and Recovery

### Valkey Backup

Configure regular RDB snapshots and AOF persistence:

```yaml
services:
  valkey:
    command: ["valkey-server", "--save", "900 1", "--appendonly", "yes"]
```

### Faiss Backup

Regularly back up the Faiss index files from the mounted volume.

## Upgrading

To upgrade Agrama:

1. Pull the latest changes:
   ```bash
   git pull
   ```

2. Update the services:
   ```bash
   docker compose -f docker-compose.prod.yml pull
   docker compose -f docker-compose.prod.yml up -d
   ```

## Troubleshooting

### Common Issues

#### Connection Errors

If services cannot connect to each other, check:
- Network configuration
- Service discovery settings
- Firewall rules

#### Performance Issues

If experiencing performance degradation:
- Check resource utilization
- Adjust resource limits
- Consider scaling horizontally
