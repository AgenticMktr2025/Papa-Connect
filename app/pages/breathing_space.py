import reflex as rx
from app.state.state import AppState
from app.pages.dashboard import status_indicator


def breathing_space_header() -> rx.Component:
    return rx.el.div(
        rx.el.h1("Breathing Space", class_name="text-3xl font-bold text-slate-900"),
        status_indicator(AppState.user.status),
        class_name="flex items-center justify-between mb-4",
    )


def what_is_paused_card(icon: str, title: str, description: str) -> rx.Component:
    return rx.el.div(
        rx.icon(icon, class_name="h-6 w-6 text-orange-600"),
        rx.el.div(
            rx.el.h4(title, class_name="font-semibold text-slate-800"),
            rx.el.p(description, class_name="text-sm text-slate-500"),
        ),
        class_name="flex items-center gap-4 p-4 bg-slate-100 border rounded-md",
    )


def what_is_preserved_item(text: str) -> rx.Component:
    return rx.el.li(
        rx.icon("square_check", class_name="h-5 w-5 text-teal-500"),
        rx.el.span(text, class_name="text-slate-700"),
        class_name="flex items-center gap-3",
    )


def breathing_space_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.a(
                rx.icon("arrow-left", class_name="h-5 w-5 mr-2"),
                "Back to Home",
                href="/home",
                class_name="flex items-center font-semibold text-slate-800 hover:underline mb-8",
            ),
            rx.el.div(
                breathing_space_header(),
                rx.el.p(
                    "Take the time you need. Your connections will be here when you're ready.",
                    class_name="text-slate-600 mb-8 max-w-2xl",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.h3(
                            "Set Duration",
                            class_name="font-semibold text-slate-800 mb-4",
                        ),
                        rx.el.div(
                            rx.foreach(
                                ["1 week", "2 weeks", "1 month", "Indefinite"],
                                lambda duration: rx.el.button(
                                    duration,
                                    on_click=lambda: AppState.set_breathing_duration(
                                        duration
                                    ),
                                    class_name=rx.cond(
                                        AppState.breathing_duration == duration,
                                        "font-semibold bg-slate-800 text-white px-4 py-2 rounded-md",
                                        "font-medium bg-white border px-4 py-2 rounded-md hover:bg-slate-100",
                                    ),
                                ),
                            ),
                            class_name="flex flex-wrap gap-3 mb-8",
                        ),
                        rx.el.button(
                            rx.cond(
                                AppState.user.status == "active",
                                rx.fragment(
                                    rx.icon("pause", class_name="mr-2"),
                                    "Activate Breathing Space",
                                ),
                                rx.fragment(
                                    rx.icon("play", class_name="mr-2"),
                                    "Resume Active Status",
                                ),
                            ),
                            on_click=AppState.toggle_breathing_space,
                            class_name="w-full flex items-center justify-center font-semibold text-white py-3 rounded-md transition-colors bg-slate-800 hover:bg-slate-900",
                        ),
                    ),
                    rx.el.div(
                        rx.el.h3(
                            "Paused Connections",
                            class_name="font-semibold text-slate-800 mb-4",
                        ),
                        rx.el.div(
                            rx.foreach(
                                AppState.connections,
                                lambda conn: rx.el.div(
                                    rx.el.image(
                                        src=conn.avatar_url,
                                        class_name="h-10 w-10 rounded-full",
                                    ),
                                    rx.el.p(
                                        conn.peer_name,
                                        class_name="font-medium text-slate-700",
                                    ),
                                    rx.icon(
                                        "timer-off",
                                        class_name="ml-auto h-5 w-5 text-slate-400",
                                    ),
                                    class_name="flex items-center gap-3 p-3 bg-slate-100 border rounded-md",
                                ),
                            ),
                            class_name="grid grid-cols-1 sm:grid-cols-2 gap-3",
                        ),
                    ),
                    class_name="grid lg:grid-cols-2 gap-8 mb-8",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.h3(
                            "What gets paused?",
                            class_name="font-semibold text-slate-800 mb-4",
                        ),
                        rx.el.div(
                            what_is_paused_card(
                                "bell-off",
                                "Notifications",
                                "All reminders and prompts will be muted.",
                            ),
                            what_is_paused_card(
                                "hourglass",
                                "Connection Timers",
                                "Dormancy and activation timers are frozen.",
                            ),
                            what_is_paused_card(
                                "brain-circuit",
                                "Smart Suggestions",
                                "You won't receive new meet-up ideas.",
                            ),
                            class_name="flex flex-col gap-3",
                        ),
                    ),
                    rx.el.div(
                        rx.el.h3(
                            "What's preserved?",
                            class_name="font-semibold text-slate-800 mb-4",
                        ),
                        rx.el.ul(
                            what_is_preserved_item(
                                "All your connections and their data."
                            ),
                            what_is_preserved_item("Your complete meet-up history."),
                            what_is_preserved_item("All private ratings and notes."),
                            what_is_preserved_item("Your analytics and achievements."),
                            class_name="space-y-3 p-4 bg-slate-100 border rounded-md",
                        ),
                    ),
                    class_name="grid md:grid-cols-2 gap-8",
                ),
                class_name="p-8 bg-white rounded-lg shadow-lg border w-full max-w-5xl",
            ),
        ),
        class_name="flex items-center justify-center min-h-screen bg-cool-gray-50 font-['Poppins'] p-4",
    )