import reflex as rx
from app.state.state import AppState


def connection_selector() -> rx.Component:
    return rx.el.div(
        rx.el.label(
            "Who are you meeting with?", class_name="font-semibold text-gray-700 mb-2"
        ),
        rx.el.select(
            rx.el.option("Select a contact...", value="", disabled=True),
            rx.foreach(
                AppState.connections,
                lambda conn: rx.el.option(conn.peer_name, value=conn.id.to_string()),
            ),
            on_change=AppState.select_connection_for_planner,
            class_name="w-full p-3 border rounded-lg bg-white",
            default_value="",
        ),
        class_name="w-full",
    )


def availability_grid() -> rx.Component:
    return rx.el.div(
        rx.el.h3(
            "Availability (Placeholder)", class_name="font-semibold text-gray-800 mb-4"
        ),
        rx.el.div(
            rx.el.div(class_name="h-24 bg-gray-100 rounded-lg border p-2"),
            rx.el.div(
                class_name="h-24 bg-green-100 rounded-lg border border-green-200 p-2"
            ),
            rx.el.div(class_name="h-24 bg-gray-100 rounded-lg border p-2"),
            rx.el.div(
                class_name="h-24 bg-green-100 rounded-lg border border-green-200 p-2"
            ),
            rx.el.div(class_name="h-24 bg-gray-100 rounded-lg border p-2"),
            rx.el.div(
                class_name="h-24 bg-green-100 rounded-lg border border-green-200 p-2"
            ),
            rx.el.div(class_name="h-24 bg-gray-100 rounded-lg border p-2"),
            class_name="grid grid-cols-7 gap-2 animate-pulse",
        ),
    )


def time_slot_card(slot: dict) -> rx.Component:
    return rx.el.button(
        rx.el.div(
            rx.el.p(slot["date"], class_name="font-semibold text-green-800"),
            rx.el.p(
                f"{slot['time']} ({slot['duration']})",
                class_name="text-sm text-gray-600",
            ),
        ),
        rx.icon("arrow_right", class_name="h-6 w-6 text-gray-400"),
        class_name="flex items-center justify-between w-full p-4 border bg-white rounded-lg hover:border-green-500 hover:bg-green-50 transition-all text-left",
    )


def event_form() -> rx.Component:
    return rx.el.form(
        rx.el.div(
            rx.el.label("Event Title", class_name="font-semibold text-gray-700"),
            rx.el.input(
                name="title",
                placeholder="e.g., Park Hangout",
                required=True,
                class_name="w-full mt-1 p-2 border rounded-md",
            ),
            class_name="mb-4",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.label("Date", class_name="font-semibold text-gray-700"),
                rx.el.input(
                    name="date",
                    type="date",
                    required=True,
                    class_name="w-full mt-1 p-2 border rounded-md",
                ),
                class_name="flex-1",
            ),
            rx.el.div(
                rx.el.label("Time", class_name="font-semibold text-gray-700"),
                rx.el.input(
                    name="time",
                    type="time",
                    required=True,
                    class_name="w-full mt-1 p-2 border rounded-md",
                ),
                class_name="flex-1",
            ),
            class_name="flex gap-4 mb-4",
        ),
        rx.el.div(
            rx.el.label("Location", class_name="font-semibold text-gray-700"),
            rx.el.input(
                name="location",
                placeholder="e.g., Greenleaf Park",
                required=True,
                class_name="w-full mt-1 p-2 border rounded-md",
            ),
            class_name="mb-4",
        ),
        rx.el.div(
            rx.el.label("Notes (Optional)", class_name="font-semibold text-gray-700"),
            rx.el.textarea(
                name="notes",
                placeholder="Anything to remember?",
                class_name="w-full mt-1 p-2 border rounded-md",
            ),
            class_name="mb-6",
        ),
        rx.el.button(
            rx.icon("calendar-plus", class_name="mr-2"),
            "Confirm & Sync Event",
            type="submit",
            class_name="w-full flex items-center justify-center bg-green-800 text-white font-semibold py-3 px-6 rounded-lg hover:bg-green-900 transition-all",
        ),
        on_submit=AppState.create_event,
    )


def success_confirmation() -> rx.Component:
    return rx.el.div(
        rx.icon("check-check", class_name="h-16 w-16 text-teal-500 mx-auto mb-4"),
        rx.el.h2(
            "Event Scheduled!",
            class_name="text-2xl font-bold text-center text-slate-800",
        ),
        rx.el.p(
            "It's on the calendar. An invite has been sent.",
            class_name="text-center text-slate-500 mt-2",
        ),
        rx.el.a(
            "Back to Home",
            href="/home",
            class_name="mt-6 inline-block bg-slate-100 text-slate-800 font-semibold py-2 px-4 rounded-md hover:bg-slate-200",
        ),
        class_name="p-8 bg-white rounded-lg shadow-lg border w-full max-w-md text-center",
    )


def event_planner_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.cond(
                AppState.event_created_success,
                success_confirmation(),
                rx.el.div(
                    rx.el.a(
                        rx.icon("arrow-left", class_name="h-5 w-5 mr-2"),
                        "Back to Home",
                        href="/home",
                        class_name="flex items-center font-semibold text-slate-800 hover:underline mb-8",
                    ),
                    rx.el.h1(
                        "Plan an Event",
                        class_name="text-3xl font-bold text-slate-900 mb-6",
                    ),
                    connection_selector(),
                    rx.cond(
                        AppState.selected_connection_id_planner,
                        rx.el.div(
                            rx.el.div(class_name="my-8 border-t border-slate-200"),
                            rx.el.div(
                                rx.el.div(
                                    availability_grid(),
                                    rx.el.h3(
                                        "Suggested Times",
                                        class_name="font-semibold text-slate-800 my-4",
                                    ),
                                    rx.el.div(
                                        rx.foreach(
                                            AppState.suggested_time_slots,
                                            time_slot_card,
                                        ),
                                        class_name="grid md:grid-cols-3 gap-4",
                                    ),
                                    class_name="w-full lg:w-3/5",
                                ),
                                rx.el.div(
                                    rx.el.h3(
                                        "Event Details",
                                        class_name="font-semibold text-slate-800 mb-4",
                                    ),
                                    event_form(),
                                    class_name="w-full lg:w-2/5",
                                ),
                                class_name="flex flex-col lg:flex-row gap-8",
                            ),
                        ),
                        rx.el.div(
                            rx.icon(
                                "mouse_pointer",
                                class_name="h-12 w-12 text-slate-400 mx-auto mt-16 mb-4",
                            ),
                            rx.el.p(
                                "Select a contact to start planning.",
                                class_name="text-center text-slate-500",
                            ),
                            class_name="text-center py-12 bg-slate-100 rounded-lg border border-dashed mt-8",
                        ),
                    ),
                    class_name="p-8 bg-white rounded-lg shadow-lg border w-full max-w-7xl",
                ),
            )
        ),
        class_name="flex items-center justify-center min-h-screen bg-cool-gray-50 font-['Poppins'] p-4",
    )