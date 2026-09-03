---
document_id: ARCH-002
document_type: architecture
title: ShopSphere Backend Architecture
component: backend
service: backend-platform
status: active
version: 1.0
---

# ShopSphere Backend Architecture

Status: Active

The ShopSphere backend consists of independently deployable services.

## Core Services

- Checkout Service
- Payment Service
- Order Service
- Inventory Service
- Catalog Service
- Notification Service

## API Communication

Services communicate using internal REST APIs.

The Checkout Service is the primary orchestration service
for the customer checkout workflow.

## Reliability

Services use:

- Request timeouts
- Retry policies
- Structured logging
- Circuit-breaker behavior
- Health checks

Retry behavior must be configured carefully because retries
can increase downstream load.

## Payment

Payment processing is handled by the Payment Service.

The Payment Service communicates with an external payment provider.

The Checkout Service must not directly call the payment provider.

## Related Documents

- ARCH-003 Checkout Architecture
- ARCH-004 Service Dependencies
- ADR-003 Payment API Migration
- INC-1024 Payment Timeout Incident