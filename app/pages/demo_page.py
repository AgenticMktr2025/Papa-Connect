import reflex as rx
from app.state.state import AppState
from app.pages.dashboard import dashboard_page
from app.components.sidebar import sidebar, nav_item


def mobile_sidebar() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.button(
                rx.icon("x", class_name="h-6 w-6"),
                on_click=AppState.toggle_mobile_sidebar,
                class_name="absolute top-4 right-4 text-slate-500 hover:text-slate-800",
            ),
            rx.el.a(
                rx.icon("circle-user-round", class_name="h-8 w-8 text-orange-600"),
                rx.el.span("PapaConnect", class_name="text-lg font-bold"),
                href="/home",
                class_name="flex items-center gap-2 mb-8",
            ),
            rx.el.nav(
                rx.foreach(AppState.nav_items, nav_item),
                class_name="grid items-start text-sm font-medium",
            ),
        ),
        class_name="fixed inset-0 z-50 bg-white p-6 animate-in slide-in-from-left-full duration-300 md:hidden",
    )


def mobile_header() -> rx.Component:
    return rx.el.header(
        rx.el.button(
            rx.icon("menu", class_name="h-6 w-6"),
            on_click=AppState.toggle_mobile_sidebar,
        ),
        rx.el.a(
            rx.icon("circle-user-round", class_name="h-8 w-8 text-orange-600"),
            href="/home",
        ),
        rx.el.div(rx.el.div(class_name="h-6 w-6")),
        class_name="sticky top-0 z-30 flex h-16 items-center justify-between gap-4 border-b bg-white px-4 md:hidden",
    )


def demo_page() -> rx.Component:
    """The demo page, which wraps the dashboard in a sidebar layout."""
    return rx.el.div(
        sidebar(),
        rx.el.div(
            mobile_header(),
            dashboard_page(),
            class_name="flex flex-col w-full min-h-screen ml-auto",
            width=rx.cond(
                AppState.sidebar_collapsed, "calc(100% - 5rem)", "calc(100% - 16rem)"
            ),
        ),
        rx.cond(AppState.mobile_sidebar_open, mobile_sidebar(), None),
        class_name="flex min-h-screen w-full",
    )