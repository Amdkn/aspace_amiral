# Implementation Plan: Infrastructure R1 Gatekeeper

## Phase 1: Docker Environment & Core Services
- [x] Task: Initialize R1 Directory Structure 008f4f4
    - [x] Create `01_PROJECTS/infrastructure_r1` directory
    - [x] Setup subdirectories for Supabase and n8n persistent volumes
- [ ] Task: Draft Docker Compose Configuration
    - [ ] Define Supabase services (db, kong, auth, rest)
    - [ ] Define n8n service with persistent volume
    - [ ] Set up private networking between containers
- [ ] Task: TDD - Verify Container Orchestration
    - [ ] Write a script to verify service health (healthcheck)
    - [ ] Launch services and ensure all containers reach "healthy" status
- [ ] Task: Conductor - User Manual Verification 'Phase 1: Docker Environment' (Protocol in workflow.md) [checkpoint: ]

## Phase 2: Sovereign Memory (Supabase) Setup
- [ ] Task: Database Schema Initialization
    - [ ] Define tables for `pulses` and `system_state`
    - [ ] Create SQL migration script
- [ ] Task: TDD - Verify Schema and Connectivity
    - [ ] Write a Python test script using `psycopg2` or `supabase-py`
    - [ ] Verify R0 can connect to Supabase via the private network
    - [ ] Verify CRUD operations on the `pulses` table
- [ ] Task: Conductor - User Manual Verification 'Phase 2: Sovereign Memory' (Protocol in workflow.md) [checkpoint: ]

## Phase 3: Autonomous Workflow (n8n) Integration
- [ ] Task: n8n Configuration & Pulse Workflow
    - [ ] Setup n8n initial credentials via CLI or config
    - [ ] Create the "Pulse Forwarding" workflow (Webhook -> Supabase Insert)
- [ ] Task: TDD - End-to-End Pulse Sync
    - [ ] Write a test script in R0 that sends a mock pulse to the n8n webhook
    - [ ] Verify the pulse is correctly recorded in the Supabase database
- [ ] Task: Implement Backup Script
    - [ ] Create a shell/python script for database and workflow exports
    - [ ] Verify backup integrity
- [ ] Task: Conductor - User Manual Verification 'Phase 3: Integration' (Protocol in workflow.md) [checkpoint: ]
