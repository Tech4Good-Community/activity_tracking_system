# Planning Sheet Workflow

The Planning Sheet Workflow ensures that all project activity plans go through the necessary approval channels before implementation. It is crucial for aligning funder requirements, internal strategy, and state-specific plans.

---

## 🔁 Workflow States

1. Draft
2. Submitted by Project Team
3. Approved by State Manager
4. Finalised

---

## 👥 State Permissions

| State | Permitted Role |
|-------|----------------|
| Draft | Project Coordinator |
| Submitted by Project Team | Project Coordinator |
| Approved by State Manager | State Manager |
| Finalised | Project Director |

---

## 🔄 Transition Rules

| # | Current State | Action | Next State | Allowed Role |
|---|---------------|--------|------------|--------------|
| 1 | Draft | Submit | Submitted by Project Team | Project Coordinator |
| 2 | Submitted by Project Team | Approve | Approved by State Manager | State Manager |
| 3 | Submitted by Project Team | Send Back | Draft | State Manager |
| 4 | Approved by State Manager | Finalise | Finalised | Project Director |
| 5 | Approved by State Manager | Send Back | Submitted by Project Team | Project Director |

---

## 📝 Notes

- A planning sheet can only be edited while in `Draft` or if sent back by the State Manager.
- Once finalised, the sheet becomes read-only and is used for tracking and reporting.
- Notifications are triggered at each transition.
