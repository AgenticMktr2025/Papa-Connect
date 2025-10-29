import reflex as rx
from app.state.state import AppState
from app.models.models import Event, Connection, Suggestion


def status_indicator(status: rx.Var[str]) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            class_name=rx.match(
                status,
                ("active", "h-2 w-2 rounded-full bg-green-500"),
                ("paused", "h-2 w-2 rounded-full bg-amber-500"),
                ("breathing", "h-2 w-2 rounded-full bg-sky-500"),
                "h-2 w-2 rounded-full bg-gray-400",
            )
        ),
        rx.el.span(status.to_string().capitalize(), class_name="text-sm font-medium"),
        class_name="flex items-center gap-2 px-3 py-1 rounded-full text-gray-700 bg-white border border-gray-200 w-fit shadow-sm",
    )


def user_menu_dropdown() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.foreach(
                AppState.nav_items,
                lambda item: rx.el.a(
                    rx.icon(item["icon"], class_name="h-4 w-4 mr-3 text-slate-500"),
                    item["label"],
                    href=item["path"],
                    class_name="flex items-center px-3 py-2 text-sm font-medium text-slate-700 rounded-md hover:bg-slate-100",
                ),
            ),
            class_name="flex flex-col gap-1 p-2",
        ),
        rx.el.div(class_name="border-t border-slate-200 my-2"),
        rx.el.div(
            rx.el.a(
                rx.icon("life-buoy", class_name="h-4 w-4 mr-3 text-slate-500"),
                "Help & Support",
                href="/help-support",
                class_name="flex items-center px-3 py-2 text-sm font-medium text-slate-700 rounded-md hover:bg-slate-100",
            ),
            class_name="p-2",
        ),
        rx.el.div(class_name="border-t border-slate-200 my-2"),
        rx.el.div(
            rx.el.a(
                rx.icon("log-out", class_name="h-4 w-4 mr-3 text-red-500"),
                "Logout",
                on_click=AppState.logout,
                class_name="flex items-center px-3 py-2 text-sm font-medium text-red-600 rounded-md hover:bg-red-50 cursor-pointer",
            ),
            class_name="p-2",
        ),
        class_name="absolute right-0 mt-2 w-64 bg-white rounded-xl shadow-2xl border z-50",
    )


def dashboard_header() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h1(
                f"Welcome back, {AppState.user.name}!",
                class_name="text-3xl font-bold text-slate-900",
            ),
            rx.el.p(AppState.current_date, class_name="text-slate-500 font-semibold"),
            class_name="hidden md:block",
        ),
        rx.el.div(
            rx.el.button(
                rx.el.image(
                    src=AppState.user_avatar_url,
                    class_name="h-12 w-12 rounded-full border-2 border-white shadow-md",
                ),
                on_click=AppState.toggle_dropdown,
            ),
            rx.cond(AppState.dropdown_open, user_menu_dropdown(), None),
            class_name="relative",
        ),
        class_name="flex items-center justify-between",
    )


def quick_actions() -> rx.Component:
    actions = [
        {"icon": "user-plus", "label": "Add Contact", "path": "/add-contact"},
        {"icon": "calendar-plus", "label": "Plan Event", "path": "/event-planner"},
        {"icon": "bar-chart-2", "label": "View Analytics", "path": "/analytics"},
    ]
    return rx.el.div(
        rx.foreach(
            actions,
            lambda action: rx.el.a(
                rx.icon(action["icon"], class_name="h-5 w-5"),
                action["label"],
                href=action["path"],
                class_name="flex items-center justify-center gap-2 font-semibold text-white px-4 py-3 rounded-md hover:shadow-lg transition-all shadow-md bg-orange-600 hover:bg-orange-700",
            ),
        ),
        class_name="grid grid-cols-1 sm:grid-cols-3 gap-4",
    )


