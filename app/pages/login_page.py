import reflex as rx
from app.state.state import AppState


def google_signin_button() -> rx.Component:
    return rx.el.button(
        rx.icon("mail", class_name="h-5 w-5"),
        rx.el.span("Sign in with Google", class_name="font-semibold"),
        on_click=lambda: rx.redirect("/home"),
        class_name="w-full flex items-center justify-center gap-3 py-3 px-4 bg-white border border-slate-300 rounded-lg hover:bg-slate-50 transition-all text-slate-800",
    )


def email_signin_form() -> rx.Component:
    return rx.el.form(
        rx.el.div(
            rx.el.label(
                "Email Address", class_name="text-sm font-medium text-slate-400"
            ),
            rx.el.input(
                placeholder="you@example.com",
                name="email",
                type="email",
                required=True,
                class_name="w-full mt-1 p-2 bg-slate-700 border border-slate-600 rounded-md focus:ring-2 focus:ring-orange-500 text-white",
            ),
            class_name="mb-4",
        ),
        rx.el.div(
            rx.el.label("Password", class_name="text-sm font-medium text-slate-400"),
            rx.el.input(
                placeholder="********",
                name="password",
                type="password",
                required=True,
                class_name="w-full mt-1 p-2 bg-slate-700 border border-slate-600 rounded-md focus:ring-2 focus:ring-orange-500 text-white",
            ),
            class_name="mb-4",
        ),
        rx.cond(
            AppState.login_error != "",
            rx.el.p(AppState.login_error, class_name="text-sm text-red-400 mb-4"),
        ),
        rx.el.button(
            "Sign In with Email",
            type="submit",
            class_name="w-full bg-slate-900 text-white font-semibold py-3 px-6 rounded-lg hover:bg-slate-950 transition-all",
        ),
        on_submit=AppState.login,
    )


def splash_page() -> rx.Component:
    return rx.el.div(
        rx.video(
            src=AppState.current_video_url,
            auto_play=True,
            muted=True,
            loop=True,
            class_name="absolute top-0 left-0 w-full h-full object-cover z-0",
            style={"filter": "brightness(0.4)"},
        ),
        rx.el.div(
            class_name="absolute top-0 left-0 w-full h-full bg-slate-900/50 z-10"
        ),
        rx.el.div(
            rx.el.h2(
                "Welcome to Papa Connect",
                class_name="text-3xl font-bold text-white text-center mb-2",
            ),
            rx.el.p(
                "The app that helps dads actually meet up.",
                class_name="text-slate-300 text-center mb-8",
            ),
            google_signin_button(),
            rx.el.div(
                rx.el.hr(class_name="w-full border-slate-600"),
                rx.el.span(
                    "OR",
                    class_name="absolute px-3 bg-slate-800 text-sm text-slate-400 font-medium",
                    style={"left": "50%", "transform": "translateX(-50%)"},
                ),
                class_name="relative flex items-center justify-center my-6",
            ),
            email_signin_form(),
            rx.el.p(
                "Don't have an account? ",
                rx.el.a(
                    "Sign up here",
                    on_click=AppState.toggle_signup,
                    class_name="font-semibold text-orange-500 hover:underline cursor-pointer",
                ),
                class_name="text-center text-sm text-slate-300 mt-6",
            ),
            class_name="relative z-20 w-full max-w-sm p-8 bg-slate-800/80 backdrop-blur-sm rounded-xl shadow-lg border border-slate-700",
        ),
        class_name="relative flex items-center justify-center min-h-screen bg-slate-900 font-['Poppins'] p-4 overflow-hidden",
    )