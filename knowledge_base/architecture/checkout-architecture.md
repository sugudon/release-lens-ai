---
document_id: ARCH-003
document_type: architecture
title: Checkout Service Architecture
component: checkout
service: checkout-service
status: active
version: 2.1
---

# Checkout Service Architecture

Status: Active

## Overview

The Checkout Service coordinates the end-to-end checkout workflow.

The main flow is:

Customer
→ Frontend
→ Checkout Service
→ Inventory Service
→ Payment Service
→ Order Service

## Payment Dependency

Checkout depends on the Payment Service for payment authorization.

The Checkout Service does not communicate directly with the
external payment provider.

## Payment API

The Payment Service currently supports Payment API v1.

Payment API v2 is being introduced as part of the payment
modernization initiative.

The migration from Payment API v1 to Payment API v2 is described
in ADR-003.

## Retry Behavior

Payment authorization requests currently use a controlled retry policy.

The retry policy exists to handle transient failures.

However, excessive retries can increase request latency and
downstream provider load.

## Failure Handling

If payment authorization cannot be completed within the configured
timeout, checkout should fail safely and should not create an order.

## Impact Consideration

Changes to the following areas may affect checkout:

- Payment API version
- Request/response schema
- Timeout configuration
- Retry configuration
- Payment error handling

## Related Documents

- ARCH-004 Service Dependencies
- ADR-003 Payment API Migration
- INC-1024 Payment Timeout Incident
- RUN-003 Checkout Troubleshooting
- TEST-004 Retry and Payment Load Testing