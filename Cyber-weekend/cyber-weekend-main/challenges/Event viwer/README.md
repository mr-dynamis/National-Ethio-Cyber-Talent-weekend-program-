# 🔍 Windows Event Viewer – PowerShell Attack Analysis

## 📌 Overview

This project analyzes a **PowerShell-based attack** using Windows Event Viewer logs. It focuses on identifying attack execution, process details, and group activity through forensic investigation.

---

## ✅ Q1. Event ID for PowerShell Downgrade Attack

**Answer:** `400`

**Explanation:**
Event ID **400** logs the start of the PowerShell engine. If the engine version shows `2.0`, it indicates a **downgrade attack**, often used to bypass security controls.

---

## ✅ Q2. Date & Time of Attack

**Answer:** *(From Event ID 400 or earliest 4104 event)*

**Explanation:**
The timestamp shows when the attack occurred. Found in:

* `TimeCreated`
* Logged time field

**Format:**

```
MM/DD/YYYY H:MM:SS AM/PM
```

---

## ✅ Q3. Log Clear Event – Event Record ID

**Answer:** *(From Event ID 104 in this lab)*

**Explanation:**

* Normally: Event ID **1102** = Security log cleared
* In this case: Event ID **104** was used
* The required value is the **EventRecordID** (unique identifier of the event)

---

## ✅ Q4. Computer Name

**Answer:** `WIN-1O0UJBNP9G7`

**Explanation:**
Found in:

```xml
<Computer>WIN-1O0UJBNP9G7</Computer>
```

---

## ✅ Q5. First Variable in PowerShell Command

**Answer:** `$__PSUsingVariable_TargetComputers`

**Explanation:**
From ScriptBlock:

```powershell
WFTraceAddWorkflowExit -TargetComputers $__PSUsingVariable_TargetComputers
```

* Variables start with `$`
* First variable is selected
* Parameters (like `-TargetComputers`) are ignored

---

## ✅ Q6. Date & Time of Attack (Execution)

**Answer:** *(Earliest Event ID 4104 timestamp)*

**Explanation:**
Event ID **4104** logs actual PowerShell execution.

* Choose the **earliest event**
* Represents the start of the attack

---

## ✅ Q7. Execution Process ID

**Answer:** `400`

**Explanation:**
From:

```xml
<Execution ProcessID="400" ThreadID="5756" />
```

* **ProcessID** = PowerShell process executing the attack
* **ThreadID** is not required

---

## ✅ Q8. Group Security ID (SID)

**Answer:**

```
S-1-5-21-1881654409-284601696-3713096779-513
```

**Explanation:**
From:

```xml
<Data Name="TargetSid">...</Data>
```

* Identifies the **group involved** in the activity

---

## ✅ Q9. Event ID (Group Activity)

**Answer:** `4728`

**Explanation:**
Event ID **4728** indicates:

> A member was added to a **security-enabled global group**

* Matches the group-related action in the logs
* Contains TargetSid and user information

---

## 🧠 Key Takeaways

* **400 → PowerShell engine start (downgrade detection)**
* **4104 → Attack execution (ScriptBlock logging)**
* **401 / 1102 → Log clearing events**
* **4728 → Group activity (enumeration/addition)**
* **ProcessID → Tracks execution process**
* **SID → Identifies users/groups uniquely**

---




