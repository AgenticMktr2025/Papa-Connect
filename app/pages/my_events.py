import reflex as rx
from app.state.state import AppState
from app.models.models import Event


def event_card(event: Event) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.h3(event.title, class_name="font-semibold text-gray-800"),
                rx.el.p(
                    f"with {AppState.get_connection_name_by_id.get(event.connection_id, 'a friend')}",
                    class_name="text-sm text-gray-500",
                ),
            ),
            rx.el.div(
                rx.el.button(
                    "Edit",
                    class_name="text-sm font-medium text-green-800 hover:underline",
                ),
                rx.el.button(
                    "Cancel",
                    class_name="text-sm font-medium text-red-600 hover:underline",
                ),
                class_name="flex gap-4",
            ),
            class_name="flex justify-between items-start mb-3",
        ),
        rx.el.div(
            rx.el.div(
                rx.icon("calendar", class_name="h-4 w-4 text-gray-500 mr-2"),
                rx.el.p(event.date, class_name="text-sm text-gray-600 font-medium"),
                class_name="flex items-center",
            ),
            rx.el.div(
                rx.icon("clock", class_name="h-4 w-4 text-gray-500 mr-2"),
                rx.el.p(event.time, class_name="text-sm text-gray-600 font-medium"),
                class_name="flex items-center",
            ),
            rx.el.div(
                rx.icon("map-pin", class_name="h-4 w-4 text-gray-500 mr-2"),
                rx.el.p(event.location, class_name="text-sm text-gray-600 font-medium"),
                class_name="flex items-center",
            ),
            class_name="flex flex-wrap items-center gap-x-4 gap-y-2",
        ),
        class_name="p-5 bg-white border rounded-xl shadow-sm",
    )


def event_list_section(title: str, events: rx.Var[list[Event]]) -> rx.Component:
    return rx.el.div(
        rx.el.h2(title, class_name="text-2xl font-bold text-gray-900 mb-4"),
        rx.cond(
            events.length() > 0,
            rx.el.div(rx.foreach(events, event_card), class_name="flex flex-col gap-4"),
            rx.el.div(
                rx.icon(
                    "calendar-x-2", class_name="h-8 w-8 text-gray-400 mx-auto mb-2"
                ),
                rx.el.p("No events here.", class_name="text-center text-gray-500"),
                class_name="text-center p-8 bg-gray-50 rounded-lg border border-dashed",
            ),
        ),
    )


def my_events_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.a(
                rx.icon("arrow-left", class_name="h-5 w-5 mr-2"),
                "Back to Home",
                href="/home",
                class_name="flex items-center font-semibold text-slate-800 hover:underline mb-8",
            ),
            rx.el.div(
                rx.el.h1("My Events", class_name="text-3xl font-bold text-slate-900"),
                rx.el.div(
                    rx.el.label(
                        "Filter by connection:",
                        class_name="text-sm font-medium text-slate-600 mr-2",
                    ),
                    rx.el.select(
                        rx.el.option("All Connections", value="all"),
                        rx.foreach(
                            AppState.connections,
                            lambda conn: rx.el.option(
                                conn.peer_name, value=conn.id.to_string()
                            ),
                        ),
                        on_change=AppState.set_event_filter_connection,
                        class_name="p-2 border rounded-md bg-white",
                        default_value="all",
                    ),
                    class_name="flex items-center",
                ),
                class_name="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4 mb-6",
            ),
            event_list_section("Upcoming Events", AppState.filtered_upcoming_events),
            rx.el.div(class_name="my-8 border-t"),
            event_list_section("Past Events", AppState.filtered_past_events),
            class_name="w-full max-w-4xl mx-auto",
        ),
        class_name="flex items-start justify-center min-h-screen bg-cool-gray-50 font-['Poppins'] p-4 sm:p-8",
    )