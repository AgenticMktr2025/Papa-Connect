import reflex as rx
from app.state.state import AppState


def faq_item(faq: dict, index: int) -> rx.Component:
    return rx.el.div(
        rx.el.button(
            rx.el.h3(
                faq["question"], class_name="font-semibold text-slate-800 text-left"
            ),
            rx.icon(
                rx.cond(
                    AppState.faq_open_state[index.to_string()],
                    "chevron-up",
                    "chevron-down",
                ),
                class_name="h-5 w-5 text-slate-500 transition-transform",
            ),
            on_click=lambda: AppState.toggle_faq(index),
            class_name="w-full flex justify-between items-center py-4",
        ),
        rx.cond(
            AppState.faq_open_state[index.to_string()],
            rx.el.div(
                rx.el.p(faq["answer"], class_name="text-slate-600 pb-4"),
                class_name="animate-in fade-in duration-300",
            ),
            None,
        ),
        class_name="border-b border-slate-200",
    )


def help_support_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.a(
                rx.icon("arrow-left", class_name="h-5 w-5 mr-2"),
                "Back to Home",
                href="/home",
                class_name="flex items-center font-semibold text-slate-800 hover:underline mb-8",
            ),
            rx.el.h1(
                "Help & Support", class_name="text-3xl font-bold text-slate-900 mb-2"
            ),
            rx.el.p(
                "Find answers to common questions and get in touch with our team.",
                class_name="text-slate-600 mb-8",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.h2(
                        "Frequently Asked Questions",
                        class_name="text-xl font-bold text-slate-900 mb-4",
                    ),
                    rx.el.div(rx.foreach(AppState.faqs, faq_item)),
                    class_name="p-6 bg-white border rounded-lg shadow-sm",
                ),
                rx.el.div(
                    rx.el.h2(
                        "Contact Support",
                        class_name="text-xl font-bold text-slate-900 mb-4",
                    ),
                    rx.el.p(
                        "Can't find what you're looking for? Our team is here to help.",
                        class_name="text-slate-600 mb-4",
                    ),
                    rx.el.button(
                        rx.icon("mail", class_name="mr-2"),
                        "Email Support",
                        class_name="w-full flex items-center justify-center bg-slate-800 text-white font-semibold py-3 px-6 rounded-md hover:bg-slate-900 transition-all",
                    ),
                    class_name="p-6 bg-white border rounded-lg shadow-sm",
                ),
                class_name="grid md:grid-cols-2 gap-8 items-start",
            ),
        ),
        class_name="max-w-6xl mx-auto p-4 sm:p-8",
    )