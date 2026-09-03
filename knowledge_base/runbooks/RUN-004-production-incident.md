---
document_id: RUN-004
document_type: runbook
title: Production Incident Handling
component: platform
service: production
status: active
---

# RUN-004: Production Incident Handling

## Incident Process

1. Detect the issue.
2. Assign an incident owner.
3. Assess severity.
4. Identify affected services.
5. Mitigate customer impact.
6. Investigate root cause.
7. Communicate status.
8. Restore service.
9. Validate critical workflows.
10. Create a post-incident review.

## Critical Services

The following services are considered critical to checkout:

- Checkout Service
- Payment Service
- Order Service
- Inventory Service

## Evidence Collection

During an incident collect:

- Application logs
- Error rates
- Latencies
- Deployment information
- Retry counts
- Provider errors
- Database metrics

## Related Documents

- INC-1024 Payment Timeout Incident
- INC-1050 Checkout Performance Degradation
- RUN-001 Payment Rollback