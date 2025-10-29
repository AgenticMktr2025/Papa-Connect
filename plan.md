# Papa Connect - Live Data Implementation Plan 🚀

## Current Status
✅ Complete MVP with 8 pages and full database integration
🎯 **CURRENT PHASE**: Phase 10 Complete - Ready for Phase 11

---

## Phase 9: Database Setup & Authentication System ✅
**Goal**: Implement real database backend and proper authentication

- [x] Install required dependencies (sqlalchemy, alembic, bcrypt, python-jose, passlib, psycopg2-binary)
- [x] Create database models (app/models/db_models.py) matching existing Reflex models
- [x] Set up SQLAlchemy engine and session management (app/database.py)
- [x] Implement authentication system (app/auth.py):
  - Password hashing with bcrypt
  - JWT token generation and validation
  - Session management utilities
- [x] Test database connection and auth flow
- [x] Wire up authentication to AppState
- [x] Update splash page with demo mode toggle

**Status**: Complete. All database infrastructure working correctly.

---

## Phase 10: User Profile & Connection CRUD Operations ✅
**Goal**: Replace dummy data with real database operations for users and connections

- [x] Update AppState with live data integration:
  - Add demo_mode flag and toggle (already present)
  - Load user data from database when demo_mode=False
  - Keep dummy data when demo_mode=True
  - Implement login/register event handlers
- [x] Update splash page (login_page.py):
  - Demo mode toggle switch (already functional)
  - Wire up real authentication
  - Show demo mode indicator when active
  - Handle login errors properly
- [x] Implement Connection database operations:
  - Create connection (manual add, QR scan, NFC simulation)
  - Read connections list with filters
  - Update connection (tier, state, notes, ratings)
  - Store connections in database when not in demo mode
  - Query connections on app load
- [x] Implement connection state transitions (active_72h → engaged when event created)
- [x] Test all CRUD operations with real data
- [x] Verify demo mode still works with in-memory data

**Testing Results:**
- ✅ User login with JWT authentication working
- ✅ Add contact stores in database
- ✅ Create event stores in database and updates connection state
- ✅ Demo mode preserves in-memory dummy data
- ✅ All event handlers tested and working

**Status**: Complete. App now supports both demo mode and live database operations.

---

## Phase 11: Event Management & Calendar Integration
**Goal**: Store events in database and integrate real calendar APIs

- [ ] Implement Event database operations:
  - Create event with validation ✅ (already done)
  - Read events (upcoming, past, filtered by connection) ✅ (already done)
  - Update event details
  - Delete/cancel event
- [ ] Add Google Calendar API integration:
  - OAuth token storage in database
  - Fetch user's free/busy data
  - Create calendar events on confirmation
  - Sync event updates/deletions
- [ ] Build smart scheduling algorithm:
  - Parse both users' availability
  - Suggest 2-3 optimal time slots
  - Handle timezone differences
- [ ] Implement event notifications:
  - 24h before reminder
  - Post-event follow-up prompt
- [ ] Update stats tracking on event creation
- [ ] Test calendar sync and event persistence

---

## Phase 12: Smart Behavioral Logic & Background Tasks
**Goal**: Implement automated timers, state transitions, and notifications

- [ ] Create background task system:
  - Check 72h activation windows every hour
  - Detect 30-day dormant connections daily
  - Run monthly tier rebalancing review
  - Send notifications for state changes
- [ ] Implement timer management:
  - Store timer start dates in database
  - Calculate remaining time dynamically
  - Freeze/resume timers on pause/breathing space
- [ ] Build notification system:
  - Email notifications (SMTP integration)
  - Push notifications (placeholder for mobile)
  - In-app notification center
- [ ] Add notification preferences:
  - Store in database per user
  - Honor do-not-disturb settings
  - Respect breathing space state
- [ ] Implement connection revival detection:
  - Track dormant → active transitions
  - Update stats counter
  - Show celebration message
- [ ] Test all automated workflows

---

## Phase 13: Analytics & Stats Calculation from Real Data
**Goal**: Calculate all stats from database queries, not hardcoded values

- [ ] Implement stats calculation queries:
  - Active connections (state != paused/dormant)
  - Total exchanges (sum of all connections)
  - Events coordinated (count from events table)
  - Longest relationship (max days since first event)
  - Revived connections (count state transitions)
  - Engagement rate (active events in last 30 days / total connections)
- [ ] Build aggregation queries for charts:
  - Connection tier breakdown (group by tier)
  - Monthly event counts (group by month, last 6 months)
  - Top connections by event count (order by count)
- [ ] Add caching layer:
  - Cache expensive stats queries (1 hour TTL)
  - Invalidate cache on data changes
- [ ] Implement data export:
  - Generate JSON export from database
  - Include all user data (profile, connections, events, ratings)
- [ ] Test analytics accuracy with various data scenarios

---

## Phase 14: Demo Mode Polish & Registration Flow
**Goal**: Perfect the demo/live mode experience

- [ ] Build registration flow:
  - Create new user account
  - Hash password properly
  - Generate JWT token
  - Redirect to onboarding
- [ ] Improve demo mode UI:
  - Add banner: "Demo Mode - Data not saved"
  - Show toggle indicator clearly
  - Add "Create Account" CTA in demo mode
- [ ] Implement data migration:
  - Option to "Save demo data to your account" after registration
  - Copy demo connections/events to database
- [ ] Add demo mode restrictions UI:
  - Show why certain features are disabled
  - Encourage registration for full features
- [ ] Test mode switching:
  - Demo → Live (after registration)
  - Live → Demo (logout)
  - Data isolation verification

---

## Phase 15: Security, Error Handling & Production Readiness
**Goal**: Harden the app for production deployment

- [ ] Implement security best practices:
  - SQL injection prevention (parameterized queries) ✅ (SQLAlchemy ORM)
  - XSS protection (input sanitization)
  - CSRF protection (tokens)
  - Rate limiting on auth endpoints
  - Secure password requirements
- [ ] Add comprehensive error handling:
  - Database connection failures (retry logic)
  - API call failures (graceful degradation)
  - Invalid user input (validation messages)
  - Network errors (offline mode)
- [ ] Build logging system:
  - Log all database operations
  - Track API calls and errors
  - Monitor background task execution
- [ ] Add data backup system:
  - Automated daily backups
  - Export/import functionality ✅ (export_user_data implemented)
- [ ] Implement privacy features:
  - GDPR-compliant data export ✅ (already implemented)
  - Right to deletion (cascade) ✅ (implemented in unsubscribe flow)
  - Data retention policies
- [ ] Performance optimization:
  - Database indexing on foreign keys
  - Query optimization (N+1 problem)
  - Lazy loading for large lists
- [ ] Test production deployment:
  - Environment variable configuration
  - Database migrations on deployment
  - SSL/TLS for API calls

---

## Technical Notes
- **Database**: PostgreSQL for production, SQLite for local development (default: sqlite:///reflex.db)
- **Authentication**: JWT tokens with 30-minute expiry, bcrypt password hashing
- **Files Created**: 
  - app/database.py (SQLAlchemy setup)
  - app/auth.py (Authentication utilities)
  - app/models/db_models.py (Database models)
- **Environment Variables**: 
  - DATABASE_URL (optional, defaults to SQLite)
  - SECRET_KEY (optional, has secure default)
- **Demo Mode**: Fully functional with in-memory dummy data, toggle on splash screen
- **Database Models Fixed**: Removed incorrect User.events relationship, proper one-to-many through connections

## Next Steps
Phase 11 will add Google Calendar integration and smart scheduling features. The foundation is now complete with working database, authentication, and demo mode!
