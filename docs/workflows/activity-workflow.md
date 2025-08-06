# Activity Workflow

The Activity Workflow manages the approval process for each activity from creation to finalization. It includes multiple departments depending on the nature of the activity.

---

## 🔁 Workflow States

1. Submit from City Manager
2. Approval from State Manager
3. Approval from Deputy Director
4. Approval from HR Department
5. Approval from Procurement Department
6. Finalised

---

## 👥 State Permissions

| State | Permitted Role |
|-------|----------------|
| Submit from City Manager | City Manager |
| Approval from State Manager | State Manager |
| Approval from Deputy Director | Deputy Director |
| Approval from HR Department | HR Department Head |
| Approval from Procurement Department | Procurement Department Head |
| Finalised | HR or Procurement Head (depending on activity) |

---

## 🔄 Transition Rules

| # | Current State | Action | Next State | Allowed Role |
|---|---------------|--------|------------|--------------|
| 1 | Submit from City Manager | Submit | Approval from State Manager | City Manager |
| 2 | Approval from State Manager | Approve | Approval from Deputy Director | State Manager |
| 3 | Approval from State Manager | Make Changes | Submit from City Manager | State Manager |
| 4 | Approval from Deputy Director | Approve for HR Dept | Approval from HR Department | Deputy Director |
| 5 | Approval from Deputy Director | Approve for Procurement Dept | Approval from Procurement Department | Deputy Director |
| 6 | Approval from Deputy Director | Make Changes | Approval from State Manager | Deputy Director |
| 7 | Approval from HR Department | Approve | Finalised | HR Department Head |
| 8 | Approval from Procurement Department | Approve | Finalised | Procurement Head |
| 9 | Approval from HR Department | Make Changes | Approval from Deputy Director | HR Department Head |
| 10 | Approval from Procurement Department | Make Changes | Approval from Deputy Director | Procurement Head |

---

## 📝 Notes

- Only one path (HR or Procurement) is followed depending on the activity type.
- Status automatically updates based on transitions.
- Notifications are triggered on every state change.
