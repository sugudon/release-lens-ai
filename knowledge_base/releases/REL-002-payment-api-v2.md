---
document_id: REL-002
document_type: release
title: Payment API v2 Migration
component: payment
service: payment-service
release_date: 2025-11-20
status: completed
---

# REL-002: Payment API v2 Migration

## Summary

The Payment Service was migrated from Payment API v1
to Payment API v2.

## Changes

- Updated payment request schema
- Updated payment response handling
- Updated provider error handling
- Changed retry recommendations
- Improved idempotency handling

## Impacted Components

- Payment Service
- Checkout Service

## Testing

The release included:

- Unit tests
- API contract tests
- Integration tests
- Regression tests
- Payment load testing

## Rollout

The migration was deployed using a controlled rollout.

The team monitored:

- Payment success rate
- Payment latency
- Retry count
- Provider errors
- Checkout completion rate

## Rollback

The Payment Service retained the ability to return to
Payment API v1 during the migration window.

## Related Documents

- ADR-003 Payment API Migration
- ARCH-003 Checkout Architecture
- ARCH-004 Service Dependencies
- INC-1024 Payment Timeout Incident
- TEST-004 Retry and Payment Load Testing
- RUN-001 Payment Rollback