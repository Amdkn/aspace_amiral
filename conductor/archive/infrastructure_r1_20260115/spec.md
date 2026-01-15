# Specification: Infrastructure R1 Gatekeeper

## Overview
Deploy a persistent "Gatekeeper" layer (R1) using Docker to host n8n (Orchestration) and Supabase (Sovereign Memory). This infrastructure will serve as the bridge between local operations (R0) and cloud delivery (R2/R3), enabling autonomous data synchronization and persistent state management.

## User Stories
- As the Amiral, I want my OS state and KPIs stored in a sovereign database (Supabase) so that the system's memory persists independently of my local machine.
- As the Manager (Antigravity), I want n8n to automatically sync local "Pulses" to the global database so that I have a real-time, persistent view of business health.
- As the system, I want R1 to be accessible only via private network (VPN) and backed up regularly to ensure security and anti-fragility.

## Functional Requirements
- **Containerization:** Deploy n8n and Supabase (PostgreSQL, GoTrue, PostgREST) using Docker Compose.
- **Sovereign Memory:** Initialize a Supabase schema to store project statuses and global KPIs.
- **Pulse Synchronization:** Implement an n8n workflow that receives pulse data (from R0) and updates the Supabase database.
- **Connectivity:** Configure the environment for access via a private VPN/Tunnel (Tailscale).
- **Anti-Fragility:** Implement a backup script for Supabase database exports and n8n workflow JSONs.

## Non-Functional Requirements
- **Security:** No public port exposure; access restricted to the private network.
- **Reliability:** Automated restart policies for all Docker containers.
- **Documentation:** Clear map of container ports and volume mappings in R1.

## Acceptance Criteria
- [ ] Docker Compose successfully launches n8n and Supabase services.
- [ ] Supabase is reachable from R0 via the private network.
- [ ] An n8n workflow successfully writes a "Test Pulse" into a Supabase table.
- [ ] A backup of the Supabase schema can be generated and verified.

## Out of Scope
- Integration with external webhooks (GitHub/Stripe) - *Reserved for future tracks*.
- Deployment of a public-facing Reverse Proxy (HTTPS).
