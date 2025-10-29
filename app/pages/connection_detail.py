import reflex as rx
from app.state.state import AppState
from app.pages.dashboard import connection_state_badge


def detail_header() -> rx.Component:
    return rx.cond(
        AppState.current_connection,
        rx.el.div(
            rx.el.div(
                rx.el.a(
                    rx.icon("arrow-left", class_name="h-5 w-5 mr-2"),
                    "All Connections",
                    href="/home",
                    class_name="flex items-center font-semibold text-green-800 hover:underline mb-4",
                ),
                rx.el.div(
                    rx.el.image(
                        src=AppState.current_connection.avatar_url,
                        class_name="h-16 w-16 rounded-full",
                    ),
                    rx.el.div(
                        rx.el.h1(
                            AppState.current_connection.peer_name,
                            class_name="text-3xl font-bold text-gray-900",
                        )
                    ),
                    class_name="flex items-center gap-4",
                ),
            ),
            connection_state_badge(AppState.current_connection.state),
            class_name="flex items-start justify-between",
        ),
        rx.el.div("Connection not found."),
    )


def meet_up_history() -> rx.Component:
    def history_item(event: dict) -> rx.Component:
        return rx.el.div(
            rx.el.div(
                class_name="absolute w-3 h-3 bg-gray-200 rounded-full mt-1.5 -start-1.5 border border-white"
            ),
            rx.el.time(
                event.date,
                class_name="mb-1 text-sm font-normal leading-none text-gray-400",
            ),
            rx.el.h3(event.title, class_name="text-lg font-semibold text-gray-900"),
            rx.el.p(
                f"at {event.location}", class_name="text-base font-normal text-gray-500"
            ),
            class_name="ms-4 relative border-s border-gray-200 ps-4 py-2",
        )

    return rx.el.div(
        rx.el.h2("Meet-up History", class_name="text-2xl font-bold text-gray-900 mb-4"),
        rx.cond(
            AppState.get_events_for_connection.length() > 0,
            rx.el.div(rx.foreach(AppState.get_events_for_connection, history_item)),
            rx.el.div(
                rx.icon(
                    "calendar_x_2", class_name="h-8 w-8 text-gray-400 mx-auto mb-2"
                ),
                rx.el.p("No meet-ups yet.", class_name="text-center text-gray-500"),
                class_name="text-center p-8 bg-gray-50 rounded-lg border",
            ),
        ),
    )


def private_ratings() -> rx.Component:
    return rx.el.div(
        rx.el.h3("Private Rating", class_name="font-semibold text-gray-800 mb-2"),
        rx.el.div(
            rx.el.button(
                "⭐",
                class_name="p-2 text-2xl rounded-full hover:bg-gray-200 transition-all",
            ),
            rx.el.button(
                "⭐⭐",
                class_name="p-2 text-2xl rounded-full hover:bg-gray-200 transition-all",
            ),
            rx.el.button(
                "⭐⭐⭐",
                class_name="p-2 text-2xl rounded-full hover:bg-gray-200 transition-all",
            ),
            rx.el.button(
                "🏆",
                class_name="p-2 text-2xl rounded-full hover:bg-gray-200 transition-all",
            ),
            class_name="flex items-center gap-2",
        ),
    )


def connection_actions() -> rx.Component:
    return rx.el.div(
        rx.el.button(
            "Plan Event",
            class_name="flex-1 bg-green-800 text-white font-semibold py-3 px-6 rounded-lg hover:bg-green-900 transition-all",
        ),
        rx.el.button(
            "Send Message",
            class_name="flex-1 bg-gray-200 text-gray-800 font-semibold py-3 px-6 rounded-lg hover:bg-gray-300 transition-all",
        ),
        class_name="flex gap-4 mt-8",
    )


def connection_detail_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            detail_header(),
            rx.el.div(class_name="my-8 border-t border-gray-200"),
            rx.el.div(
                rx.el.div(meet_up_history(), class_name="w-full lg:w-2/3"),
                rx.el.div(
                    rx.el.div(
                        rx.el.h3(
                            "Shared Interests (Placeholder)",
                            class_name="font-semibold text-gray-800 mb-2",
                        ),
                        rx.el.div(
                            rx.foreach(
                                ["Hiking", "Board Games", "DIY Projects"],
                                lambda tag: rx.el.span(
                                    tag,
                                    class_name="px-3 py-1 bg-gray-100 text-gray-700 rounded-full text-sm font-medium",
                                ),
                            ),
                            class_name="flex flex-wrap gap-2 mb-6",
                        ),
                        private_ratings(),
                        class_name="p-6 bg-white border rounded-xl shadow-sm",
                    ),
                    class_name="w-full lg:w-1/3",
                ),
                class_name="flex flex-col lg:flex-row gap-8",
            ),
            connection_actions(),
            class_name="max-w-6xl mx-auto p-6 sm:p-8",
        ),
        class_name="bg-stone-50 min-h-screen font-['Poppins']",
    )