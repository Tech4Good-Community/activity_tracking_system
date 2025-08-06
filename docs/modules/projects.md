# Projects Module

The Projects module allows users to define and manage details about various funded initiatives across different locations.

---

## Fields

| Field | Description |
|-------|-------------|
| **Project Name** | Full name of the project |
| **Project Code** | Unique code (auto-checks for duplication) |
| **Start Date / End Date** | Project duration |
| **Project Status** | Active / Completed / On Hold |
| **Priority** | Low / Medium / High |
| **Project Type** | Based on initiative (e.g., TCI, ATF, etc.) |
| **Department** | Department owning the project |
| **Funder** | Linked to a record in the Funders module |

---

## 📝 User Instructions

### ✅ To Add a New Project:
1. Go to **Projects** > **New**.
2. Enter project details like Name, Code, Dates.
3. Select the **Funder** from the dropdown (must be pre-created).
4. Choose Department, Project Type, and Status.
5. Save and Submit the record.

### 🔍 To Edit a Project:
1. Locate the project using filters or search.
2. Click to view and then select **Edit**.
3. Update relevant fields. Changes may trigger notifications.

---

## ⛓ Dependencies

- Funders must be added before linking them here.
- Projects are used in Activity and Fund Allocation modules.
