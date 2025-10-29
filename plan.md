# Papa Connect - Full-Stack Dad Coordination App 🎉

## Current Goal
Build a complete MVP with 8 core pages, smart behavioral logic, and a compassionate user experience.

---

## Phase 1: Core Navigation, Data Models & Home Dashboard ✅
**Goal**: Set up app structure, state management, data models, and implement the home dashboard with upcoming events and active connections.

- [x] Define complete data models (UserProfile, Connection, Event, UserStats) using rx.Base
- [x] Create AppState with all state variables and dummy data for connections, events, and stats
- [x] Implement navigation sidebar with links to all 8 pages
- [x] Build Home Dashboard with:
  - Welcome header with user name and status indicator
  - Upcoming events section (cards showing title, date, time, location)
  - Top connections leaderboard (showing top 5 by event count with rankings)
  - Smart suggestions section for meet-up recommendations
  - Quick action buttons (Add Contact, Plan Event, View Analytics)
- [x] Apply Material Design 3 styling with indigo primary color, gray secondary, Poppins font
- [x] Test all event handlers for navigation and state updates

---

## Phase 2: Onboarding, Dad Card & Connection Management ✅
**Goal**: Build onboarding flow, profile creation, contact detail pages, and connection management features.

- [x] Create Onboarding page with:
  - Google OAuth placeholder (mock sign-in button with success state)
  - Calendar link integration placeholder (mock connection UI)
  - Dad Card creation form (name, location, kids' ages, interests, availability checkboxes)
  - Multi-step wizard with progress indicator
- [x] Build Add Contact page with:
  - QR code display placeholder (generated from user ID)
  - NFC simulation button
  - Manual add form (name, phone, tier selection)
  - Success animation and redirect to connection detail
- [x] Implement Connection Detail page with:
  - Header showing peer name, tier stars, and state badge
  - Shared interests tag cloud
  - Meet-up history timeline (dates, locations, notes)
  - Private Michelin-style rating system (⭐1-3 / 🏆 buttons)
  - Edit tier and notes functionality
  - Action buttons (Plan Event, Send Message WhatsApp deep-link)
- [x] Add connection state management event handlers (activate, pause, delete)
- [x] Test all forms, validation, and state transitions

---

## Phase 3: Event Planner & Calendar Integration ✅
**Goal**: Build intelligent event planning system with calendar conflict detection and sync.

- [x] Create Event Planner page with:
  - Connection selector (dropdown or search)
  - Calendar availability viewer (weekly grid showing free/busy blocks)
  - Smart suggestion algorithm (2-3 proposed time slots based on both calendars)
  - Time slot selection cards with date, time, duration
  - Location input with suggestions (park, cafe, playground)
  - Event notes field
  - Confirm and sync button
- [x] Implement event creation logic:
  - Add event to both users' calendars (placeholder sync)
  - Update connection state to "engaged"
  - Create WhatsApp deep-link message with event details
  - Success notification with calendar preview
- [x] Build My Events page showing:
  - Upcoming events list (sorted by date)
  - Past events archive
  - Filter by connection
  - Event detail modal with edit/cancel options
- [x] Add 72-hour activation timer logic (mock timer countdown)
- [x] Test event creation, calendar conflict detection, and state transitions

---

## Phase 4: Pause/Breathing Space & Behavioral Logic ✅
**Goal**: Implement pause states, timer management, and connection lifecycle automation.

- [x] Create Pause/Breathing Space page with:
  - Current status indicator (Active / Paused / Breathing Space)
  - Visual representation of paused timers
  - Duration selector for breathing space (1 week, 2 weeks, 1 month, indefinite)
  - Explanation of what gets paused (notifications, timers, prompts)
  - Resume button with countdown display
  - "What's preserved" section (connections, history, ratings)
- [x] Implement pause/resume event handlers:
  - Toggle user status (active → paused → breathing)
  - Freeze all connection timers
  - Stop dormancy checks and tidy-up prompts
  - Update UI state across all pages
- [x] Build automated behavioral logic:
  - New connection → 72h activation window
  - Event booked → state changes to "engaged"
  - No event after 72h → auto-pause with notification
  - 30-day dormancy detection → tidy-up prompt
  - Monthly tier rebalancing check (⭐⭐⭐ max 5, ⭐⭐ max 20)
- [x] Add notification system (in-app banners for prompts)
- [x] Test all pause states and automated transitions

---

## Phase 5: Analytics Dashboard & Stats Tracking ✅
**Goal**: Build comprehensive analytics showing relationship metrics and quiet wins.

- [x] Create Analytics page with:
  - Hero stats cards (active connections, total exchanges, events coordinated)
  - Longest relationship badge with days counter
  - Revived connections counter
  - Connection tier breakdown (pie chart or bar graph)
  - Monthly activity trend (line chart showing events over time)
  - Top 5 connections leaderboard (by event count)
  - Engagement rate calculation and display
- [x] Implement stats calculation logic:
  - Track all metrics in UserStats model
  - Update counters on key events (new connection, event created, revival)
  - Calculate longest relationship from first event date
  - Detect revived connections (dormant → active)
- [x] Add data visualization:
  - Use rx.recharts for charts (pie, bar, line)
  - Animate stat counters on page load
  - Export stats as image/PDF button (placeholder)
- [x] Build "Quiet Wins" motivational messaging system
- [x] Test all stat calculations and chart rendering

---

## Phase 6: Unsubscribe Flow & Data Management ✅
**Goal**: Create thoughtful offboarding experience and data export/deletion features.

- [x] Build Unsubscribe Flow page with:
  - "Before you go" hero message with empathy
  - Full stats showcase (all analytics in summary view)
  - Testimonials or benefits reminder
  - Alternative option: "Try Breathing Space instead" prominent CTA
  - Final confirmation modal ("Are you sure?")
  - Data export button (download JSON/CSV of connections and events)
  - Permanent delete button with multi-step confirmation
- [x] Create Settings page:
  - Profile management (edit Dad Card details)
  - Notification preferences (email, push, frequency) with toggle switches
  - Privacy settings (profile visibility)
  - Data export/download button
  - Account deletion link
- [x] Implement data export functionality:
  - Generate JSON with all user data
  - Export connections and events data
  - Show success notification
- [x] Add account deletion logic:
  - Multi-step confirmation flow
  - Breathing Space alternative recommendation
  - Processing animation (2-second delay)
  - Final confirmation screen
- [x] Test unsubscribe flow and breathing space redirect

---

## Phase 7: Smart Group Matching Algorithm ✅
**Goal**: Implement intelligent connection graph analysis to recommend group events.

- [x] Extend Connection model with `mutual_connection_ids` field to track who knows whom
- [x] Build `detect_group_opportunities()` algorithm that:
  - Analyzes connection graph to find sets of 3 connections with no mutual links
  - Filters for active/engaged connections (not paused/dormant)
  - Calculates compatibility score based on tier levels
  - Returns top 3 group opportunities sorted by score
- [x] Implement dynamic suggestion generation:
  - Replace hardcoded suggestions with algorithm-generated recommendations
  - Create "Group Hangout Opportunity" cards showing all 3 names
  - Add "Reconnect with [dormant connection]" individual suggestions
  - Include dismissible suggestion cards with reasoning text
- [x] Add group event visualization:
  - Display 3 avatars side-by-side for group suggestions
  - Show icon for individual suggestions
  - Include dismiss button functionality
- [x] Test algorithm with various connection graphs

---

## Phase 8: Onboarding Selfie Avatar Generation (Option 3 Compromise) ✅
**Goal**: Add selfie capture during onboarding with feature extraction to customize DiceBear avatar seeds.

- [x] Add selfie capture UI to onboarding Dad Card step:
  - Camera access button (HTML5 getUserMedia API wrapper)
  - Live camera preview with capture button
  - "Skip" option to use name-based seed instead
  - Privacy notice: "Photo processed locally, never stored"
- [x] Implement client-side feature extraction simulation:
  - Mock detection of hair color, eye color, beard presence, glasses
  - Generate custom DiceBear seed from extracted features
  - Example seed format: `{name}_hair_{color}_eyes_{color}_beard_{yes/no}`
- [x] Update AppState with:
  - `selfie_features: dict` to store extracted characteristics
  - `avatar_seed: str` computed variable based on features or name
  - Event handler `process_selfie(features: dict)` to generate custom seed
- [x] Integrate with existing avatar display:
  - Update all avatar URLs to use `AppState.avatar_seed`
  - Ensure consistency across dashboard, sidebar, connection cards
- [x] Add visual feedback:
  - Processing animation during "feature extraction"
  - Preview of generated avatar before confirming
  - Success message: "Avatar created from your photo!"
- [x] Test onboarding flow:
  - With selfie capture → custom seed avatar
  - With skip → name-based seed avatar (existing behavior)
  - Verify no photo data stored in state or backend

---

## ✅ ALL PHASES COMPLETE!

The Papa Connect MVP is now fully implemented with all 8 core pages, smart behavioral logic, compassionate UX, and privacy-first selfie avatar generation!

---

## Notes
- Use SQLite for local data storage (placeholder setup)
- Mock Google OAuth flow with success/failure states
- WhatsApp integration via deep-link (whatsapp://send?phone=...)
- All calendar operations are placeholder (no real Google Calendar API yet)
- Material Design 3 with indigo primary, gray secondary, Poppins font
- Responsive design for web, mobile-ready
- Copy tone: calming, supportive, minimal ("Keep your energy where it counts")
- **Selfie avatar generation uses simulated feature extraction (no real ML/CV)**
- **Original photo never leaves client, never stored on server**
- **Custom seeds create more personalized avatars while maintaining privacy**
