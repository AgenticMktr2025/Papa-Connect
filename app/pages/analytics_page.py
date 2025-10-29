import reflex as rx
from app.state.state import AppState
from collections import Counter


def stat_card(icon: str, label: str, value: rx.Var, color: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(icon, class_name="h-6 w-6"), class_name=f"p-3 {color} rounded-md"
        ),
        rx.el.div(
            rx.el.p(label, class_name="text-sm font-medium text-slate-500"),
            rx.el.p(value, class_name="text-3xl font-bold text-slate-900"),
        ),
        class_name="flex items-center gap-4 p-5 bg-white border rounded-lg shadow-sm transition-all hover:shadow-md hover:-translate-y-1",
    )


def tier_breakdown_chart() -> rx.Component:
    return rx.recharts.pie_chart(
        rx.recharts.graphing_tooltip(cursor=False),
        rx.recharts.pie(
            rx.foreach(
                AppState.connection_tier_breakdown,
                lambda item, index: rx.recharts.cell(
                    fill=rx.Var.create(["#1e293b", "#475569", "#64748b"])[index]
                ),
            ),
            data=AppState.connection_tier_breakdown,
            data_key="count",
            name_key="tier",
            inner_radius=60,
            outer_radius=80,
            padding_angle=5,
            custom_attrs={"cornerRadius": 5},
            stroke="#fff",
            stroke_width=2,
        ),
        width="100%",
        height=250,
    )


def monthly_activity_chart() -> rx.Component:
    return rx.recharts.line_chart(
        rx.recharts.cartesian_grid(
            horizontal=True, vertical=False, class_name="opacity-25"
        ),
        rx.recharts.graphing_tooltip(cursor=False),
        rx.recharts.x_axis(
            data_key="month", tick_line=False, axis_line=False, class_name="text-xs"
        ),
        rx.recharts.y_axis(
            tick_line=False, axis_line=False, width=20, class_name="text-xs"
        ),
        rx.recharts.line(
            data_key="events",
            type_="natural",
            stroke="#1e293b",
            stroke_width=2,
            dot=False,
        ),
        data=AppState.monthly_event_counts,
        width="100%",
        height=250,
        margin={"top": 5, "right": 10, "left": -10, "bottom": 5},
    )


def top_connection_item(connection: dict) -> rx.Component:
    return rx.el.div(
        rx.el.image(
            src=f"https://api.dicebear.com/9.x/notionists/svg?seed={connection['name']}",
            class_name="h-10 w-10 rounded-full",
        ),
        rx.el.div(
            rx.el.p(connection["name"], class_name="font-semibold text-slate-800"),
            rx.el.p(
                f"{connection['event_count']} events",
                class_name="text-sm text-slate-500",
            ),
        ),
        rx.el.div(
            f"#{connection['rank']}",
            class_name="ml-auto text-lg font-bold text-slate-400",
        ),
        class_name="flex items-center gap-4 p-3 bg-slate-100/80 border rounded-md",
    )


def analytics_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.a(
                rx.icon("arrow-left", class_name="h-5 w-5 mr-2"),
                "Back to Home",
                href="/home",
                class_name="flex items-center font-semibold text-slate-800 hover:underline mb-8",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.h1(
                        "Your Quiet Wins",
                        class_name="text-3xl font-bold text-slate-900",
                    ),
                    rx.el.p(
                        "These numbers tell a story of showing up.",
                        class_name="text-slate-600 mt-1",
                    ),
                ),
                rx.el.button(
                    rx.icon("download", class_name="mr-2"),
                    "Export Stats",
                    on_click=lambda: rx.console_log("Exporting stats..."),
                    class_name="bg-white border text-slate-700 font-semibold py-2 px-4 rounded-md hover:bg-slate-100 transition-all shadow-sm",
                ),
                class_name="flex justify-between items-start mb-8",
            ),
            rx.el.div(
                stat_card(
                    "users",
                    "Active Connections",
                    AppState.stats.active_connections,
                    "bg-blue-100 text-blue-700",
                ),
                stat_card(
                    "arrow-right-left",
                    "Total Exchanges",
                    AppState.stats.total_exchanges,
                    "bg-teal-100 text-teal-700",
                ),
                stat_card(
                    "calendar-check",
                    "Events Coordinated",
                    AppState.stats.events_coordinated,
                    "bg-sky-100 text-sky-700",
                ),
                stat_card(
                    "trophy",
                    "Longest Relationship",
                    f"{AppState.stats.longest_relationship_days} days",
                    "bg-orange-100 text-orange-700",
                ),
                stat_card(
                    "sparkles",
                    "Revived Connections",
                    AppState.stats.revived_connections,
                    "bg-indigo-100 text-indigo-700",
                ),
                class_name="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-6 mb-8",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.h3(
                        "Tier Breakdown",
                        class_name="text-xl font-bold text-slate-900 mb-4",
                    ),
                    tier_breakdown_chart(),
                    class_name="p-6 bg-white border rounded-lg shadow-sm",
                ),
                rx.el.div(
                    rx.el.h3(
                        "Monthly Activity",
                        class_name="text-xl font-bold text-slate-900 mb-4",
                    ),
                    monthly_activity_chart(),
                    class_name="p-6 bg-white border rounded-lg shadow-sm",
                ),
                class_name="grid md:grid-cols-2 gap-6 mb-8",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.h3(
                        "Top Connections",
                        class_name="text-xl font-bold text-slate-900 mb-4",
                    ),
                    rx.el.div(
                        rx.foreach(
                            AppState.top_connections_by_events, top_connection_item
                        ),
                        class_name="flex flex-col gap-3",
                    ),
                    class_name="p-6 bg-white border rounded-lg shadow-sm",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.div(
                            f"{AppState.engagement_rate}%",
                            class_name="text-5xl font-bold text-slate-800",
                        ),
                        rx.el.p(
                            "Engagement Rate", class_name="font-semibold text-slate-600"
                        ),
                        class_name="text-center",
                    ),
                    rx.el.p(
                        "Ratio of connections with recent events.",
                        class_name="text-center text-sm text-slate-500 mt-4",
                    ),
                    class_name="p-6 bg-white border rounded-lg shadow-sm h-full flex flex-col justify-center items-center",
                ),
                class_name="grid md:grid-cols-2 gap-6",
            ),
            class_name="w-full max-w-7xl mx-auto",
        ),
        class_name="flex items-start justify-center min-h-screen bg-cool-gray-50 font-['Poppins'] p-4 sm:p-8",
    )