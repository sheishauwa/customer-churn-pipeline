# Customer Churn Prediction & Retention Pipeline

## 📌 Project Overview
This project implements an **end-to-end customer churn prediction pipeline** for a telecom company using the IBM Telco Customer Churn dataset. It covers:

- Infrastructure provisioning with **Terraform**
- Configuration automation with **Ansible**
- ETL and data processing with **AWS Glue & PySpark**
- Data storage and partitioning with **S3**
- CI/CD deployment with **GitHub Actions**
- Real-time job monitoring using **CloudWatch**
- IAM-based access management
- ML model for churn prediction with ML-ready output

---

## 🧬 Dataset Path in S3
```
s3://telco-churn-data-hauwa/
├── raw/
│   └── WA_Fn-UseC_-Telco-Customer-Churn.csv
├── processed/
│   └── *.parquet
└── ml-ready/
    ├── Churn=Yes/
    └── Churn=No/
```

---

## ⚙️ Technologies Used
- **AWS S3** - Data lake for raw, processed, and ML-ready data
- **AWS Glue** - ETL pipeline for cleaning, transforming, partitioning
- **Terraform** - Infrastructure provisioning
- **Ansible** - Post-deploy automation
- **GitHub Actions** - CI/CD automation for IaC deployments
- **CloudWatch** - Monitoring Glue job runs
- **IAM** - Secure access management
- **PySpark** - Spark data processing
- **Python** - ML prediction script

---

## 🔁 ETL Workflow
1. Upload raw CSV to `s3://telco-churn-data-hauwa/raw/`
2. Run Glue ETL job:
   - Cleans & drops nulls
   - Converts to Parquet
   - Saves to `processed/`
3. ML-ready transformation:
   - Partitioned into `Churn=Yes/No` folders
   - Output stored in `ml-ready/`

---

## 📸 Screenshots & Architecture

### `Architectur`
- 📌 Description: End-to-end architecture of the pipeline
![Architecture Diagram](images/architecture.png)


### `etl-flow.png`
- 📌 Description: ETL steps from raw to ML-ready
- 📷 Location: `docs/images/etl-flow.png`
- 🛠 How to: Draw raw ➜ processed ➜ ml-ready flow

### `s3-output.png`
- 📌 Description: Screenshot of S3 folders with ML-ready churn partitions
![ML-ready Screenshort](images/ml_image.png)

```

---

## ✅ Deployment Steps
1. **Upload Dataset** to S3 `raw/`
2. **Terraform Apply** to provision infra
3. **Ansible Playbook** (if needed) to configure resources
4. **Run GitHub Actions CI/CD** to trigger Glue Job
5. **Verify in Glue Job Run & S3 Output**
6. **Run ML Script** for churn prediction on processed data

---

## 📩 Author
**Hauwa Kulu Njidda**
- 📧 hauwa.dbtech@gmail.com
- 🔗 [LinkedIn](https://www.linkedin.com/in/hauwa-kulu-njidda)

---
