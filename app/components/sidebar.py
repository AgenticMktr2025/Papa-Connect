import reflex as rx
from app.state.state import AppState
from app.pages.dashboard import status_indicator


def nav_item(item: dict) -> rx.Component:
    return rx.el.a(
        rx.icon(item["icon"], class_name="h-5 w-5"),
        rx.el.span(item["label"], class_name="font-medium"),
        href=item["path"],
        class_name=rx.cond(
            AppState.router.page.path == item["path"],
            "flex items-center gap-3 rounded-lg bg-slate-100 px-3 py-2 text-slate-900 transition-all hover:text-slate-900",
            "flex items-center gap-3 rounded-lg px-3 py-2 text-slate-500 transition-all hover:text-slate-900",
        ),
    )


def sidebar() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.a(
                    rx.icon("circle-user-round", class_name="h-8 w-8 text-orange-600"),
                    rx.el.span("PapaConnect", class_name="sr-only"),
                    href="/home",
                    class_name="flex items-center gap-2 text-lg font-semibold md:text-base",
                ),
                rx.el.nav(
                    rx.foreach(AppState.nav_items, nav_item),
                    class_name="grid items-start px-2 text-sm font-medium lg:px-4",
                ),
                class_name="flex-1",
            ),
            rx.el.div(
                status_indicator(AppState.user.status),
                rx.el.a(
                    rx.icon("log-out", class_name="h-5 w-5"),
                    "Logout",
                    href="#",
                    on_click=AppState.logout,
                    class_name="flex items-center gap-3 rounded-lg px-3 py-2 text-red-500 transition-all hover:text-red-600 font-medium",
                ),
                class_name="mt-auto p-4 space-y-2",
            ),
            class_name="flex h-full max-h-screen flex-col gap-2",
        ),
        class_name="hidden border-r bg-slate-100/40 md:block",
    )