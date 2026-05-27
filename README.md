
:

🔑 Core Features

Super Admin ControlOne dashboard for managing all users, cameras, and storage policies.

Cloud StorageCustomers get 50% of the storage quota, but the system stores video in high resolution even if the customer streams in normal resolution.→ This means you’ll need dual-stream encoding: one lower-res stream for live viewing, one high-res stream for archival.

Playback & Live StreamingCustomers can watch live feeds or replay past events. Playback should be optimized with indexed video chunks for fast retrieval.

AI Incident DetectionIf a customer asks “আজকের ঘটনা বের করো” (show today’s incidents), the AI scans stored footage for anomalies (motion detection, unusual activity, etc.) and returns relevant clips.→ This requires metadata tagging during recording (time, location, detected events).

⚙️ Suggested Architecture

Frontend (Web + Android App)

Built with React/Vue for web, Kotlin/Flutter for Android.

Unified UI for live view, playback, billing, and support.

Backend Services

Auth Service → Role-based access (user, reseller, super admin).

Video Service → Handles dual-stream encoding, storage, and retrieval.

AI Service → Event detection, anomaly tagging, incident search.

Billing Service → Tracks storage usage, customer plans, payments.

Storage Layer

Cloud object storage (e.g., S3-compatible) with lifecycle policies.

Metadata DB (PostgreSQL/TimescaleDB) for indexing video events.

AI Workflow

Real-time detection (motion, intrusion, fire, etc.).

On-demand queries (“show today’s incidents”) → AI searches metadata + video chunks.

Optional image summarization for quick previews.

📊 Example Flow

Customer streams CCTV → sees normal resolution.

System stores high resolution copy in cloud.

AI tags events (motion, faces, anomalies).

Customer asks for playback → gets indexed clips.

Customer asks AI for “আজকের ঘটনা” → AI returns relevant clips + summary images.

Would you like me to sketch a deployment guide (Docker Compose + microservices) for this all-in-one system, or a feature workflow diagram showing how storage, playback, and AI interact?

I can focus on deployment, workflow diagram, or AI integration.

# ISP CLOUD SYSTEM

## INSTALL

chmod +x deploy.sh

./deploy.sh

## API

http://SERVER-IP:8000
