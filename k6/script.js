import http from 'k6/http';

export let options = {
  vus: 50,           // Number of virtual users (concurrent users)
  duration: '1m',    // Test duration: 1 minute
  thresholds: {
    // Fail the test if error rate exceeds 1%
    'http_req_failed': ['rate<0.01'],
    // Optional: Add response time thresholds
    'http_req_duration': ['p95<200'], // 95% of requests should be below 200ms
  },
};

// Main function that will be executed for each virtual user
export default function () {
  // Make a GET request to the node endpoint
  const response = http.get('http://localhost:8000/nodes/seed-0001');

  // Optional: Add check to verify the response
  check(response, {
    'status is 200': (r) => r.status === 200,
  });
}

// Import check function if used
import { check } from 'k6';
