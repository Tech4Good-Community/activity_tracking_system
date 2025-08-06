# Funds Allocation Module

The Funds Allocation module allows budgeting for a project and tracks planned vs. actual usage across categories.

---

## Fields

| Field | Description |
|-------|-------------|
| **Project Name** | Auto-linked |
| **Project Start / End Date** | From project record |
| **Date of Planning** | Date of allocation entry |
| **Total Funds** | Total fund value for the project |

### 💰 Utilisation Categories (with Allocation & %)

- Salary
- Travel
- Activity
- Consultant
- Equipment
- Research
- Indirect

Each has:
- Funds Allocated
- Percentage of Allocation

| Field | Description |
|-------|-------------|
| **Grand Total** | Sum of all allocated funds |
| **Status** | Pending / Finalised etc. (Workflow-driven) |

---

## 📝 User Instructions

### ✅ To Add a Fund Allocation:
1. Go to **Funds Allocation** > **New**.
2. Select the **Project Name**.
3. Fill in planned budgets for each category.
4. Ensure total % = 100%.
5. Submit the form to trigger the fund allocation workflow.

### 🌀 Workflow:
- Pending
- Request Edit
- Edit Permitted
- Finalised
- Edit Submitted
- Edit Denied
- No Edits

### 📌 Edit Workflow:
- System Manager and Executive Director control transitions.
- Only permitted edits can be made.

---

## 🛠 Tips

- Use the “Request to Edit” button to initiate workflow for updates.
- Always review fund distribution percentages before finalising.
- Edits are tracked and must be submitted via workflow approval.
