# LocalLink Backend: Agreed Decisions

Keep this file updated. If a new requirement conflicts with a decision here, discuss it first, then edit this file.

## MVP scope (2-week deadline)
- Auth + Users (email/password; phone/OTP postponed)
- Discovery: public directory of businesses (guest browsing, rate limited)
- ONE full vertical: Salon booking (slots, double-booking prevention, cancellation policy)
- Out of MVP: Courier, merchant staff RBAC, supermarket/restaurant/laundry/cafe flows, escrow, chat, OTP

## Architecture
- Modular monolith: one Django app per business module under `apps/`
- Django + DRF + PostgreSQL (from day one, no SQLite)
- REST API under `/api/v1/`
- Settings split: `base` (safe defaults) / `dev` / `prod`; all secrets via environment (`.env`)
- Local development with venv; Docker Compose for PostgreSQL only
- Dependencies: pip + `requirements/base.txt` / `dev.txt`, exact pinned versions

## Users and Auth
- Custom User model, email is `USERNAME_FIELD` (stored lowercase, unique), `phone` nullable
- `role` field: customer / merchant / admin
- Public registration can only create customer or merchant; admin is never creatable via the API
- UUID primary keys on all domain models (`apps.core.models.BaseModel`)
- JWT for all clients (SimpleJWT): refresh rotation + blacklist
- Secure by default: DRF default permission is `IsAuthenticated`; public endpoints opt in with `AllowAny`
