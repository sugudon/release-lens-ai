---
document_id: ADR-003
document_type: adr
title: Payment API v1 to v2 Migration
component: payment
service: payment-service
status: accepted
decision_date: 2025-06-20
---

# ADR-003: Payment API v1 to v2 Migration

## Context

The external payment provider is introducing Payment API v2.

Payment API v1 uses the legacy payment authorization request format.

Payment API v2 introduces:

- A new request schema
- Updated error codes
- Improved idempotency handling
- Different retry recommendations

## Decision

ShopSphere will migrate the Payment Service from Payment API v1
to Payment API v2.

The migration will be implemented behind the Payment Service
boundary so that the Checkout Service does not need to communicate
directly with provider-specific APIs.

## Retry Behavior

Payment API v2 recommends a more conservative retry strategy.

The number of retries should be reduced for non-transient failures.

Transient failures may still be retried using controlled backoff.

## Timeout

Payment authorization requests must remain within the checkout
latency budget.

Timeout and retry configuration must therefore be reviewed together.

## Testing Requirements

The migration must include:

- Unit tests
- API contract tests
- Integration tests
- Regression tests
- Load testing for retry behavior

## Rollout

The migration should use a controlled rollout.

The team should monitor:

- Payment success rate
- Payment latency
- Timeout rate
- Retry count
- Provider error rate

## Rollback

If Payment API v2 causes unacceptable payment failures,
the Payment Service should be able to return to Payment API v1
during the migration window.

## Related Documents

- ARCH-003 Checkout Service Architecture
- ARCH-004 Service Dependency Map
- INC-1024 Payment Timeout Incident
- RUN-001 Payment Rollback Runbook
- RUN-003 Checkout Troubleshooting
- TEST-004 Retry and Payment Load Testing
- REL-002 Payment API v2 Migration