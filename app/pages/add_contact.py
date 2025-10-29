import reflex as rx
from app.state.state import AppState


def qr_scanner_overlay() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.button(
                rx.icon("x", class_name="h-6 w-6"),
                on_click=AppState.toggle_qr_scanner,
                class_name="absolute top-4 right-4 text-white bg-black/50 rounded-full p-2 z-10",
            ),
            rx.el.div(
                rx.el.div(
                    rx.icon("camera", class_name="h-32 w-32 text-gray-400"),
                    class_name="w-full max-w-sm aspect-square bg-gray-900 rounded-lg flex items-center justify-center",
                ),
                rx.el.p(
                    "Scanning for a Papa Connect QR code...",
                    class_name="text-white mt-4 font-medium",
                ),
                rx.el.button(
                    "Simulate Successful Scan",
                    on_click=lambda: AppState.on_qr_scan(
                        {"name": "Scanned Dad", "email": "scanned.dad@example.com"}
                    ),
                    class_name="mt-4 bg-amber-500 text-white font-semibold py-2 px-4 rounded-lg hover:bg-amber-600",
                ),
            ),
        ),
        class_name="fixed inset-0 bg-black/80 flex flex-col items-center justify-center z-50",
    )


def add_contact_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.a(
                rx.icon("arrow-left", class_name="h-5 w-5 mr-2"),
                "Back to Home",
                href="/home",
                class_name="flex items-center font-semibold text-slate-800 hover:underline mb-8",
            ),
            rx.cond(
                AppState.contact_added_success,
                rx.el.div(
                    rx.icon(
                        "check_check", class_name="h-16 w-16 text-teal-500 mx-auto mb-4"
                    ),
                    rx.el.h2(
                        "Contact Added!",
                        class_name="text-2xl font-bold text-center text-slate-800",
                    ),
                    rx.el.p(
                        "Redirecting you back to your home page...",
                        class_name="text-center text-slate-500 mt-2",
                    ),
                    class_name="p-8 bg-white rounded-lg shadow-lg border w-full max-w-md",
                ),
                rx.el.div(
                    rx.el.h1(
                        "Add a New Contact",
                        class_name="text-3xl font-bold text-slate-900 mb-2",
                    ),
                    rx.el.p(
                        "Manually add a new dad to your network.",
                        class_name="text-slate-500 mb-8",
                    ),
                    rx.el.div(
                        rx.el.div(
                            rx.el.button(
                                rx.el.image(
                                    src=AppState.qr_code_url,
                                    class_name="h-24 w-24 p-2 bg-white rounded-md",
                                ),
                                rx.el.p(
                                    "Show My QR Code",
                                    class_name="font-semibold mt-2 text-slate-800",
                                ),
                                on_click=AppState.generate_qr_code,
                                class_name="flex flex-col items-center justify-center p-4 bg-slate-100 rounded-md border border-slate-200 w-full text-slate-700 hover:bg-slate-200 transition-all",
                            ),
                            rx.el.button(
                                rx.icon(
                                    "scan-line", class_name="h-12 w-12 text-slate-800"
                                ),
                                rx.el.p(
                                    "Scan a Code",
                                    class_name="font-semibold mt-2 text-slate-800",
                                ),
                                on_click=AppState.toggle_qr_scanner,
                                class_name="flex flex-col items-center justify-center p-4 bg-slate-100 rounded-md border border-slate-200 w-full text-slate-700 hover:bg-slate-200 transition-all",
                            ),
                            class_name="grid grid-cols-2 gap-4 mb-4",
                        ),
                        rx.el.button(
                            rx.icon("credit_card", class_name="h-8 w-8 text-white"),
                            rx.el.span(
                                "Simulate NFC Tap", class_name="font-semibold text-lg"
                            ),
                            on_click=AppState.simulate_nfc_tap,
                            class_name="w-full flex items-center justify-center gap-3 p-4 bg-slate-600 text-white rounded-md hover:bg-slate-700 transition-all mb-8 shadow-sm",
                        ),
                        rx.cond(AppState.is_scanning_qr, qr_scanner_overlay(), None),
                    ),
                    rx.el.form(
                        rx.el.div(
                            rx.el.label(
                                "Name", class_name="font-semibold text-slate-700"
                            ),
                            rx.el.input(
                                placeholder="John Doe",
                                name="name",
                                required=True,
                                class_name="w-full mt-1 p-2 border rounded-md",
                            ),
                            class_name="mb-4",
                        ),
                        rx.el.div(
                            rx.el.label(
                                "Email (Optional)",
                                class_name="font-semibold text-slate-700",
                            ),
                            rx.el.input(
                                placeholder="john@example.com",
                                name="email",
                                type="email",
                                class_name="w-full mt-1 p-2 border rounded-md",
                            ),
                            class_name="mb-4",
                        ),
                        rx.el.div(
                            rx.el.label(
                                "Phone (Optional)",
                                class_name="font-semibold text-slate-700",
                            ),
                            rx.el.input(
                                placeholder="+1234567890",
                                name="phone",
                                class_name="w-full mt-1 p-2 border rounded-md",
                            ),
                            class_name="mb-6",
                        ),
                        rx.el.button(
                            "Add Contact",
                            type="submit",
                            class_name="w-full bg-slate-800 text-white font-semibold py-3 px-6 rounded-md hover:bg-slate-900 transition-all",
                        ),
                        on_submit=AppState.add_contact,
                    ),
                    class_name="p-8 bg-white rounded-lg shadow-lg border w-full max-w-md",
                ),
            ),
        ),
        class_name="flex items-center justify-center min-h-screen bg-cool-gray-50 font-['Poppins'] p-4",
    )