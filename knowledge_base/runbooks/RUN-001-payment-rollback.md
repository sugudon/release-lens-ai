---
document_id: RUN-001
document_type: runbook
title: Payment Service Rollback
component: payment
service: payment-service
status: active
---

# RUN-001: Payment Service Rollback

## Purpose

Use this runbook when a Payment Service deployment causes
payment failures, elevated latency, or unexpected provider errors.

## Trigger Conditions

Consider rollback when:

- Payment success rate decreases significantly.
- Payment timeout rate increases.
- Provider error rate increases.
- Retry count increases unexpectedly.
- Checkout failures increase.

## Rollback Procedure

1. Stop the progressive rollout.
2. Review payment success rate.
3. Review payment latency.
4. Review retry count.
5. Review provider error rate.
6. Roll back Payment Service to the previous stable version.
7. Verify payment authorization.
8. Verify checkout completion.
9. Continue monitoring.

## Special Consideration

If the issue is related to Payment API v2 migration,
verify whether the issue is caused by:

- Request schema
- Error handling
- Retry behavior
- Timeout behavior

## Related Documents

- ADR-003 Payment API Migration
- INC-1024 Payment Timeout Incident
- ARCH-003 Checkout Architecture