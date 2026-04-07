# FileSure Assignment – Tech Operations & Support Intern

This project is a solution to the FileSure take-home assignment.
The goal was to ingest messy CSV data, clean it, store it in MongoDB, and expose it through an API with a simple frontend.

---

## 🚀 Tech Stack

* Python (Data ingestion)
* MongoDB Atlas
* Node.js + Express (API)
* HTML, CSS, JavaScript (Frontend)

---

## 📁 Project Structure

```
filesure-assignment/
│
├── ingestion/
│   └── ingest.py
│
├── backend/
│   ├── app.js
│   ├── db.js
│   ├── routes/
│   │   └── companies.js
│   └── package.json
│
├── frontend/
│   └── index.html
│
├── data/
│   └── company_records.csv
│
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the repo

```
git clone https://github.com/Sufalthakre18/filesure-assignment
cd filesure-assignment
```

---

### 2. Setup Environment Variables

Create a `.env` file in root:

```
MONGO_URI=your_mongodb_atlas_connection_string
```

---

### 3. Run Data Ingestion (Python)

```
cd ingestion
pip install pandas pymongo python-dateutil python-dotenv
python ingest.py
```

This will:

* Read CSV file
* Clean and normalize data
* Insert into MongoDB Atlas

---

### 4. Run Backend (Node.js)

```
cd backend
npm install
npm run dev
```

Server will run on:

```
http://localhost:5000
```

---

### 5. Run Frontend

Simply open:

```
frontend/index.html
```

---

## 📡 API Endpoints

### 1. Get Companies (with pagination)

```
GET /companies?page=1&limit=10
```

---

### 2. Filter Companies

```
GET /companies?status=Active&state=Maharashtra
```

---

### 3. Summary (Aggregation)

```
GET /companies/summary
```

Returns count of companies grouped by status.

---

## 🧹 Data Cleaning Approach

* Normalized inconsistent status values (Active, Strike Off, etc.)
* Converted multiple date formats into ISO format
* Cleaned paid-up capital into numeric values
* Handled missing values safely (no crashes)
* Validated emails and flagged invalid ones instead of removing them

---

## ⚡ Optimization

* Added index on `status` and `state` for faster queries
* Used pagination to avoid large data loads
* Used MongoDB aggregation for efficient summary computation

---

## 🎥 Submission Links

* **GitHub Repo:**
  [https://github.com/Sufalthakre18/filesure-assignment](https://github.com/Sufalthakre18/filesure-assignment)

* **Video Walkthrough:**
  [https://drive.google.com/file/d/17BeWGw4BTHV2jWCF7r4zVXvvnQLxqbEP/view?usp=sharing](https://drive.google.com/file/d/17BeWGw4BTHV2jWCF7r4zVXvvnQLxqbEP/view?usp=sharing)

---

## 💡 Notes

* Kept the implementation simple and readable
* Focused on data correctness and handling messy input
* Avoided overengineering while ensuring scalability basics

---
