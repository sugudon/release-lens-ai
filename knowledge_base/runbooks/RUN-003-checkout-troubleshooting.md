---
document_id: RUN-003
document_type: runbook
title: Checkout Troubleshooting
component: checkout
service: checkout-service
status: active
---

# RUN-003: Checkout Troubleshooting

## Symptoms

Use this runbook when customers report checkout failures,
payment timeouts, or slow checkout responses.

## Investigation Sequence

1. Check Checkout Service health.
2. Check Payment Service health.
3. Check Payment Provider latency.
4. Check payment error rate.
5. Check retry count.
6. Check timeout metrics.
7. Check recent deployments.

## Payment Investigation

If payment failures are elevated, determine whether the problem
is related to:

- Payment API version
- Request schema
- Provider error codes
- Retry behavior
- Timeout configuration

## Escalation

Escalate to the Payment Service team when payment authorization
failures exceed the agreed production threshold.

## Related Documents

- ARCH-003 Checkout Architecture
- INC-1024 Payment Timeout Incident
- INC-1050 Checkout Performance Degradation
- RUN-001 Payment Rollback