import reflex as rx
from app.state.state import AppState
from app.pages.dashboard import status_indicator


def nav_item(item: dict) -> rx.Component:
    return rx.el.a(
        rx.icon(item["icon"], class_name="h-5 w-5"),
        rx.cond(
            AppState.sidebar_collapsed,
            None,
            rx.el.span(item["label"], class_name="font-medium"),
        ),
        href=item["path"],
        class_name=rx.cond(
            AppState.router.page.path == item["path"],
            "flex items-center gap-3 rounded-lg bg-slate-100 px-3 py-2 text-slate-900 transition-all hover:text-slate-900",
            "flex items-center gap-3 rounded-lg px-3 py-2 text-slate-500 transition-all hover:text-slate-900",
        ),
        rx_props={"tooltip": item["label"], "tooltip_options": {"side": "right"}},
    )


def sidebar() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.a(
                        rx.icon(
                            "circle-user-round", class_name="h-8 w-8 text-orange-600"
                        ),
                        rx.cond(
                            AppState.sidebar_collapsed,
                            None,
                            rx.el.span("PapaConnect", class_name="font-bold"),
                        ),
                        href="/home",
                        class_name="flex items-center gap-2 text-lg font-semibold",
                    ),
                    rx.el.button(
                        rx.icon("panel-left-close", class_name="h-6 w-6"),
                        on_click=AppState.toggle_sidebar,
                        class_name="p-1 rounded-md hover:bg-slate-200",
                    ),
                    class_name="flex items-center justify-between p-4 border-b",
                ),
                rx.el.nav(
                    rx.foreach(AppState.nav_items, nav_item),
                    class_name="flex flex-col gap-2 p-4 text-sm font-medium",
                ),
                class_name="flex-1 overflow-y-auto",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.a(
                        rx.icon("log-out", class_name="h-5 w-5"),
                        rx.cond(AppState.sidebar_collapsed, None, rx.el.span("Logout")),
                        href="#",
                        on_click=AppState.logout,
                        class_name="flex items-center gap-3 rounded-lg px-3 py-2 text-red-500 transition-all hover:text-red-600 font-medium",
                    ),
                    class_name="flex flex-col gap-2 p-4 border-t",
                )
            ),
            class_name="flex h-full max-h-screen flex-col justify-between",
        ),
        class_name="hidden border-r bg-slate-100/40 md:block transition-all duration-300",
        width=rx.cond(AppState.sidebar_collapsed, "5rem", "16rem"),
    )