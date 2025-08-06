# System Admin Guide

This guide is for system administrators managing the PSI Frappe system.

## User Management

- **Create User**: Go to `Users > New`, assign role (DC, SC, Admin)
- **Role Assignment**: Use Role Profile or assign individually
- **Deactivate User**: Uncheck "Enabled" in user record

## Permission Management

- Use Role Permission Manager to fine-tune access:
  - Example: DC can only “Read” Funders, but can “Create/Edit” Activities

## Backups

- Navigate to `Settings > Data > Download Backups`
- Schedule automatic backups via Scheduler

## Email Setup

- Go to `Settings > Email Account`
- Configure SMTP for outgoing notifications

## Custom Fields / Forms

- Use Customize Form to add project-specific fields if needed.
- Avoid modifying core DocTypes directly.

## Data Import

- Use Data Import Tool to bulk upload:
  - Funders, Projects, Users, or Historical Activities
  - Templates available within the tool

## Troubleshooting

- **Error Logs**: Check `Error Logs` and `Scheduler Logs`
- **Clear Cache**: Run `Bench Clear-Cache` or use System Settings
- **Rebuild Index**: For search issues, rebuild global search index via `Settings > Rebuild Search`
