# Dashboard1_dataIngestionService
# Influencer Management & Analytics Platform — Data Ingestion Service

## Overview

The **Influencer Management & Analytics Platform** is designed to connect **creators (influencers)** and **brands** while providing analytics, collaboration tools, and AI-powered insights.  

The **Data Ingestion Service** is a critical component of the platform. Its main purpose is to **collect, process, and store influencer and brand data from multiple sources**, such as social media platforms (Instagram, TikTok, YouTube), and make it available for analytics, reporting, and recommendations.

---

## Data Ingestion Service Overview

This service is responsible for:

1. **Connecting to External APIs**
   - Fetches real-time data from social media platforms via **connected accounts**.
   - Supports multiple platforms per influencer.
   - Handles API authentication tokens securely (stored in the database).

2. **Processing & Normalization**
   - Cleans and formats incoming data into a standardized structure.
   - Aggregates metrics like followers, engagement, and reach.
   - Computes derived values like average engagement and growth trends.

3. **Database Storage**
   - Writes processed data into **Supabase PostgreSQL**.
   - Works in tandem with the **Backend Service** to update:
     - `InfluencerDetails`
     - `ConnectedAccounts`
     - Analytics tables (future)
   - Ensures relational integrity and avoids duplicate entries.

4. **Scheduling & Automation**
   - Runs at configurable intervals (e.g., hourly, daily) to keep influencer data fresh.
   - Can be extended to support real-time streaming updates from APIs in the future.

5. **Error Handling & Logging**
   - Handles API rate limits, failures, and retries.
   - Logs ingestion events and errors for monitoring and debugging.

---

## Tech Stack

- **Backend / Worker:** Node.js  
- **Database:** Supabase PostgreSQL  
- **ORM:** Prisma  
- **Authentication:** OAuth2 / API Tokens for external platforms  
- **Scheduling:** Cron jobs or task queues (e.g., Bull or Agenda for future scalability)  
- **Environment Management:** dotenv  

---



