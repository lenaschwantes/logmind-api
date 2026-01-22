# Deployment Guide

## Docker Deployment

### Prerequisites
- Docker installed
- Docker Compose installed
- OpenAI API key

### Quick Start

1. Clone repository:
```bash
git clone [repository-url]
cd logmind-api
```

2. Configure environment:
```bash
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY
```

3. Run with Docker Compose:
```bash
docker-compose up -d
```

4. Verify deployment:
```bash
curl http://localhost:8000/docs
```

### Management Commands

**Start services:**
```bash
docker-compose up -d
```

**Stop services:**
```bash
docker-compose down
```

**View logs:**
```bash
docker-compose logs -f
```

**Rebuild after code changes:**
```bash
docker-compose up -d --build
```

### Production Considerations

- Use environment-specific `.env` files
- Configure reverse proxy (nginx) for HTTPS
- Set up monitoring and logging
- Consider horizontal scaling with multiple containers
- Implement rate limiting for API endpoints