def upcoming_event_card(event: Event) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.icon("calendar", class_name="h-5 w-5 text-orange-600"),
                class_name="p-3 bg-orange-100 rounded-md",
            ),
            rx.el.div(
                rx.el.h3(event.title, class_name="font-semibold text-slate-800"),
                rx.el.p(
                    f"with {AppState.get_connection_name_by_id.get(event.connection_id, 'a friend')}",
                    class_name="text-sm text-slate-500",
                ),
            ),
            class_name="flex items-center gap-4",
        ),
        rx.el.div(
            rx.el.div(
                rx.icon("clock", class_name="h-4 w-4 text-slate-500 mr-2"),
                rx.el.p(
                    f"{event.date} at {event.time}",
                    class_name="text-sm text-slate-600 font-medium",
                ),
                class_name="flex items-center",
            ),
            rx.el.div(
                rx.icon("map-pin", class_name="h-4 w-4 text-slate-500 mr-2"),
                rx.el.p(
                    event.location, class_name="text-sm text-slate-600 font-medium"
                ),
                class_name="flex items-center",
            ),
            class_name="mt-4 flex flex-col sm:flex-row sm:items-center sm:justify-between gap-2 sm:gap-4 text-sm",
        ),
        class_name="p-5 bg-white border border-slate-200 rounded-lg shadow hover:shadow-lg hover:-translate-y-1 transition-all",
    )


def connection_state_badge(state: rx.Var[str]) -> rx.Component:
    return rx.el.div(
        state.to_string().replace("_", " ").capitalize(),
        class_name=rx.match(
            state,
            (
                "engaged",
                "px-2 py-1 text-xs font-semibold text-teal-800 bg-teal-100 rounded-full",
            ),
            (
                "active_72h",
                "px-2 py-1 text-xs font-semibold text-sky-800 bg-sky-100 rounded-full",
            ),
            (
                "paused",
                "px-2 py-1 text-xs font-semibold text-orange-800 bg-orange-100 rounded-full",
            ),
            (
                "dormant",
                "px-2 py-1 text-xs font-semibold text-slate-800 bg-slate-200 rounded-full",
            ),
            "px-2 py-1 text-xs font-semibold text-slate-700 bg-slate-200 rounded-full",
        ),
    )


def top_connection_card(connection: dict) -> rx.Component:
    return rx.el.a(
        rx.el.div(
            rx.el.div(
                f"#{connection['rank']}",
                class_name="text-lg font-bold text-slate-400 w-8 text-center",
            ),
            rx.el.image(
                src=f"https://api.dicebear.com/9.x/notionists/svg?seed={connection['name']}",
                class_name="h-12 w-12 rounded-full",
            ),
            rx.el.div(
                rx.el.h4(connection["name"], class_name="font-semibold text-slate-800"),
                rx.el.p(
                    f"{connection['event_count']} events",
                    class_name="text-sm text-slate-500",
                ),
                class_name="flex-1",
            ),
            rx.icon("chevron-right", class_name="h-5 w-5 text-slate-400"),
            class_name="flex items-center gap-4",
        ),
        href=f"/connections/{connection['id']}",
        class_name="p-4 bg-white border border-slate-200 rounded-lg shadow-sm hover:shadow-md transition-all",
    )


def group_suggestion_avatars(connection_ids: rx.Var[list[int]]) -> rx.Component:
    return rx.el.div(
        rx.foreach(
            connection_ids,
            lambda conn_id: rx.el.image(
                src=f"https://api.dicebear.com/9.x/notionists/svg?seed={AppState.get_connection_by_id[conn_id].peer_name}",
                class_name="h-8 w-8 rounded-full border-2 border-white -ml-2 first:ml-0",
            ),
        ),
        class_name="flex items-center",
    )


