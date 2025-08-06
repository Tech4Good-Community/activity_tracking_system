# Fund Allocation Workflow

The Fund Allocation Workflow manages how project funds are approved and edited before being finalized.

---

## 🔁 Workflow States

1. Pending
2. Requested for Edit
3. Edit Permitted
4. Edit Denied
5. Edit Submitted
6. Finalised
7. No Edits

---

## 👥 State Permissions

| State | Permitted Role |
|-------|----------------|
| Pending | System Manager |
| Requested for Edit | Executive Director |
| Edit Permitted | Executive Director |
| Edit Denied | Executive Director |
| Finalised | Executive Director |
| Edit Submitted | System Manager |
| No Edits | System Manager |

---

## 🔄 Transition Rules

| # | Current State | Action | Next State | Allowed Role |
|---|---------------|--------|------------|--------------|
| 1 | Pending | Request Edit | Requested for Edit | System Manager |
| 2 | Requested for Edit | Permit Edit | Edit Permitted | Executive Director |
| 3 | Requested for Edit | Reject Edit | Edit Denied | Executive Director |
| 4 | Pending | Finalise | Finalised | Executive Director |
| 5 | Edit Permitted | Submit the edit | Edit Submitted | System Manager |
| 6 | Edit Permitted | No edits done | No Edits | System Manager |
| 7 | Edit Submitted | Approve the fund | Finalised | Executive Director |
| 8 | Edit Submitted | Review the edit | Pending | Executive Director |
| 9 | No Edits | Finalise | Finalised | Executive Director |
| 10 | No Edits | Review | Pending | Executive Director |

---

## 📝 Notes

- Edits can only be made if permitted via the workflow.
- “Request to Edit” button should be used to initiate edit flow.
- Only Executive Director can finalize fund allocations.
