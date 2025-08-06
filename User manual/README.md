# 📘 PSI System — User Manual

Welcome to the **PSI System**, a platform to manage planning, activity tracking, and fund allocation for development projects across multiple districts.

This guide is your complete reference to understanding how the PSI system works — from user roles to workflow automation, fund management, and reporting.

---
## 1. OVERVIEW

The PSI system enables users to:
- Plan district-wise project activities
- Allocate and track funds
- Monitor activity implementation
- Generate reports for funders and internal use

It supports programmatic workflows, role-based access, and real-time data visibility for stakeholders.

---

## 2. ROLES AND ACCESS

There are three primary user roles:

### 1. District User
- Can fill Planning Sheets for their district.
- Can view activities and track their progress.

### 2. State Reviewer
- Reviews and verifies Planning Sheets from multiple districts.
- Can request changes or approve plans.

### 3. System Admin
- Manages users, permissions, and system setup.
- Has full access to all modules and reports.

---

## 3. MODULES

### A. FUNDERS
- Add funder details (Name, Contact, Type, etc.)
- Link funders to specific projects.

### B. PROJECTS
- Projects are linked to funders.
- Activities and planning sheets are created under projects.

### C. PLANNING SHEET
- The entry point for districts to propose activities.
- Contains fields like Activity Type, Objective, Timeline, Budget, etc.
- Requires State Reviewer approval.

### D. ACTIVITIES
- Auto-generated from approved Planning Sheets.
- Used to track actual implementation progress.
- Includes photos, updates, and completion status.

### E. FUND ALLOCATION
- Admins allocate funds to projects, activities, and districts.
- Can track available vs used funds.

### F. DASHBOARD
- Displays counts and summaries of planning sheets, activities, funds, etc.
- Helps in monitoring key metrics quickly.

### G. REPORTS
- Exportable data for activities, planning sheets, fund allocations, etc.
- Can be filtered by project, district, date, and status.

---

## 4. WORKFLOWS

### A. PLANNING SHEET WORKFLOW
1. Draft → Submitted by District User  
2. Review by State Reviewer  
3. Approved → Activities Created Automatically

### B. ACTIVITY WORKFLOW
1. Auto-created from Planning Sheet  
2. District Users update progress  
3. Marked as Completed by assigned reviewer

### C. FUND ALLOCATION WORKFLOW
1. Admin allocates funds per district/project  
2. Allocation is linked to planning sheet or activity  
3. Funds tracked against usage reports

---

## 5. NOTIFICATIONS

- Email alerts when Planning Sheets are submitted, approved, or rejected.
- Reminders for pending reviews or updates.
- Error alerts for failed fund linkage.

---

## 6. REPORTING VIEWS

- Quick filters for each module.
- Export options to Excel or PDF.
- Useful for funder reporting and internal tracking.

---

## 7. SYSTEM ADMIN INSTRUCTIONS

- Use Role Permissions Manager to configure access.
- Maintain daily backups of the database.
- Use Data Import Tool for bulk uploading projects, funders, or activities.
- Customize dashboards and reports via Report Builder.

---

## 8. BEST PRACTICES

- Ensure all districts submit planning sheets on time.
- Link activities correctly to planning sheets.
- Review fund allocations monthly for discrepancies.
- Update activity progress at least weekly.

---


Built with **role-based access** and **custom workflows**, the platform ensures accountability, transparency, and traceability.

---

## 👤 Roles and Access

Start here to understand how different users interact with the system:
- [Roles and Access](./roles-and-access.md)

---

## 💸 Fund Management

Key modules to handle funders, fund tracking, and fund allocation:
- [Funders](./funders.md) — Add and manage funder organizations
- [Projects](./projects.md) — Create and link projects to funders
- [Funds Allocation](./funds-allocation.md) — Allocate budgets across districts/activities

---

## 🛠️ Program Planning & Implementation

Everything related to activity planning and execution:
- [Planning Sheet](./planning-sheet.md) — Enter planned activities, budgets, and schedules
- [Activities](./activities.md) — View, update, and monitor actual execution
- [Dashboard](./dashboard.md) — Visual overview of key data

---

## 🔁 Workflows

Understand the approval workflows that ensure checks and accountability:
- [Activity Workflow](./activity-workflow.md)
- [Fund Allocation Workflow](./fund-allocation-workflow.md)
- [Planning Sheet Workflow](./workflows/planning-sheet-workflow.md)

Each workflow includes role-wise permissions, stages, and action points.

---

## 📊 Reports & Notifications

Stay updated and make informed decisions:
- [Reports](./reports.md) — Downloadable and interactive reports
- [Reporting Views](./reporting-views.md) — Custom views for easier filtering
- [Notifications](./notifications.md) — System alerts and email updates

---

## ⚙️ System Admin Guide

For developers and system admins maintaining the platform:
- [System Admin Guide](./system-admin.md)

Includes:
- User management
- Backup procedures
- Customization options

---