def suggestion_card(suggestion: Suggestion) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.cond(
                suggestion.type == "group",
                group_suggestion_avatars(suggestion.involved_connections),
                rx.icon(suggestion.icon, class_name="h-6 w-6 text-orange-600"),
            ),
            rx.el.div(
                rx.el.h4(suggestion.title, class_name="font-semibold text-slate-800"),
                rx.el.p(suggestion.description, class_name="text-sm text-slate-500"),
                class_name="flex-1",
            ),
            rx.el.div(
                rx.el.button(
                    rx.icon("arrow-right", class_name="h-4 w-4"),
                    class_name="bg-slate-100 hover:bg-slate-200 text-slate-600 p-2 rounded-full",
                ),
                rx.el.button(
                    rx.icon("x", class_name="h-4 w-4"),
                    on_click=lambda: AppState.dismiss_suggestion(suggestion.id),
                    class_name="bg-slate-100 hover:bg-slate-200 text-slate-600 p-2 rounded-full",
                ),
                class_name="flex flex-col gap-2",
            ),
            class_name="flex items-start gap-4",
        ),
        class_name="p-4 bg-white border border-slate-200 rounded-lg shadow-sm",
    )


def notification_banner() -> rx.Component:
    return rx.cond(
        AppState.notification_visible,
        rx.el.div(
            rx.el.p(AppState.notification_message, class_name="font-semibold"),
            rx.el.button(
                rx.icon("x", class_name="h-5 w-5"),
                on_click=AppState.dismiss_notification,
                class_name="p-1 rounded-full hover:bg-white/20",
            ),
            class_name="fixed top-0 left-0 right-0 bg-slate-800 text-white p-3 flex justify-between items-center shadow-md z-50 animate-in fade-in slide-in-from-top duration-300",
        ),
        None,
    )


def next_event_widget() -> rx.Component:
    return rx.cond(
        AppState.next_event,
        rx.el.div(
            rx.el.h2("Next Event", class_name="text-2xl font-bold text-slate-900 mb-4"),
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        class_name="text-4xl font-bold text-orange-600 animate-pulse"
                    ),
                    rx.moment(
                        AppState.next_event_iso_datetime,
                        from_now=True,
                        class_name="text-4xl font-bold text-orange-600 animate-pulse",
                    ),
                    rx.el.p(
                        "until your next hang out",
                        class_name="text-sm text-slate-500 font-medium",
                    ),
                    class_name="text-center",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.h3(
                            AppState.next_event.title,
                            class_name="font-semibold text-slate-800",
                        ),
                        rx.el.p(
                            f"with {AppState.get_connection_name_by_id.get(AppState.next_event.connection_id, 'a friend')}",
                            class_name="text-sm text-slate-500",
                        ),
                        class_name="flex-1",
                    ),
                    rx.el.div(
                        rx.icon("calendar-check", class_name="h-5 w-5 text-orange-600"),
                        class_name="p-3 bg-orange-100 rounded-md",
                    ),
                    class_name="flex items-center justify-between mt-6",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.icon("clock", class_name="h-4 w-4 text-slate-500 mr-2"),
                        rx.el.p(
                            f"{AppState.next_event.date} at {AppState.next_event.time}",
                            class_name="text-sm text-slate-600 font-medium",
                        ),
                        class_name="flex items-center",
                    ),
                    rx.el.div(
                        rx.icon("map-pin", class_name="h-4 w-4 text-slate-500 mr-2"),
                        rx.el.p(
                            AppState.next_event.location,
                            class_name="text-sm text-slate-600 font-medium",
                        ),
                        class_name="flex items-center",
                    ),
                    class_name="mt-4 flex items-center justify-between text-sm",
                ),
                class_name="p-5 bg-white border border-slate-200 rounded-lg shadow-sm h-full flex flex-col justify-between",
            ),
        ),
        rx.el.div(
            rx.el.h2("Next Event", class_name="text-2xl font-bold text-slate-900 mb-4"),
            rx.el.div(
                rx.icon("calendar-plus", class_name="h-10 w-10 text-slate-400"),
                rx.el.p(
                    "No upcoming events.",
                    class_name="text-slate-500 font-semibold mt-2",
                ),
                rx.el.a(
                    "Plan one now",
                    href="/event-planner",
                    class_name="mt-4 text-sm font-semibold text-orange-600 hover:underline",
                ),
                class_name="flex flex-col items-center justify-center p-8 bg-white border-2 border-dashed border-slate-200 rounded-lg h-full text-center",
            ),
        ),
    )


