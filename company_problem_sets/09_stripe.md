# Stripe Problem Set

Stripe Problem Set - Commonly reported practical coding, API, and debugging patterns for Stripe SWE interviews

Focus: multi-part implementation tasks, readable code, working with APIs or JSON-like data, debugging existing code, simple system behaviors, and careful edge-case handling.

Stripe interviews are not LeetCode-style in the usual sense. Stripe interviews tend to reward correct, clean solutions over clever algorithm tricks. The practical goal is to write working code, extend existing code, read documentation, and use core data structures well.

## Warmups

1. Parse and validate JSON-like payloads
2. Transform nested transaction records
3. Implement user mention parsing
4. Normalize event log entries
5. Count mentions per user
6. Merge and sort small event streams

## Core

1. Build a rate limiter
2. Add TTL caching behavior
3. Extend a mock API client
4. Aggregate payment events by account
5. Detect duplicate or out-of-order events
6. Implement pagination over a response stream
7. Repair a buggy helper in an existing codebase
8. Extend a small in-memory service
9. Convert between domain objects and wire formats
10. Add validation and error handling to a request pipeline
11. Implement a small webhook processor
12. Debug a partially working integration
13. Add a filter or search feature to an existing endpoint
14. Simulate a simple ledger or account summary view

## Stretch

1. Design a webhook retry queue
2. Implement idempotency keys
3. Build a simplified ledger reconciliation flow
4. Add backoff and retry behavior to an API wrapper
5. Implement a small feature flag store

## Review Modules

- `13_hash_tables/`
- `01_arrays/`
- `03_stacks_and_queues/`
- `05_hashing_and_sets/`
- `08_trees/`
- `10_intervals/`
- `12_graphs/`
