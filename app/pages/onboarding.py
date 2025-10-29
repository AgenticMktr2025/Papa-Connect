import reflex as rx
from app.state.state import AppState


def progress_indicator() -> rx.Component:
    steps = [
        {"step": 1, "title": "Welcome"},
        {"step": 2, "title": "Connect Calendar"},
        {"step": 3, "title": "Create Dad Card"},
        {"step": 4, "title": "Done!"},
    ]

    def step_component(step_info: dict, current_step: rx.Var[int]) -> rx.Component:
        is_completed = current_step > step_info["step"].to(int)
        is_current = current_step == step_info["step"].to(int)
        return rx.el.div(
            rx.el.div(
                rx.cond(
                    is_completed,
                    rx.icon("check", class_name="h-4 w-4 text-white"),
                    rx.el.span(step_info["step"], class_name="text-sm font-bold"),
                ),
                rx.cond(
                    is_completed,
                    "w-8 h-8 rounded-full bg-slate-800 flex items-center justify-center",
                    rx.cond(
                        is_current,
                        "w-8 h-8 rounded-full bg-orange-100 border-2 border-orange-600 text-orange-600 flex items-center justify-center",
                        "w-8 h-8 rounded-full bg-slate-100 border-2 border-slate-300 text-slate-500 flex items-center justify-center",
                    ),
                ),
            ),
            rx.el.span(
                step_info["title"], class_name="mt-2 text-sm font-medium text-slate-600"
            ),
            class_name="flex flex-col items-center",
            on_click=lambda: AppState.set_onboarding_step(step_info["step"]),
        )

    return rx.el.div(
        rx.foreach(steps, lambda s: step_component(s, AppState.onboarding_step)),
        class_name="flex justify-between w-full max-w-2xl mx-auto mb-12",
    )


def welcome_step() -> rx.Component:
    return rx.el.div(
        rx.el.h2(
            "Welcome to Papa Connect!",
            class_name="text-3xl font-bold text-slate-900 mb-4",
        ),
        rx.el.p(
            "Let's get you set up to make meaningful connections with other dads.",
            class_name="text-slate-600 mb-8",
        ),
        rx.el.button(
            rx.icon("user-check", class_name="mr-2"),
            "Sign in with Google (Placeholder)",
            on_click=AppState.next_step,
            class_name="w-full flex items-center justify-center gap-2 bg-slate-800 text-white font-semibold py-3 px-6 rounded-md hover:bg-slate-900 transition-all",
        ),
    )


def calendar_step() -> rx.Component:
    return rx.el.div(
        rx.el.h2(
            "Link Your Calendar", class_name="text-3xl font-bold text-slate-900 mb-4"
        ),
        rx.el.p(
            "This helps find the best times for meet-ups without the back-and-forth.",
            class_name="text-slate-600 mb-8",
        ),
        rx.el.button(
            rx.icon("calendar-plus", class_name="mr-2"),
            "Connect Google Calendar (Placeholder)",
            on_click=AppState.next_step,
            class_name="w-full flex items-center justify-center gap-2 bg-slate-800 text-white font-semibold py-3 px-6 rounded-md hover:bg-slate-900 transition-all",
        ),
    )