def dashboard_page() -> rx.Component:
    return rx.el.main(
        notification_banner(),
        rx.el.div(
            dashboard_header(),
            rx.el.div(class_name="my-8 border-t border-slate-200"),
            quick_actions(),
            rx.el.div(
                rx.el.div(
                    next_event_widget(),
                    rx.el.div(
                        rx.el.h2(
                            "Top Connections",
                            class_name="text-2xl font-bold text-slate-900 mb-4",
                        ),
                        rx.cond(
                            AppState.top_connections_by_events.length() > 0,
                            rx.el.div(
                                rx.foreach(
                                    AppState.top_connections_by_events,
                                    top_connection_card,
                                ),
                                class_name="flex flex-col gap-4",
                            ),
                            rx.el.div(
                                rx.icon(
                                    "users",
                                    class_name="h-8 w-8 text-slate-400 mx-auto mb-2",
                                ),
                                rx.el.p(
                                    "No connections yet.",
                                    class_name="text-center text-slate-500",
                                ),
                                rx.el.a(
                                    "Add your first contact",
                                    href="/add-contact",
                                    class_name="mt-2 text-sm font-semibold text-orange-600 hover:underline",
                                ),
                                class_name="text-center flex flex-col items-center p-8 bg-slate-100/50 rounded-lg border border-dashed",
                            ),
                        ),
                    ),
                    class_name="lg:col-start-3 lg:col-end-4 row-start-1 row-end-3 space-y-8",
                ),
                rx.el.div(
                    rx.el.h2(
                        "Upcoming Events",
                        class_name="text-2xl font-bold text-slate-900 mb-4",
                    ),
                    rx.cond(
                        AppState.upcoming_events.length() > 0,
                        rx.el.div(
                            rx.foreach(AppState.upcoming_events, upcoming_event_card),
                            class_name="flex flex-col gap-4",
                        ),
                        rx.el.div(
                            rx.icon(
                                "calendar-check",
                                class_name="h-8 w-8 text-slate-400 mx-auto mb-2",
                            ),
                            rx.el.p(
                                "No upcoming events. Time to plan!",
                                class_name="text-center text-slate-500",
                            ),
                            rx.el.a(
                                "Plan an Event",
                                href="/event-planner",
                                class_name="mt-2 text-sm font-semibold text-orange-600 hover:underline",
                            ),
                            class_name="text-center flex flex-col items-center p-8 bg-slate-100/50 rounded-lg border border-dashed",
                        ),
                    ),
                    class_name="lg:col-span-2",
                ),
                rx.el.div(
                    rx.el.h2(
                        "Smart Suggestions",
                        class_name="text-2xl font-bold text-slate-900 mb-4",
                    ),
                    rx.el.p(
                        "Keep your energy where it counts. Here are some ideas:",
                        class_name="text-slate-500 mb-4",
                    ),
                    rx.cond(
                        AppState.suggestions.length() > 0,
                        rx.el.div(
                            rx.foreach(AppState.suggestions, suggestion_card),
                            class_name="flex flex-col gap-4",
                        ),
                        rx.el.div(
                            rx.icon(
                                "sparkles",
                                class_name="h-8 w-8 text-slate-400 mx-auto mb-2",
                            ),
                            rx.el.p(
                                "No new suggestions right now.",
                                class_name="text-center text-slate-500",
                            ),
                            class_name="text-center p-8 bg-slate-100/50 rounded-lg border border-dashed",
                        ),
                    ),
                    class_name="lg:col-span-2",
                ),
                class_name="mt-8 grid grid-cols-1 lg:grid-cols-[repeat(2,minmax(0,1fr))_320px] gap-8 items-start",
            ),
            class_name="max-w-7xl mx-auto p-4 sm:p-6 lg:p-8",
        ),
        class_name="flex-1 overflow-y-auto bg-cool-gray-50",
    )