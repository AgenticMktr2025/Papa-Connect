import reflex as rx
from app.state.state import AppState
from app.pages.onboarding import selfie_capture_component


def settings_card_header(icon: str, title: str) -> rx.Component:
    return rx.el.div(
        rx.icon(icon, class_name="h-6 w-6 text-green-800"),
        rx.el.h3(title, class_name="text-lg font-bold text-gray-800"),
        class_name="flex items-center gap-3 border-b pb-4 mb-4",
    )


def profile_settings() -> rx.Component:
    return rx.el.div(
        settings_card_header("user_pen", "Profile Information"),
        rx.cond(
            AppState.avatar_edit_mode,
            rx.el.div(
                selfie_capture_component(),
                rx.el.button(
                    "Cancel",
                    on_click=lambda: AppState.toggle_avatar_edit_mode(False),
                    class_name="w-full text-center mt-2 text-sm font-medium text-slate-600 hover:underline",
                ),
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.button(
                        rx.el.image(
                            src=AppState.user_avatar_url,
                            class_name="h-24 w-24 rounded-full border-4 border-white shadow-md",
                        ),
                        rx.el.div(
                            rx.icon("pencil", class_name="h-5 w-5 text-white"),
                            class_name="absolute inset-0 flex items-center justify-center bg-black/50 opacity-0 group-hover:opacity-100 rounded-full transition-opacity",
                        ),
                        on_click=lambda: AppState.toggle_avatar_edit_mode(True),
                        class_name="relative group",
                    ),
                    class_name="flex justify-center mb-6",
                ),
                rx.el.form(
                    rx.el.div(
                        rx.el.label("Name", class_name="font-semibold text-gray-700"),
                        rx.el.input(
                            default_value=AppState.user.name,
                            name="name",
                            class_name="w-full mt-1 p-2 border rounded-md bg-gray-50",
                        ),
                        class_name="mb-4",
                    ),
                    rx.el.div(
                        rx.el.label("Phone", class_name="font-semibold text-gray-700"),
                        rx.el.input(
                            default_value=AppState.user.phone,
                            name="phone",
                            placeholder="+1 (555) 123-4567",
                            class_name="w-full mt-1 p-2 border rounded-md bg-gray-50",
                        ),
                        class_name="mb-4",
                    ),
                    rx.el.div(
                        rx.el.label("Email", class_name="font-semibold text-gray-700"),
                        rx.el.input(
                            default_value=AppState.user.email,
                            name="email",
                            is_disabled=True,
                            class_name="w-full mt-1 p-2 border rounded-md bg-gray-200 text-gray-500",
                        ),
                        class_name="mb-6",
                    ),
                    rx.el.button(
                        "Save Changes",
                        type="submit",
                        class_name="w-full bg-green-800 text-white font-semibold py-2.5 px-6 rounded-lg hover:bg-green-900 transition-all",
                    ),
                    on_submit=AppState.update_profile,
                ),
            ),
        ),
        class_name="p-6 bg-white border rounded-xl shadow-sm",
    )


def notification_settings() -> rx.Component:
    def toggle_switch(
        label: str, description: str, is_on: rx.Var[bool], on_toggle: rx.event.EventType
    ) -> rx.Component:
        return rx.el.div(
            rx.el.div(
                rx.el.p(label, class_name="font-semibold text-gray-800"),
                rx.el.p(description, class_name="text-sm text-gray-500"),
            ),
            rx.el.button(
                rx.el.span(
                    class_name=rx.cond(is_on, "translate-x-5", "translate-x-0")
                    + " pointer-events-none inline-block h-5 w-5 transform rounded-full bg-white shadow-lg ring-0 transition-transform duration-200 ease-in-out"
                ),
                on_click=on_toggle,
                class_name=rx.cond(is_on, "bg-green-800", "bg-gray-200")
                + " relative inline-flex h-6 w-11 flex-shrink-0 cursor-pointer rounded-full border-2 border-transparent transition-colors duration-200 ease-in-out focus:outline-none focus:ring-2 focus:ring-green-800 focus:ring-offset-2",
            ),
            class_name="flex justify-between items-center p-3 rounded-lg hover:bg-gray-50",
        )

    return rx.el.div(
        settings_card_header("bell", "Notifications"),
        rx.el.div(
            toggle_switch(
                "Email Notifications",
                "Receive summaries and reminders via email.",
                AppState.email_notifications_enabled,
                AppState.toggle_email_notifications,
            ),
            toggle_switch(
                "Push Notifications",
                "Get real-time alerts on your devices.",
                AppState.push_notifications_enabled,
                AppState.toggle_push_notifications,
            ),
            toggle_switch(
                "Smart Suggestions",
                "Receive proactive meet-up ideas.",
                AppState.smart_suggestions_enabled,
                AppState.toggle_smart_suggestions,
            ),
            class_name="flex flex-col gap-2",
        ),
        class_name="p-6 bg-white border rounded-xl shadow-sm",
    )


def account_management() -> rx.Component:
    return rx.el.div(
        settings_card_header("shield-alert", "Account Management"),
        rx.el.div(
            rx.el.button(
                rx.icon("cloud_download", class_name="mr-2"),
                "Export My Data",
                on_click=AppState.export_user_data,
                class_name="flex-1 text-center bg-gray-100 text-gray-800 font-semibold py-2.5 px-4 rounded-lg hover:bg-gray-200 transition-all",
            ),
            rx.el.a(
                rx.icon("trash-2", class_name="mr-2"),
                "Delete Account",
                href="/unsubscribe",
                on_click=AppState.initiate_account_deletion,
                class_name="flex-1 text-center bg-red-50 border-red-200 border text-red-600 font-semibold py-2.5 px-4 rounded-lg hover:bg-red-100 transition-all",
            ),
            class_name="flex gap-4",
        ),
        class_name="p-6 bg-white border rounded-xl shadow-sm",
    )


def settings_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.a(
                rx.icon("arrow-left", class_name="h-5 w-5 mr-2"),
                "Back to Home",
                href="/home",
                class_name="flex items-center font-semibold text-slate-800 hover:underline mb-8",
            ),
            rx.el.div(
                rx.el.h1("Settings", class_name="text-3xl font-bold text-gray-900"),
                rx.el.p(
                    "Manage your profile, notifications, and account settings.",
                    class_name="text-gray-600 mt-1",
                ),
                class_name="mb-8",
            ),
            rx.el.div(
                profile_settings(),
                notification_settings(),
                account_management(),
                class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8",
            ),
            class_name="w-full max-w-7xl mx-auto",
        ),
        class_name="flex items-start justify-center min-h-screen bg-stone-50 font-['Poppins'] p-4 sm:p-8",
    )