def selfie_capture_component() -> rx.Component:
    return rx.el.div(
        rx.el.h3(
            "Create Your Avatar", class_name="text-xl font-bold text-slate-900 mb-2"
        ),
        rx.el.p(
            "Let's create a unique avatar for you.", class_name="text-slate-500 mb-6"
        ),
        rx.cond(
            AppState.capture_selfie_mode,
            rx.el.div(
                rx.el.div(
                    rx.cond(
                        AppState.is_processing_selfie,
                        rx.el.div(
                            rx.spinner(class_name="h-8 w-8 text-orange-500"),
                            rx.el.p(
                                "Extracting features...",
                                class_name="text-slate-500 mt-2",
                            ),
                            class_name="flex flex-col items-center justify-center h-full",
                        ),
                        rx.cond(
                            AppState.selfie_avatar_preview_url != "",
                            rx.el.div(
                                rx.el.p(
                                    "Here is your generated avatar!",
                                    class_name="text-center font-semibold text-slate-800 mb-4",
                                ),
                                rx.el.image(
                                    src=AppState.selfie_avatar_preview_url,
                                    class_name="h-32 w-32 rounded-full mx-auto border-4 border-white shadow-lg",
                                ),
                                rx.el.div(
                                    rx.foreach(
                                        AppState.selfie_features.items(),
                                        lambda item: rx.el.div(
                                            rx.el.span(
                                                f"{item[0].capitalize()}:",
                                                class_name="font-semibold",
                                            ),
                                            rx.el.span(item[1]),
                                            class_name="text-sm text-slate-600 bg-slate-100 px-2 py-1 rounded-md",
                                        ),
                                    ),
                                    class_name="flex flex-wrap gap-2 justify-center mt-4",
                                ),
                                class_name="text-center",
                            ),
                            rx.el.div(
                                rx.icon(
                                    "camera", class_name="h-16 w-16 text-slate-400"
                                ),
                                rx.el.p(
                                    "Camera preview placeholder",
                                    class_name="text-slate-500 mt-2",
                                ),
                                class_name="flex flex-col items-center justify-center h-full",
                            ),
                        ),
                    ),
                    class_name="w-full aspect-square bg-slate-200 rounded-lg flex items-center justify-center mb-4 relative",
                ),
                rx.cond(
                    AppState.selfie_avatar_preview_url != "",
                    rx.el.div(
                        rx.el.button(
                            "Looks Good!",
                            on_click=[AppState.confirm_avatar, AppState.next_step],
                            class_name="w-full bg-teal-600 text-white font-semibold py-3 rounded-md hover:bg-teal-700",
                        ),
                        rx.el.button(
                            "Try Again",
                            on_click=AppState.process_selfie,
                            class_name="w-full text-center text-slate-600 font-medium hover:underline mt-2",
                        ),
                        class_name="w-full",
                    ),
                    rx.el.div(
                        rx.el.button(
                            rx.icon("camera", class_name="mr-2"),
                            "Capture Selfie",
                            on_click=AppState.process_selfie,
                            class_name="w-full flex items-center justify-center bg-orange-600 text-white font-semibold py-3 rounded-md hover:bg-orange-700",
                        ),
                        rx.el.button(
                            "Cancel",
                            on_click=lambda: AppState.toggle_capture_selfie_mode(False),
                            class_name="w-full text-center text-slate-600 font-medium hover:underline mt-2",
                        ),
                        class_name="w-full",
                    ),
                ),
                rx.el.p(
                    "Your photo is processed locally and never stored.",
                    class_name="text-xs text-slate-400 text-center mt-4",
                ),
            ),
            rx.el.div(
                rx.el.image(
                    src=AppState.user_avatar_url,
                    class_name="h-24 w-24 rounded-full mx-auto mb-4 border-4 border-white shadow-md",
                ),
                rx.el.button(
                    "Or, use my initial instead",
                    on_click=AppState.next_step,
                    class_name="w-full text-center text-slate-600 font-medium hover:underline mt-2",
                ),
                rx.el.button(
                    rx.icon("camera", class_name="mr-2"),
                    "Create Custom Avatar",
                    on_click=lambda: AppState.toggle_capture_selfie_mode(True),
                    class_name="w-full flex items-center justify-center bg-slate-800 text-white font-semibold py-3 rounded-md hover:bg-slate-900",
                ),
                rx.el.button(
                    "Or, continue to next step",
                    on_click=AppState.next_step,
                    class_name="w-full text-center text-slate-600 font-medium hover:underline mt-2",
                ),
            ),
        ),
        class_name="p-6 bg-slate-50 border rounded-lg mb-8",
    )


def dad_card_step() -> rx.Component:
    return rx.el.div(
        rx.el.h2(
            "Create Your Dad Card", class_name="text-3xl font-bold text-slate-900 mb-4"
        ),
        rx.el.p(
            "This is how other dads will see you. Share as much as you're comfortable with.",
            class_name="text-slate-600 mb-8",
        ),
        selfie_capture_component(),
        rx.el.form(
            rx.el.div(
                rx.el.label("Your Name", class_name="font-semibold text-slate-700"),
                rx.el.input(
                    placeholder="e.g., Alex",
                    name="name",
                    class_name="w-full mt-1 p-2 border rounded-md",
                    default_value=AppState.user.name,
                ),
                class_name="mb-4",
            ),
            rx.el.div(
                rx.el.label("Location", class_name="font-semibold text-slate-700"),
                rx.el.input(
                    placeholder="e.g., Brooklyn, NY",
                    name="location",
                    class_name="w-full mt-1 p-2 border rounded-md",
                ),
                class_name="mb-4",
            ),
            rx.el.button(
                "Finish Setup",
                type="submit",
                class_name="w-full bg-slate-800 text-white font-semibold py-3 px-6 rounded-md hover:bg-slate-900 transition-all",
            ),
            on_submit=AppState.next_step,
        ),
    )


def done_step() -> rx.Component:
    return rx.el.div(
        rx.icon("party-popper", class_name="h-16 w-16 text-orange-500 mx-auto mb-4"),
        rx.el.h2(
            "You're all set!", class_name="text-3xl font-bold text-slate-900 mb-4"
        ),
        rx.el.p(
            "Start connecting with other dads and make some plans.",
            class_name="text-slate-600 mb-8",
        ),
        rx.el.a(
            "Go to Home",
            href="/home",
            class_name="w-full text-center bg-slate-800 text-white font-semibold py-3 px-6 rounded-md hover:bg-slate-900 transition-all",
        ),
    )


def onboarding_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            progress_indicator(),
            rx.el.div(
                rx.match(
                    AppState.onboarding_step,
                    (1, welcome_step()),
                    (2, calendar_step()),
                    (3, dad_card_step()),
                    (4, done_step()),
                    welcome_step(),
                ),
                class_name="w-full max-w-md p-8 bg-white rounded-lg shadow-lg border",
            ),
            class_name="flex flex-col items-center justify-center min-h-screen bg-cool-gray-50 font-['Poppins'] p-4",
        )
    )