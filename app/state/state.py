import reflex as rx
from app.models.models import UserProfile, Connection, Event, UserStats, Suggestion
import datetime
import asyncio


class AppState(rx.State):
    user: UserProfile = UserProfile(
        id=1,
        name="Alex",
        email="alex@papaconnect.com",
        phone="+1 (555) 123-4567",
        status="active",
        avatar_seed="Alex",
    )
    connections: list[Connection] = [
        Connection(
            id=1,
            peer_name="Tom Riley",
            tier=3,
            state="engaged",
            last_event_date="2024-07-20",
            avatar_url="https://api.dicebear.com/9.x/notionists/svg?seed=Tom",
        ),
        Connection(
            id=2,
            peer_name="Raj Patel",
            tier=2,
            state="active_72h",
            last_event_date="N/A",
            avatar_url="https://api.dicebear.com/9.x/notionists/svg?seed=Raj",
        ),
        Connection(
            id=3,
            peer_name="Ben Carter",
            tier=2,
            state="dormant",
            last_event_date="2024-05-15",
            avatar_url="https://api.dicebear.com/9.x/notionists/svg?seed=Ben",
        ),
        Connection(
            id=4,
            peer_name="Sam Chen",
            tier=1,
            state="paused",
            last_event_date="2024-06-30",
            avatar_url="https://api.dicebear.com/9.x/notionists/svg?seed=Sam",
            mutual_connection_ids=[1, 2],
        ),
        Connection(
            id=5,
            peer_name="Mike Lee",
            tier=2,
            state="active_72h",
            last_event_date="N/A",
            avatar_url="https://api.dicebear.com/9.x/notionists/svg?seed=Mike",
            mutual_connection_ids=[3],
        ),
        Connection(
            id=6,
            peer_name="David Kim",
            tier=2,
            state="engaged",
            last_event_date="2024-07-22",
            avatar_url="https://api.dicebear.com/9.x/notionists/svg?seed=David",
            mutual_connection_ids=[1],
        ),
    ]
    events: list[Event] = [
        Event(
            id=1,
            title="Park Hangout",
            date="2025-10-30",
            time="10:00 AM",
            location="Greenleaf Park",
            connection_id=1,
        ),
        Event(
            id=2,
            title="Coffee & Crawlers",
            date="2025-11-05",
            time="9:00 AM",
            location="The Daily Grind",
            connection_id=2,
        ),
    ]
    stats: UserStats = UserStats(
        active_connections=6,
        total_exchanges=12,
        events_coordinated=28,
        longest_relationship_days=342,
        revived_connections=2,
    )
    suggestions: list[Suggestion] = []
    group_event_opportunities: list[dict] = []
    nav_items: list[dict[str, str]] = [
        {"label": "Home", "icon": "layout-dashboard", "path": "/home"},
        {"label": "Add Contact", "icon": "user-plus", "path": "/add-contact"},
        {"label": "Event Planner", "icon": "calendar-plus", "path": "/event-planner"},
        {"label": "My Events", "icon": "calendar", "path": "/my-events"},
        {
            "label": "Breathing Space",
            "icon": "pause-circle",
            "path": "/breathing-space",
        },
        {"label": "Analytics", "icon": "bar-chart-2", "path": "/analytics"},
        {"label": "Settings", "icon": "settings", "path": "/settings"},
    ]
    faqs: list[dict[str, str]] = [
        {
            "question": "What is Breathing Space?",
            "answer": "Breathing Space is a feature that allows you to pause all notifications and connection timers. Your data is preserved, and you can resume anytime.",
        },
        {
            "question": "How do I add a new contact?",
            "answer": "You can add a new contact by navigating to the 'Add Contact' page. You can either scan their QR code, use the NFC tap simulation, or enter their details manually.",
        },
        {
            "question": "How are my analytics calculated?",
            "answer": "Analytics are based on your activity within the app. 'Total Exchanges' tracks events and significant interactions, while 'Engagement Rate' measures how many of your connections you've interacted with recently.",
        },
        {
            "question": "Is my data private?",
            "answer": "Yes, your privacy is a priority. Your data is not shared, and features like the selfie avatar generation process images locally on your device without storing them.",
        },
    ]
    onboarding_step: int = 1
    contact_added_success: bool = False
    selected_connection_id_planner: int | None = None
    event_created_success: bool = False
    suggested_time_slots: list[dict[str, str]] = [
        {"date": "Saturday, Aug 3", "time": "10:00 AM", "duration": "2 hours"},
        {"date": "Saturday, Aug 3", "time": "2:00 PM", "duration": "1.5 hours"},
        {"date": "Sunday, Aug 4", "time": "11:00 AM", "duration": "2 hours"},
    ]
    event_filter_connection: str = "all"
    breathing_duration: str = ""
    notification_message: str = ""
    notification_visible: bool = False
    email_notifications_enabled: bool = True
    push_notifications_enabled: bool = True
    smart_suggestions_enabled: bool = False
    show_delete_confirmation: bool = False
    unsubscribe_step: int = 1
    qr_code_url: str = ""
    is_scanning_qr: bool = False
    is_loaded: bool = False
    is_authenticated: bool = False
    token: str = ""
    selfie_features: dict[str, str] = {}
    capture_selfie_mode: bool = False
    is_processing_selfie: bool = False
    selfie_avatar_preview_url: str = ""
    avatar_edit_mode: bool = False
    dropdown_open: bool = False
    faq_open_state: dict[str, bool] = {}
    show_signup: bool = False
    login_error: str = ""
    demo_mode: bool = False
    splash_video_urls: list[str] = [
        "https://drive.google.com/uc?export=download&id=12ch8dyOirz5hSQtyNPFMkoPdWcTsYVqM",
        "https://drive.google.com/uc?export=download&id=1nRXbJILsiv5PQGd79f-de2t-weFM5eWz",
        "https://drive.google.com/uc?export=download&id=1evMoZSTes6PczLgomG24xJUxfCjYPif1",
        "https://drive.google.com/uc?export=download&id=1GkQQGB_r66Yf_bZol0W8GbTFS3-TMU4k",
        "https://drive.google.com/uc?export=download&id=1wUWwbTGqY7s0HMxEmzieDC3gmWVGPEwy",
    ]
    current_video_index: int = 0
    mobile_sidebar_open: bool = False

    @rx.var
    def current_video_url(self) -> str:
        if self.splash_video_urls:
            import random

            return random.choice(self.splash_video_urls)
        return ""

    def _load_faqs(self):
        if not self.faq_open_state:
            self.faq_open_state = {str(i): False for i, _ in enumerate(self.faqs)}

    @rx.event
    async def on_load(self):
        """Check auth and load data."""
        import reflex_clerk_api as clerk
        from app.database import get_db, init_db
        from app.models.db_models import (
            User,
            Connection as DBConnection,
            Event as DBEvent,
        )

        init_db()
        clerk_user_state = await self.get_state(clerk.ClerkState)
        if not clerk_user_state.user_id:
            self.is_authenticated = False
            self.is_loaded = True
            self._load_faqs()
            return
        user_id = clerk_user_state.user_id
        self.is_authenticated = True
        with get_db() as db:
            db_user = db.query(User).filter(User.id == user_id).first()
            if db_user:
                self.user = UserProfile(
                    id=db_user.id,
                    name=db_user.name,
                    email=db_user.email,
                    phone=db_user.phone,
                    status=db_user.status.value,
                    avatar_seed=db_user.avatar_seed or db_user.name,
                )
                db_connections = (
                    db.query(DBConnection)
                    .filter(DBConnection.owner_id == user_id)
                    .all()
                )
                self.connections = [
                    Connection(
                        id=c.id,
                        peer_name=c.peer_name,
                        email=c.email,
                        tier=c.tier,
                        state=c.state.value,
                        last_event_date=c.last_event_date or "N/A",
                        avatar_url=c.avatar_url,
                    )
                    for c in db_connections
                ]
                db_events = (
                    db.query(DBEvent)
                    .join(DBConnection)
                    .filter(DBConnection.owner_id == user_id)
                    .all()
                )
                self.events = [
                    Event(
                        id=e.id,
                        title=e.title,
                        date=e.date,
                        time=e.time,
                        location=e.location,
                        connection_id=e.connection_id,
                    )
                    for e in db_events
                ]
        self.is_loaded = True
        self._load_faqs()
        if self.router.page.path == "/":
            return rx.redirect("/home")

    @rx.event
    def toggle_mobile_sidebar(self):
        self.mobile_sidebar_open = not self.mobile_sidebar_open

    @rx.event
    async def login(self, form_data: dict):
        """Login the user."""
        self.login_error = "Login is handled by Clerk."

    @rx.event
    def toggle_signup(self):
        self.show_signup = not self.show_signup
        self.login_error = ""

    @rx.event
    def toggle_demo_mode(self):
        self.demo_mode = not self.demo_mode
        if self.demo_mode:
            return rx.redirect("/home")

    @rx.event
    def toggle_faq(self, index: int):
        self._load_faqs()
        key = str(index)
        self.faq_open_state[key] = not self.faq_open_state.get(key, False)

    @rx.event
    def toggle_dropdown(self):
        self.dropdown_open = not self.dropdown_open

    @rx.event
    def logout(self):
        return clerk.sign_out()

    @rx.event
    def update_profile(self, form_data: dict):
        self.user.name = form_data.get("name", self.user.name)
        self.user.phone = form_data.get("phone", self.user.phone)
        self.show_notification("Profile updated successfully!")

    @rx.event
    def toggle_email_notifications(self):
        self.email_notifications_enabled = not self.email_notifications_enabled

    @rx.event
    def toggle_push_notifications(self):
        self.push_notifications_enabled = not self.push_notifications_enabled

    @rx.event
    def toggle_smart_suggestions(self):
        self.smart_suggestions_enabled = not self.smart_suggestions_enabled

    @rx.event
    def export_user_data(self):
        user_data = {
            "user": self.user.dict(),
            "connections": [c.dict() for c in self.connections],
            "events": [e.dict() for e in self.events],
        }
        print("User data exported:", user_data)
        self.show_notification("Your data export is ready!")
        return rx.download(data=str(user_data), filename="papa_connect_data.json")

    @rx.event
    def initiate_account_deletion(self):
        self.show_delete_confirmation = True
        self.unsubscribe_step = 1

    @rx.event
    async def unsubscribe_account(self):
        self.unsubscribe_step = 2
        yield
        import asyncio

        await asyncio.sleep(2)
        self.unsubscribe_step = 3
        print("Account unsubscribed.")

    @rx.event
    def toggle_breathing_space(self):
        if self.user.status == "active":
            self.user.status = "breathing"
            self.show_notification("Breathing Space activated. Timers paused.")
        else:
            self.user.status = "active"
            self.show_notification("Welcome back! Timers resumed.")

    @rx.event
    def set_breathing_duration(self, duration: str):
        self.breathing_duration = duration

    @rx.event
    def show_notification(self, message: str):
        self.notification_message = message
        self.notification_visible = True

    @rx.event
    def dismiss_notification(self):
        self.notification_visible = False
        self.notification_message = ""

    @rx.event
    def check_72h_activation(self):
        return "Reminder: Follow up with new connection Tom within 72 hours."

    @rx.event
    def check_30d_dormancy(self):
        return "Tidy-up: Ben has been dormant for 30 days. Consider reaching out."

    @rx.event
    def suggest_tier_rebalancing(self):
        return "Monthly Review: You have 6 Tier 3 connections. Consider re-evaluating."

    @rx.event
    def next_step(self):
        if self.onboarding_step < 4:
            self.onboarding_step += 1

    @rx.event
    def prev_step(self):
        if self.onboarding_step > 1:
            self.onboarding_step -= 1

    @rx.event
    def set_onboarding_step(self, step: int):
        self.onboarding_step = step

    @rx.event
    def toggle_capture_selfie_mode(self, mode: bool | None = None):
        if mode is None:
            self.capture_selfie_mode = not self.capture_selfie_mode
        else:
            self.capture_selfie_mode = mode
        if not self.capture_selfie_mode:
            self.is_processing_selfie = False
            self.selfie_features = {}
            self.selfie_avatar_preview_url = ""

    @rx.event
    async def process_selfie(self):
        import random
        import asyncio

        self.is_processing_selfie = True
        self.selfie_features = {}
        yield
        await asyncio.sleep(2)
        hair_colors = ["brown", "black", "blonde", "red", "gray"]
        eye_colors = ["blue", "green", "brown", "hazel"]
        beards = ["yes", "no", "stubble"]
        glasses_options = ["yes", "no"]
        features = {
            "hair": random.choice(hair_colors),
            "eyes": random.choice(eye_colors),
            "beard": random.choice(beards),
            "glasses": random.choice(glasses_options),
        }
        self.selfie_features = features
        seed_parts = [self.user.name.lower()] + [
            f"{k}_{v}" for k, v in features.items()
        ]
        seed = "_".join(seed_parts)
        self.selfie_avatar_preview_url = (
            f"https://api.dicebear.com/9.x/notionists/svg?seed={seed}"
        )
        self.is_processing_selfie = False

    @rx.event
    def confirm_avatar(self):
        self.user.avatar_seed = self.selfie_avatar_preview_url.split("seed=")[-1]
        if self.avatar_edit_mode:
            self.avatar_edit_mode = False
            self.show_notification("Avatar updated successfully!")
        self.toggle_capture_selfie_mode(False)

    @rx.event
    def dismiss_suggestion(self, suggestion_id: int):
        self.suggestions = [s for s in self.suggestions if s.id != suggestion_id]

    @rx.event
    def detect_group_opportunities(self):
        """Analyzes connection graph to find group event opportunities."""
        import itertools

        opportunities = []
        active_connections = [
            c for c in self.connections if c.state in ["engaged", "active_72h"]
        ]
        conn_map = {c.id: c for c in self.connections}
        for combo in itertools.combinations(active_connections, 3):
            c1, c2, c3 = combo
            if (
                c2.id not in conn_map[c1.id].mutual_connection_ids
                and c3.id not in conn_map[c1.id].mutual_connection_ids
                and (c1.id not in conn_map[c2.id].mutual_connection_ids)
                and (c3.id not in conn_map[c2.id].mutual_connection_ids)
                and (c1.id not in conn_map[c3.id].mutual_connection_ids)
                and (c2.id not in conn_map[c3.id].mutual_connection_ids)
            ):
                score = (c1.tier + c2.tier + c3.tier) / 3
                opportunities.append(
                    {
                        "ids": [c1.id, c2.id, c3.id],
                        "names": [c1.peer_name, c2.peer_name, c3.peer_name],
                        "score": score,
                    }
                )
        self.group_event_opportunities = sorted(
            opportunities, key=lambda x: x["score"], reverse=True
        )[:3]
        self._generate_dynamic_suggestions()

    @rx.event
    def toggle_avatar_edit_mode(self, mode: bool | None = None):
        if mode is None:
            self.avatar_edit_mode = not self.avatar_edit_mode
        else:
            self.avatar_edit_mode = mode
        if not self.avatar_edit_mode:
            self.toggle_capture_selfie_mode(False)

    def _generate_dynamic_suggestions(self):
        """Generates a list of dynamic suggestions based on current state."""
        new_suggestions = []
        suggestion_id = 1
        for opp in self.group_event_opportunities:
            new_suggestions.append(
                Suggestion(
                    id=suggestion_id,
                    icon="users",
                    title="Group Hangout Opportunity",
                    description=f"{opp['names'][0]}, {opp['names'][1]}, and {opp['names'][2]} haven't met. Great for a group BBQ!",
                    type="group",
                    involved_connections=opp["ids"],
                )
            )
            suggestion_id += 1
        dormant_conns = [c for c in self.connections if c.state == "dormant"][:2]
        for conn in dormant_conns:
            new_suggestions.append(
                Suggestion(
                    id=suggestion_id,
                    icon="zap",
                    title=f"Reconnect with {conn.peer_name}",
                    description="It's been a while. A quick message could restart the timer.",
                    type="individual",
                    involved_connections=[conn.id],
                )
            )
            suggestion_id += 1
        self.suggestions = new_suggestions

    @rx.event
    def generate_qr_code(self):
        import qrcode
        import base64
        from io import BytesIO

        user_data = f"papaconnect://add?name={self.user.name}&email={self.user.email}"
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(user_data)
        qr.make(fit=True)
        img = qr.make_image(fill="black", back_color="white")
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
        self.qr_code_url = f"data:image/png;base64,{img_str}"

    @rx.event
    def toggle_qr_scanner(self):
        self.is_scanning_qr = not self.is_scanning_qr

    @rx.event
    async def simulate_nfc_tap(self):
        """Simulates an NFC tap, creates a new contact, and shows success."""
        import random
        import asyncio

        dad_names = ["Mike D.", "Steve R.", "Gary L.", "Jason B."]
        name = random.choice(dad_names)
        email = f"{name.lower().replace(' ', '.').replace('.', '')}@example.com"
        new_connection = Connection(
            id=len(self.connections) + 1,
            peer_name=name,
            email=email,
            tier=1,
            state="active_72h",
            last_event_date="N/A",
            avatar_url=f"https://api.dicebear.com/9.x/notionists/svg?seed={name}",
        )
        self.connections.append(new_connection)
        self.show_notification(f"Contact Added via NFC: {name}")
        self.contact_added_success = True
        yield
        await asyncio.sleep(2)
        self.contact_added_success = False
        yield rx.redirect("/home")

    @rx.event
    async def on_qr_scan(self, contact_data: dict):
        """Simulates scanning a QR code and adds the contact."""
        self.is_scanning_qr = False
        seed = contact_data.get("email") or contact_data["name"]
        new_connection = Connection(
            id=len(self.connections) + 1,
            peer_name=contact_data["name"],
            email=contact_data.get("email"),
            tier=1,
            state="active_72h",
            last_event_date="N/A",
            avatar_url=f"https://api.dicebear.com/9.x/notionists/svg?seed={seed}",
        )
        self.connections.append(new_connection)
        self.show_notification(f"Contact Added: {contact_data['name']}")
        self.contact_added_success = True
        yield
        import asyncio

        await asyncio.sleep(2)
        self.contact_added_success = False

    @rx.event
    def select_connection_for_planner(self, connection_id: str):
        self.selected_connection_id_planner = int(connection_id)

    @rx.event
    async def create_event(self, form_data: dict):
        new_event = Event(
            id=len(self.events) + 1,
            title=form_data["title"],
            date=form_data["date"],
            time=form_data["time"],
            location=form_data["location"],
            connection_id=self.selected_connection_id_planner,
        )
        self.events.append(new_event)
        for i, conn in enumerate(self.connections):
            if conn.id == self.selected_connection_id_planner:
                self.connections[i].state = "engaged"
                self.connections[i].last_event_date = form_data["date"]
                break
        self.stats.events_coordinated += 1
        self.event_created_success = True
        yield
        import asyncio

        await asyncio.sleep(3)
        self.event_created_success = False
        self.selected_connection_id_planner = None

    @rx.event
    async def add_contact(self, form_data: dict):
        """Placeholder for adding a new contact"""
        seed = form_data.get("email") or form_data["name"]
        new_connection = Connection(
            id=len(self.connections) + 1,
            peer_name=form_data["name"],
            email=form_data.get("email"),
            tier=1,
            state="active_72h",
            last_event_date="N/A",
            avatar_url=f"https://api.dicebear.com/9.x/notionists/svg?seed={seed}",
        )
        self.connections.append(new_connection)
        print("Adding contact:", new_connection)
        self.contact_added_success = True
        yield
        import asyncio

        await asyncio.sleep(2)
        self.contact_added_success = False

    @rx.event
    def set_event_filter_connection(self, connection_id: str):
        self.event_filter_connection = connection_id

    @rx.var
    def current_date(self) -> str:
        return datetime.date.today().strftime("%A, %B %d")

    @rx.var
    def upcoming_events(self) -> list[Event]:
        today = datetime.date.today()
        future_events = [
            e
            for e in self.events
            if datetime.datetime.strptime(e.date, "%Y-%m-%d").date() >= today
        ]
        return sorted(future_events, key=lambda e: (e.date, e.time))

    @rx.var
    def next_event(self) -> Event | None:
        if self.upcoming_events:
            return self.upcoming_events[0]
        return None

    @rx.var
    def next_event_iso_datetime(self) -> str:
        if self.next_event:
            try:
                dt_obj = datetime.datetime.strptime(
                    f"{self.next_event.date} {self.next_event.time}",
                    "%Y-%m-%d %I:%M %p",
                )
                return dt_obj.isoformat()
            except (ValueError, TypeError) as e:
                import logging

                logging.exception(f"Error parsing next event datetime: {e}")
                return ""
        return ""

    @rx.var
    def past_events(self) -> list[Event]:
        today = datetime.date.today()
        past_events = [
            e
            for e in self.events
            if datetime.datetime.strptime(e.date, "%Y-%m-%d").date() < today
        ]
        return sorted(past_events, key=lambda e: e.date, reverse=True)

    @rx.var
    def filtered_upcoming_events(self) -> list[Event]:
        if self.event_filter_connection == "all":
            return self.upcoming_events
        return [
            e
            for e in self.upcoming_events
            if str(e.connection_id) == self.event_filter_connection
        ]

    @rx.var
    def filtered_past_events(self) -> list[Event]:
        if self.event_filter_connection == "all":
            return self.past_events
        return [
            e
            for e in self.past_events
            if str(e.connection_id) == self.event_filter_connection
        ]

    @rx.var
    def get_connection_name_by_id(self) -> dict[int, str]:
        return {conn.id: conn.peer_name for conn in self.connections}

    @rx.var
    def get_connection_by_id(self) -> dict[int, Connection]:
        return {conn.id: conn for conn in self.connections}

    @rx.var
    def get_events_for_connection(self) -> list[Event]:
        connection_id_str = self.router.page.params.get("id", "")
        if not connection_id_str:
            return []
        try:
            connection_id = int(connection_id_str)
            return [
                event for event in self.events if event.connection_id == connection_id
            ]
        except (ValueError, TypeError) as e:
            import logging

            logging.exception(f"Error getting events for connection: {e}")
            return []

    @rx.var
    def current_connection(self) -> Connection | None:
        connection_id_str = self.router.page.params.get("id", "")
        if not connection_id_str:
            return None
        try:
            connection_id = int(connection_id_str)
            return self.get_connection_by_id.get(connection_id)
        except (ValueError, TypeError) as e:
            import logging

            logging.exception(f"Error getting current connection: {e}")
            return None

    @rx.var
    def connection_tier_breakdown(self) -> list[dict[str, int | str]]:
        from collections import Counter

        tier_counts = Counter((c.tier for c in self.connections))
        return [
            {"tier": f"Tier {tier}", "count": count, "fill": fill}
            for tier, count, fill in [
                (3, tier_counts[3], "#4f46e5"),
                (2, tier_counts[2], "#6366f1"),
                (1, tier_counts[1], "#818cf8"),
            ]
        ]

    @rx.var
    def monthly_event_counts(self) -> list[dict[str, int | str]]:
        from collections import defaultdict
        import datetime

        counts = defaultdict(int)
        today = datetime.date.today()
        for event in self.events:
            event_date = datetime.datetime.strptime(event.date, "%Y-%m-%d").date()
            if event_date > today - datetime.timedelta(days=180):
                month_key = event_date.strftime("%b")
                counts[month_key] += 1
        months = []
        for i in range(6):
            month = (today - datetime.timedelta(days=30 * i)).strftime("%b")
            months.append(month)
        months.reverse()
        return [{"month": month, "events": counts.get(month, 0)} for month in months]

    @rx.var
    def top_connections_by_events(self) -> list[dict[str, str | int]]:
        from collections import Counter

        event_counts = Counter((event.connection_id for event in self.events))
        top_five = sorted(
            [
                {
                    "id": conn.id,
                    "name": conn.peer_name,
                    "event_count": event_counts.get(conn.id, 0),
                }
                for conn in self.connections
            ],
            key=lambda x: x["event_count"],
            reverse=True,
        )[:5]
        return [{**conn, "rank": i + 1} for i, conn in enumerate(top_five)]

    @rx.var
    def engagement_rate(self) -> int:
        import datetime

        thirty_days_ago = datetime.date.today() - datetime.timedelta(days=30)
        engaged_ids = set()
        for e in self.events:
            event_date = datetime.datetime.strptime(e.date, "%Y-%m-%d").date()
            if event_date >= thirty_days_ago:
                engaged_ids.add(e.connection_id)
        engaged_connections_count = len(engaged_ids)
        total_connections = len(self.connections)
        if total_connections == 0:
            return 0
        return round(engaged_connections_count / total_connections * 100)

    @rx.var
    def user_avatar_url(self) -> str:
        return (
            f"https://api.dicebear.com/9.x/notionists/svg?seed={self.user.avatar_seed}"
        )