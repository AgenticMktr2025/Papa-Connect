import reflex as rx
import reflex_clerk_api as clerk
from app.state.state import AppState


def splash_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            class_name="absolute inset-0 bg-cover bg-center",
            style={"backgroundImage": "url('/aries_symbol_curved.png')"},
        ),
        rx.el.div(class_name="absolute inset-0 bg-black/60"),
        rx.el.div(
            rx.el.h1(
                "Papa Connect",
                class_name="text-6xl font-bold text-white tracking-tighter",
            ),
            rx.el.p(
                "The app that helps dads actually meet up.",
                class_name="text-xl text-slate-300 mt-2 max-w-lg text-center",
            ),
            clerk.sign_in_button(
                rx.el.button(
                    "Connect",
                    class_name="mt-12 h-40 w-40 rounded-full bg-orange-600 text-white text-2xl font-bold shadow-2xl hover:bg-orange-700 hover:scale-105 transition-all",
                )
            ),
            rx.el.p(
                "Want to see before you sign up? View the ",
                rx.el.span(
                    "demo",
                    on_click=AppState.toggle_demo_mode,
                    class_name="font-bold underline cursor-pointer hover:text-orange-400",
                ),
                class_name="text-slate-400 mt-8",
            ),
            class_name="relative z-10 flex flex-col items-center text-center",
        ),
        class_name="relative flex items-center justify-center min-h-screen bg-black font-['Poppins'] p-4 overflow-hidden",
    )