# Load Testing with k6

This directory contains load testing scripts for Agrama using [Grafana k6](https://k6.io/).

## Overview

k6 is used in Agrama for load testing the API endpoints to ensure they can handle expected traffic volumes with acceptable performance. The main goal is to verify that the system has less than 1% errors when tested at 100 requests per second (RPS).

## Available Scripts

- `script.js` - Basic load test that simulates 50 virtual users accessing a node endpoint for 1 minute

## Running the Tests

### Using Docker (Recommended)

```bash
# Run the basic load test
docker run --rm -i grafana/k6 run - < k6/script.js

# Run with custom options (e.g., more virtual users)
docker run --rm -i grafana/k6 run --vus 100 --duration 2m - < k6/script.js
```

### Using Make

If you have the Makefile set up, you can simply run:

```bash
make load
```

## Interpreting Results

The test will output metrics including:
- Request rate
- Response time statistics (min, max, average, p90, p95)
- Error rate

The test will fail if:
- Error rate exceeds 1%
- 95th percentile response time exceeds 200ms

## Creating Custom Tests

To create a new test script:

1. Create a new JavaScript file in this directory
2. Import the k6 modules you need
3. Define options and the default function
4. Run the test using the commands above

## Example Custom Test

```javascript
import http from 'k6/http';
import { check, sleep } from 'k6';

export let options = {
  vus: 20,
  duration: '30s',
};

export default function() {
  // Test a different endpoint
  const res = http.get('http://localhost:8000/semantic_search?q=example');
  check(res, {
    'status is 200': (r) => r.status === 200,
  });
  sleep(1);
}
```

## References

- [k6 Documentation](https://k6.io/docs/)
- [k6 Thresholds](https://k6.io/docs/using-k6/thresholds/)
- [k6 Checks](https://k6.io/docs/using-k6/checks/)
