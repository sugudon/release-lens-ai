---
document_id: INC-1024
document_type: incident
title: Payment Timeout Incident Caused by Retry Configuration
component: payment
service: payment-service
severity: SEV-1
status: resolved
incident_date: 2025-07-14
---

# INC-1024: Payment Timeout Incident

## Summary

On 2025-07-14, ShopSphere experienced elevated checkout failures.

Customers reported that payment processing remained in a pending
state before eventually timing out.

## Impact

Approximately 18% of payment attempts experienced excessive latency
during the incident window.

Checkout completion rate decreased significantly.

## Root Cause

The Payment Service retry configuration was changed during a deployment.

The service retried certain provider failures more aggressively
than expected.

Each retry consumed additional latency within the checkout request.

Under elevated provider latency, multiple retries caused requests
to exceed the checkout timeout budget.

## Contributing Factors

- Retry count was too high.
- Retry behavior was not load tested under provider latency.
- Monitoring did not initially expose retry count clearly.
- The deployment did not include a sufficient rollback checkpoint.

## Resolution

The retry configuration was reduced.

The Payment Service was redeployed.

Checkout latency returned to normal levels.

## Corrective Actions

The team introduced:

- Explicit retry limits
- Exponential backoff
- Retry classification by error type
- Retry-count monitoring
- Load testing for retry configuration changes

## Lessons Learned

Retry configuration must be treated as a production-risk change.

Increasing retries does not necessarily improve reliability.

Retries can amplify downstream failures and increase latency.

## Related Documents

- ADR-003 Payment API v1 to v2 Migration
- ARCH-003 Checkout Service Architecture
- RUN-001 Payment Rollback Runbook
- RUN-003 Checkout Troubleshooting
- TEST-004 Retry and Payment Load Testing
- REL-001 Retry Configuration Update