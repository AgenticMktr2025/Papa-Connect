import reflex as rx
from app.state.state import AppState
from app.pages.analytics_page import stat_card


def before_you_go_step() -> rx.Component:
    return rx.el.div(
        rx.el.h1(
            "Wait, before you go...", class_name="text-4xl font-bold text-gray-900 mb-4"
        ),
        rx.el.p(
            "Look at the quiet wins you've accomplished:",
            class_name="text-lg text-gray-600 mb-8",
        ),
        rx.el.div(
            stat_card(
                "users",
                "Active Connections",
                AppState.stats.active_connections,
                "bg-blue-100 text-blue-600",
            ),
            stat_card(
                "arrow-right-left",
                "Total Exchanges",
                AppState.stats.total_exchanges,
                "bg-green-100 text-green-800",
            ),
            stat_card(
                "calendar-check",
                "Events Coordinated",
                AppState.stats.events_coordinated,
                "bg-emerald-100 text-emerald-600",
            ),
            stat_card(
                "trophy",
                "Longest Relationship",
                f"{AppState.stats.longest_relationship_days} days",
                "bg-amber-100 text-amber-600",
            ),
            class_name="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 mb-10",
        ),
        rx.el.div(
            rx.el.h3(
                "Feeling overwhelmed?",
                class_name="text-xl font-bold text-gray-800 mb-2",
            ),
            rx.el.p(
                "Instead of deleting your account, you can take a break. We'll pause all timers and notifications.",
                class_name="text-gray-600 mb-4 max-w-2xl mx-auto",
            ),
            rx.el.a(
                rx.icon("circle_pause", class_name="mr-2"),
                "Try Breathing Space instead",
                href="/breathing-space",
                class_name="inline-flex items-center justify-center font-semibold text-white py-3 px-8 rounded-lg transition-colors bg-green-800 hover:bg-green-900 mb-6",
            ),
            rx.el.button(
                "No, I want to permanently delete my account",
                on_click=AppState.unsubscribe_account,
                class_name="text-sm font-medium text-red-600 hover:underline",
            ),
            class_name="p-8 bg-white rounded-xl shadow-lg border w-full max-w-4xl text-center",
        ),
    )


def unsubscribing_step() -> rx.Component:
    return rx.el.div(
        rx.spinner(class_name="h-12 w-12 text-green-800"),
        rx.el.h2(
            "We're deleting your account...",
            class_name="text-2xl font-bold text-center text-gray-800 mt-4",
        ),
        rx.el.p(
            "Your data will be permanently removed. This may take a moment.",
            class_name="text-center text-gray-500 mt-2",
        ),
        class_name="p-12 bg-white rounded-xl shadow-lg border w-full max-w-md text-center flex flex-col items-center",
    )


def confirmation_step() -> rx.Component:
    return rx.el.div(
        rx.icon("trash-2", class_name="h-16 w-16 text-gray-400 mx-auto mb-4"),
        rx.el.h2(
            "Account Deleted", class_name="text-3xl font-bold text-center text-gray-800"
        ),
        rx.el.p(
            "Your account and all associated data have been permanently deleted. We're sorry to see you go.",
            class_name="text-center text-gray-500 mt-2 max-w-sm mx-auto",
        ),
        class_name="p-12 bg-white rounded-xl shadow-lg border w-full max-w-md text-center",
    )


def unsubscribe_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.match(
                AppState.unsubscribe_step,
                (1, before_you_go_step()),
                (2, unsubscribing_step()),
                (3, confirmation_step()),
                before_you_go_step(),
            )
        ),
        class_name="flex items-center justify-center min-h-screen bg-stone-100 font-['Poppins'] p-4 sm:p-8",
    )