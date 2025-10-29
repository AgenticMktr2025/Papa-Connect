import reflex as rx
import reflex_clerk_api as clerk
from app.state.state import AppState


def collage_background() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.image(src="placeholder.svg", class_name="object-cover w-full h-full"),
            rx.el.image(src="placeholder.svg", class_name="object-cover w-full h-full"),
            class_name="grid grid-cols-2 w-full h-1/2 gap-2",
        ),
        rx.el.div(
            rx.el.image(src="placeholder.svg", class_name="object-cover w-full h-full"),
            rx.el.image(src="placeholder.svg", class_name="object-cover w-full h-full"),
            rx.el.image(src="placeholder.svg", class_name="object-cover w-full h-full"),
            class_name="grid grid-cols-3 w-full h-1/2 gap-2",
        ),
        class_name="absolute inset-0 w-full h-full flex flex-col gap-2 p-2 opacity-30",
    )


def splash_page() -> rx.Component:
    return rx.el.div(
        collage_background(),
        rx.el.div(
            class_name="absolute inset-0 bg-gradient-to-t from-black via-black/80 to-transparent"
        ),
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