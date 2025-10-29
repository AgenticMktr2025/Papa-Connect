import reflex as rx
import reflex as rx
from app.state.state import AppState
from app.pages.dashboard import dashboard_page
from app.pages.onboarding import onboarding_page
from app.pages.add_contact import add_contact_page
from app.pages.connection_detail import connection_detail_page
from app.pages.event_planner import event_planner_page
from app.pages.my_events import my_events_page
from app.pages.breathing_space import breathing_space_page
from app.pages.analytics_page import analytics_page
from app.pages.settings import settings_page
from app.pages.unsubscribe import unsubscribe_page
from app.pages.help_support import help_support_page
from app.pages.login_page import splash_page


def index() -> rx.Component:
    return rx.cond(
        AppState.is_loaded,
        rx.cond(
            AppState.is_authenticated,
            rx.el.div(
                dashboard_page(),
                class_name="min-h-screen w-full bg-cool-gray-50 font-['Poppins']",
            ),
            splash_page(),
        ),
        rx.el.div(
            rx.spinner(class_name="h-12 w-12 text-orange-500"),
            class_name="flex items-center justify-center min-h-screen",
        ),
    )


def home() -> rx.Component:
    return rx.el.div(
        dashboard_page(),
        class_name="min-h-screen w-full bg-cool-gray-50 font-['Poppins']",
    )


def settings() -> rx.Component:
    return rx.el.div(
        settings_page(),
        class_name="min-h-screen w-full bg-cool-gray-50 font-['Poppins']",
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(index, on_load=AppState.on_load)
app.add_page(home, route="/home", on_load=AppState.on_load)
app.add_page(onboarding_page, route="/onboarding")
app.add_page(add_contact_page, route="/add-contact")
app.add_page(connection_detail_page, route="/connections/[id]")
app.add_page(event_planner_page, route="/event-planner")
app.add_page(my_events_page, route="/my-events")
app.add_page(breathing_space_page, route="/breathing-space")
app.add_page(analytics_page, route="/analytics")
app.add_page(settings, route="/settings")
app.add_page(help_support_page, route="/help-support")
app.add_page(unsubscribe_page, route="/unsubscribe")