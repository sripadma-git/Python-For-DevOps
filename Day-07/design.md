# Day 07 – Design Thinking (Log Analyzer CLI Tool)

## 🧠 What problem am I solving?

- Developers and DevOps engineers work with large log files
- Manually checking logs is time-consuming
- Difficult to quickly identify number of errors or warnings

👉 Problem:
I want to automatically analyze a log file and get a summary of log levels (INFO, WARNING, ERROR)

---

## 📥 What input does my script need?

- Log file path (required)
  Example: app.log

- Optional inputs:
  - Output file path (where result will be saved)
  - Log level filter (INFO / WARNING / ERROR)

👉 User gives:
--file app.log  
--out result.txt (optional)  
--level ERROR (optional)

---

## 📤 What output should my script give?

### Terminal Output:
- Count of logs
Example:
INFO: 2  
WARNING: 1  
ERROR: 3  

### File Output (optional):
- Same summary saved in a file

Example (result.txt):
INFO: 2  
WARNING: 1  
ERROR: 3  

---

## ⚙️ What are the main steps?

1. Take input from user (CLI arguments)
2. Check if log file exists
   - If not → show error

3. Open the log file
4. Read file line by line

5. For each line:
   - Check if it contains:
     - INFO
     - WARNING
     - ERROR
   - Increase count accordingly

6. If user gives --level:
   - Show only that log level

7. Print summary to terminal

8. If output file is given:
   - Write summary into file

---

## 💡 Extra Thinking (DevOps Mindset)

- Handle large files efficiently (line by line reading ✅)
- Avoid crashing if file is missing ✅
- Make tool reusable (CLI arguments ✅)
- Keep output clean and readable ✅

---

## 🎯 Final Understanding

👉 User gives → log file  
👉 Script does → analyze logs  
👉 Script returns → summary  

This is automation replacing manual work.