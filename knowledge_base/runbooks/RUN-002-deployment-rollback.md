---
document_id: RUN-002
document_type: runbook
title: Deployment Rollback
component: platform
service: deployment-platform
status: active
---

# RUN-002: Deployment Rollback

## Purpose

This runbook describes the standard production deployment rollback.

## Trigger Conditions

Rollback may be required when:

- Error rates increase
- Critical functionality fails
- API contracts break
- Database compatibility issues occur
- Performance significantly degrades

## Procedure

1. Stop deployment.
2. Identify the affected release.
3. Review application health.
4. Review logs and metrics.
5. Determine whether rollback is safe.
6. Roll back application instances.
7. Validate health checks.
8. Validate critical user journeys.
9. Monitor production metrics.

## Validation

Critical validation flows include:

- Login
- Product search
- Cart
- Checkout
- Payment
- Order creation

## Related Documents

- INC-1042 Deployment Failure
- RUN-004 Production Incident Handling