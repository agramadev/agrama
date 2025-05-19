import http from 'k6/http';
import { check, sleep, group } from 'k6';
import { Rate, Trend } from 'k6/metrics';

// Custom metrics
const errorRate = new Rate('errors');
const nodeGetTrend = new Trend('node_get_time');
const searchTrend = new Trend('search_time');

export let options = {
  stages: [
    { duration: '30s', target: 20 },  // Ramp up to 20 users over 30 seconds
    { duration: '1m', target: 50 },   // Ramp up to 50 users over 1 minute
    { duration: '30s', target: 50 },  // Stay at 50 users for 30 seconds
    { duration: '30s', target: 0 },   // Ramp down to 0 users
  ],
  thresholds: {
    'http_req_failed': ['rate<0.01'],         // Error rate < 1%
    'http_req_duration': ['p95<200'],         // 95% of requests < 200ms
    'node_get_time': ['avg<50', 'p95<100'],   // Node GET avg < 50ms, p95 < 100ms
    'search_time': ['avg<100', 'p95<200'],    // Search avg < 100ms, p95 < 200ms
  },
};

export default function () {
  group('Node operations', function () {
    // Get a specific node
    let nodeRes = http.get('http://localhost:8000/nodes/seed-0001');

    // Record custom metric for node GET
    nodeGetTrend.add(nodeRes.timings.duration);

    // Check if request was successful
    let nodeSuccess = check(nodeRes, {
      'node status is 200': (r) => r.status === 200,
      'node has valid data': (r) => r.json().hasOwnProperty('uuid'),
    });

    // Record errors
    errorRate.add(!nodeSuccess);

    // Small pause between requests
    sleep(1);
  });

  group('Search operations', function () {
    // Perform a semantic search
    let searchPayload = JSON.stringify({
      query: "example search query",
      limit: 5
    });

    let searchRes = http.post('http://localhost:8000/semantic_search', searchPayload, {
      headers: { 'Content-Type': 'application/json' },
    });

    // Record custom metric for search
    searchTrend.add(searchRes.timings.duration);

    // Check if request was successful
    let searchSuccess = check(searchRes, {
      'search status is 200': (r) => r.status === 200,
      'search returns results': (r) => Array.isArray(r.json()),
    });

    // Record errors
    errorRate.add(!searchSuccess);

    // Small pause between requests
    sleep(1);
  });
}
