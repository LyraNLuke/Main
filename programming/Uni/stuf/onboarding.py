import tkinter as tk
from tkinter import ttk, font

# ── Theme ──────────────────────────────────────────────────────────────────────
BG        = "#0f0f0f"
CARD      = "#1a1a2e"
ACCENT    = "#7c3aed"
ACCENT_HV = "#6d28d9"
TEXT      = "#f1f5f9"
SUBTEXT   = "#94a3b8"
BORDER    = "#2d2d44"
SEL_BG    = "#2e1065"
GREEN     = "#22c55e"
YELLOW    = "#eab308"
RED       = "#ef4444"

# ── Data ──────────────────────────────────────────────────────────────────────
OCCUPATIONS   = [("\U0001f393", "Student"), ("\U0001f4bc", "Employed"),
                 ("\U0001f4bb", "Freelancer"), ("\U0001f300", "Neither")]

LIFESTYLE_ENVS = [("\U0001f33f", "Outdoor based"), ("\U0001f3e2", "Office based"),
                  ("\U0001f4da", "Classroom based"), ("\U0001f3e0", "Home based")]

FOCUS_STYLES  = [("\U0001f3af", "Deep Focus",  "Long, uninterrupted productive sessions"),
                 ("\U0001f33f", "Light Focus", "Shorter windows spread across a longer period")]

PEAK_WINDOWS  = [("\U0001f305", "Early Bird",    "Before 9 AM"),
                 ("\u2600\ufe0f",  "Midday Driver", "9 AM \u2013 3 PM"),
                 ("\U0001f319", "Night Owl",     "After 8 PM"),
                 ("\U0001f550", "Custom",        "Pick specific time slots")]

TIME_SLOTS    = ["5\u20137 AM","7\u20139 AM","9\u201311 AM","11 AM\u20131 PM",
                 "1\u20133 PM","3\u20135 PM","5\u20137 PM","7\u20139 PM","9\u201311 PM"]

NOTIF_OPTIONS = [("\U0001f514",   "Light Touch", "Morning & evening only"),
                 ("\U0001f514\U0001f514",   "Medium",      "Morning, evening & task reminders"),
                 ("\U0001f514\U0001f514\U0001f514", "High", "All of the above + mid-task reminders")]

TONES         = ["Neutral", "Gentle", "Motivational", "Direct"]
PRIORITIES   = [("Low", GREEN), ("Medium", YELLOW), ("High", RED)]

STEP_TITLES   = ["Occupation", "Lifestyle", "Focus Style",
                 "Peak Window", "Communication", "Summary"]


# ── Helpers ────────────────────────────────────────────────────────────────────
class RoundedButton(tk.Canvas):
    def __init__(self, parent, text, command, bg=ACCENT, fg=TEXT,
                 width=160, height=40, radius=12, **kw):
        super().__init__(parent, width=width, height=height,
                         bg=parent["bg"] if isinstance(parent, tk.Widget) else BG,
                         highlightthickness=0, **kw)
        self.cmd = command
        self.r   = radius
        self.bg_color = bg
        self.fg_color = fg
        self.w, self.h = width, height
        self._draw(text)
        self.bind("<Button-1>", lambda e: self.cmd())
        self.bind("<Enter>",    lambda e: self._hover(True))
        self.bind("<Leave>",    lambda e: self._hover(False))

    def _draw(self, text):
        r = self.r
        self.delete("all")
        x1, y1, x2, y2 = 2, 2, self.w-2, self.h-2
        for dx, dy in [(0,0),(x2-2*r,0),(0,y2-2*r),(x2-2*r,y2-2*r)]:
            self.create_oval(x1+dx, y1+dy, x1+dx+2*r, y1+dy+2*r,
                             fill=self.bg_color, outline="")
        self.create_rectangle(x1+r, y1, x2-r, y2, fill=self.bg_color, outline="")
        self.create_rectangle(x1, y1+r, x2, y2-r, fill=self.bg_color, outline="")
        self.create_text(self.w//2, self.h//2, text=text,
                         fill=self.fg_color, font=("Segoe UI", 10, "bold"))
        self._text = text

    def _hover(self, on):
        self.bg_color = ACCENT_HV if on else ACCENT
        self._draw(self._text)

    def configure_text(self, text):
        self._draw(text)


def make_card(parent, pady=6):
    f = tk.Frame(parent, bg=CARD, relief="flat")
    f.pack(fill="x", pady=pady, padx=4)
    return f


def label(parent, text, size=11, color=TEXT, bold=False, anchor="w"):
    w = tk.fontsize = size
    style = "bold" if bold else "normal"
    return tk.Label(parent, text=text, bg=parent["bg"],
                    fg=color, font=("Segoe UI", size, style), anchor=anchor)


# ── Main App ──────────────────────────────────────────────────────────────────
class OnboardingApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Onboarding")
        self.geometry("520x700")
        self.configure(bg=BG)
        self.resizable(False, False)

        # State
        self.step       = 0
        self.occupation = tk.StringVar()
        self.lifestyle  = {e[1]: tk.IntVar(value=5) for e in LIFESTYLE_ENVS}
        self.focus      = tk.StringVar()
        self.peak       = tk.StringVar()
        self.slots      = set()
        self.notif      = tk.StringVar()
        self.tones      = {p: tk.StringVar(value="Neutral") for p, _ in PRIORITIES}
        self.display    = tk.StringVar(value="Standard")

        self._build_shell()
        self._render_step()

    # ── Shell ──────────────────────────────────────────────────────────────────
    def _build_shell(self):
        # Top bar
        top = tk.Frame(self, bg=BG)
        top.pack(fill="x", padx=24, pady=(20, 0))
        self.step_lbl = tk.Label(top, text="", bg=BG, fg=SUBTEXT,
                                 font=("Segoe UI", 9))
        self.step_lbl.pack(side="left")
        self.pct_lbl  = tk.Label(top, text="", bg=BG, fg=SUBTEXT,
                                 font=("Segoe UI", 9))
        self.pct_lbl.pack(side="right")

        # Progress bar
        pb_frame = tk.Frame(self, bg=BG)
        pb_frame.pack(fill="x", padx=24, pady=(4, 16))
        self.pb_track = tk.Canvas(pb_frame, height=6, bg="#2d2d44",
                                  highlightthickness=0)
        self.pb_track.pack(fill="x")
        self.pb_fill  = self.pb_track.create_rectangle(0, 0, 0, 6,
                                                       fill=ACCENT, width=0)

        # Scrollable content area
        container = tk.Frame(self, bg=BG)
        container.pack(fill="both", expand=True, padx=24)

        canvas = tk.Canvas(container, bg=BG, highlightthickness=0)
        scroll = ttk.Scrollbar(container, orient="vertical",
                               command=canvas.yview)
        self.content = tk.Frame(canvas, bg=BG)
        self.content.bind("<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=self.content, anchor="nw")
        canvas.configure(yscrollcommand=scroll.set)
        canvas.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")
        canvas.bind_all("<MouseWheel>",
            lambda e: canvas.yview_scroll(-1*(e.delta//120), "units"))

        # Bottom nav
        nav = tk.Frame(self, bg=BG)
        nav.pack(fill="x", padx=24, pady=(8, 20))
        self.back_btn = RoundedButton(nav, "\u2190  Back", self._back,
                                      bg="#1e1e2e", fg=SUBTEXT, width=110, height=40)
        self.next_btn = RoundedButton(nav, "Next  \u2192", self._next,
                                      width=140, height=40)
        self.back_btn.pack(side="left")
        self.next_btn.pack(side="right")

    def _update_progress(self):
        total = len(STEP_TITLES) - 1
        pct   = int((self.step / total) * 100)
        self.step_lbl.config(text=f"Step {self.step+1} of {total}  \u2014  {STEP_TITLES[self.step]}")
        self.pct_lbl.config(text=f"{pct}%")
        self.pb_track.update_idletasks()
        w = self.pb_track.winfo_width()
        self.pb_track.coords(self.pb_fill, 0, 0, int(w * pct / 100), 6)
        # Back button visibility
        if self.step == 0:
            self.back_btn.configure(state="disabled")
        else:
            self.back_btn.configure(state="normal")

    def _clear_content(self):
        for w in self.content.winfo_children():
            w.destroy()

    def _render_step(self):
        self._clear_content()
        self._update_progress()
        steps = [self._step_occupation, self._step_lifestyle,
                 self._step_focus, self._step_peak,
                 self._step_communication, self._step_summary]
        steps[self.step]()

    # ── Navigation ────────────────────────────────────────────────────────────
    def _can_next(self):
        if self.step == 0: return bool(self.occupation.get())
        if self.step == 1: return True
        if self.step == 2: return bool(self.focus.get())
        if self.step == 3:
            return bool(self.peak.get()) and \
                   (self.peak.get() != "Custom" or len(self.slots) > 0)
        if self.step == 4: return bool(self.notif.get())
        return True

    def _next(self):
        if not self._can_next():
            self._flash_error()
            return
        self.step = min(self.step + 1, len(STEP_TITLES) - 1)
        self._render_step()

    def _back(self):
        self.step = max(self.step - 1, 0)
        self._render_step()

    def _flash_error(self):
        orig = self.next_btn.bg_color
        self.next_btn.bg_color = RED
        self.next_btn._draw(self.next_btn._text)
        self.after(500, lambda: (setattr(self.next_btn, 'bg_color', orig),
                                 self.next_btn._draw(self.next_btn._text)))

    # ── Step Builders ─────────────────────────────────────────────────────────
    def _section_header(self, title, subtitle):
        tk.Label(self.content, text=title, bg=BG, fg=TEXT,
                 font=("Segoe UI", 16, "bold"), anchor="w").pack(fill="x", pady=(4, 0))
        tk.Label(self.content, text=subtitle, bg=BG, fg=SUBTEXT,
                 font=("Segoe UI", 10), anchor="w").pack(fill="x", pady=(2, 14))

    def _option_card(self, parent, icon, label_text, desc, var, value, multi=False):
        frame = tk.Frame(parent, bg=CARD, cursor="hand2")
        frame.pack(fill="x", pady=4)

        def toggle():
            if multi:
                if value in self.slots: self.slots.discard(value)
                else:                   self.slots.add(value)
                _refresh()
            else:
                var.set(value)
                _refresh_all()

        def _is_selected():
            return value in self.slots if multi else var.get() == value

        def _refresh():
            sel = _is_selected()
            frame.config(bg=SEL_BG if sel else CARD)
            for child in frame.winfo_children():
                _set_bg(child, SEL_BG if sel else CARD)
            chk.config(text="\u2713" if sel else "",
                       fg=ACCENT if sel else CARD)

        def _refresh_all():
            _refresh()

        def _set_bg(w, color):
            try:    w.config(bg=color)
            except: pass
            for c in w.winfo_children():
                _set_bg(c, color)

        inner = tk.Frame(frame, bg=CARD, padx=12, pady=10)
        inner.pack(fill="x")
        tk.Label(inner, text=icon, bg=CARD, font=("Segoe UI", 18)).pack(side="left")
        txt_f = tk.Frame(inner, bg=CARD)
        txt_f.pack(side="left", padx=10, fill="x", expand=True)
        tk.Label(txt_f, text=label_text, bg=CARD, fg=TEXT,
                 font=("Segoe UI", 11, "bold"), anchor="w").pack(fill="x")
        if desc:
            tk.Label(txt_f, text=desc, bg=CARD, fg=SUBTEXT,
                     font=("Segoe UI", 9), anchor="w").pack(fill="x")
        chk = tk.Label(inner, text="", bg=CARD, fg=ACCENT,
                       font=("Segoe UI", 14, "bold"), width=2)
        chk.pack(side="right")

        for w in [frame, inner, txt_f] + inner.winfo_children() + txt_f.winfo_children():
            try: w.bind("<Button-1>", lambda e: toggle())
            except: pass

        _refresh()
        return _refresh

    def _step_occupation(self):
        self._section_header("What's your occupation?",
                             "This helps us understand your daily structure.")
        refreshers = []
        for icon, lbl in OCCUPATIONS:
            r = self._option_card(self.content, icon, lbl, "",
                                  self.occupation, lbl)
            refreshers.append(r)

        def refresh_all(*_):
            for r in refreshers: r()
        self.occupation.trace_add("write", refresh_all)

    def _step_lifestyle(self):
        self._section_header("Rate your lifestyle environments",
                             "On a scale of 1\u201310, how much does each apply to you?")
        for icon, env in LIFESTYLE_ENVS:
            card = make_card(self.content)
            top  = tk.Frame(card, bg=CARD, padx=12, pady=8)
            top.pack(fill="x")
            tk.Label(top, text=f"{icon}  {env}", bg=CARD, fg=TEXT,
                     font=("Segoe UI", 11, "bold")).pack(side="left")
            val_lbl = tk.Label(top, text=str(self.lifestyle[env].get()),
                               bg=CARD, fg=ACCENT, font=("Segoe UI", 11, "bold"), width=3)
            val_lbl.pack(side="right")

            def make_cmd(e=env, lbl=val_lbl):
                def cmd(v):
                    lbl.config(text=str(int(float(v))))
                return cmd

            slider = ttk.Scale(card, from_=1, to=10, orient="horizontal",
                               variable=self.lifestyle[env], command=make_cmd())
            slider.pack(fill="x", padx=12, pady=(0, 10))

    def _step_focus(self):
        self._section_header("How do you focus best?",
                             "Choose the style that matches how you work.")
        refreshers = []
        for icon, lbl, desc in FOCUS_STYLES:
            r = self._option_card(self.content, icon, lbl, desc, self.focus, lbl)
            refreshers.append(r)

        def refresh_all(*_):
            for r in refreshers: r()
        self.focus.trace_add("write", refresh_all)

    def _step_peak(self):
        self._section_header("When are you most productive?",
                             "Pick a general window or choose specific time slots.")
        refreshers = []
        slots_frame = [None]

        def build_slots():
            if slots_frame[0]:
                slots_frame[0].destroy()
            if self.peak.get() != "Custom":
                return
            sf = tk.Frame(self.content, bg=BG)
            sf.pack(fill="x", pady=(4, 0))
            slots_frame[0] = sf
            tk.Label(sf, text="Select your time slots:", bg=BG, fg=SUBTEXT,
                     font=("Segoe UI", 9, "bold")).pack(anchor="w", pady=(0, 6))
            grid = tk.Frame(sf, bg=BG)
            grid.pack(fill="x")
            slot_refreshers = []
            for i, slot in enumerate(TIME_SLOTS):
                btn_frame = tk.Frame(grid, bg=CARD, cursor="hand2")
                btn_frame.grid(row=i//3, column=i%3, padx=4, pady=4, sticky="ew")
                grid.columnconfigure(i%3, weight=1)
                lbl_w = tk.Label(btn_frame, text=slot, bg=CARD, fg=SUBTEXT,
                                 font=("Segoe UI", 9), pady=6)
                lbl_w.pack(fill="x")

                def make_toggle(s=slot, b=btn_frame, l=lbl_w):
                    def toggle(e=None):
                        if s in self.slots: self.slots.discard(s)
                        else:               self.slots.add(s)
                        sel = s in self.slots
                        b.config(bg=SEL_BG if sel else CARD)
                        l.config(bg=SEL_BG if sel else CARD,
                                 fg=ACCENT if sel else SUBTEXT)
                    return toggle
                t = make_toggle()
                btn_frame.bind("<Button-1>", t)
                lbl_w.bind("<Button-1>", t)

        for icon, lbl, desc in PEAK_WINDOWS:
            def make_refresh_all(rlist):
                def ra(*_):
                    for r in rlist: r()
                    build_slots()
                return ra
            r = self._option_card(self.content, icon, lbl, desc, self.peak, lbl)
            refreshers.append(r)

        def refresh_all(*_):
            for r in refreshers: r()
            build_slots()
        self.peak.trace_add("write", refresh_all)

    def _step_communication(self):
        self._section_header("Communication Preferences",
                             "Customize how and when we reach you.")

        # 1. Notification Frequency
        tk.Label(self.content, text="1.  Notification Frequency", bg=BG, fg=TEXT,
                 font=("Segoe UI", 11, "bold"), anchor="w").pack(fill="x", pady=(0, 6))
        notif_refreshers = []
        for icon, lbl, desc in NOTIF_OPTIONS:
            r = self._option_card(self.content, icon, lbl, desc, self.notif, lbl)
            notif_refreshers.append(r)
        def refresh_notif(*_):
            for r in notif_refreshers: r()
        self.notif.trace_add("write", refresh_notif)

        # 2. Tone per priority
        tk.Label(self.content, text="2.  Tone by Task Priority", bg=BG, fg=TEXT,
                 font=("Segoe UI", 11, "bold"), anchor="w").pack(fill="x", pady=(16, 6))

        for priority, color in PRIORITIES:
            card = make_card(self.content, pady=4)
            hdr  = tk.Frame(card, bg=CARD, padx=12, pady=8)
            hdr.pack(fill="x")
            tk.Label(hdr, text=f"{priority} Priority", bg=CARD, fg=color,
                     font=("Segoe UI", 9, "bold")).pack(anchor="w")
            btn_row = tk.Frame(card, bg=CARD, padx=12, pady=(0, 10))
            btn_row.pack(fill="x")

            def build_tone_row(p=priority, tv=self.tones[priority], row=btn_row):
                btns = {}
                for tone in TONES:
                    b = tk.Label(row, text=tone, bg="#2d2d44", fg=SUBTEXT,
                                 font=("Segoe UI", 9, "bold"), padx=10, pady=5,
                                 cursor="hand2")
                    b.pack(side="left", padx=4)
                    btns[tone] = b

                def refresh(*_):
                    for val, b in btns.items():
                        sel = val == tv.get()
                        b.config(bg=ACCENT if sel else "#2d2d44",
                                 fg=TEXT if sel else SUBTEXT)

                for tone, b in btns.items():
                    b.bind("<Button-1>",
                           lambda e, t=tone: (tv.set(t), refresh()))

                tv.trace_add("write", lambda *_: refresh())
                refresh()

            build_tone_row()

        # 3. Display mode
        tk.Label(self.content, text="3.  Display Mode", bg=BG, fg=TEXT,
                 font=("Segoe UI", 11, "bold"), anchor="w").pack(fill="x", pady=(16, 6))
        dm_frame = tk.Frame(self.content, bg=BG)
        dm_frame.pack(fill="x")
        dm_btns  = {}
        for mode, icon in [("Standard", "\u2600\ufe0f"), ("Dark", "\U0001f319")]:
            b = tk.Label(dm_frame, text=f"{icon}  {mode}", bg=CARD, fg=SUBTEXT,
                         font=("Segoe UI", 10, "bold"), padx=16, pady=10,
                         cursor="hand2", width=14)
            b.pack(side="left", padx=6)
            dm_btns[mode] = b

        def refresh_dm(*_):
            for m, b in dm_btns.items():
                sel = self.display.get() == m
                b.config(bg=SEL_BG if sel else CARD,
                         fg=ACCENT if sel else SUBTEXT)
        for mode, b in dm_btns.items():
            b.bind("<Button-1>",
                   lambda e, m=mode: (self.display.set(m), refresh_dm()))
        refresh_dm()

    def _step_summary(self):
        self.next_btn._draw("Restart")
        self.next_btn.cmd = self._restart
        self.back_btn.pack_forget()

        tk.Label(self.content, text="\U0001f389", bg=BG,
                 font=("Segoe UI", 36)).pack(pady=(8, 0))
        tk.Label(self.content, text="You're all set!", bg=BG, fg=TEXT,
                 font=("Segoe UI", 18, "bold")).pack()
        tk.Label(self.content, text="Here's your profile summary.", bg=BG, fg=SUBTEXT,
                 font=("Segoe UI", 10)).pack(pady=(2, 16))

        def row(label_text, value):
            f = make_card(self.content, pady=3)
            inner = tk.Frame(f, bg=CARD, padx=12, pady=8)
            inner.pack(fill="x")
            tk.Label(inner, text=label_text.upper(), bg=CARD, fg=SUBTEXT,
                     font=("Segoe UI", 8, "bold")).pack(side="left")
            tk.Label(inner, text=value, bg=CARD, fg=TEXT,
                     font=("Segoe UI", 10, "bold")).pack(side="right")

        row("Occupation", self.occupation.get())
        row("Focus Style", self.focus.get())
        peak_val = self.peak.get()
        if self.slots:
            peak_val += " (" + ", ".join(sorted(self.slots)) + ")"
        row("Peak Window", peak_val)
        row("Notifications", self.notif.get())
        row("Display Mode", self.display.get())

        # Lifestyle bars
        life_card = make_card(self.content, pady=3)
        tk.Label(life_card, text="LIFESTYLE", bg=CARD, fg=SUBTEXT,
                 font=("Segoe UI", 8, "bold"), padx=12).pack(anchor="w", pady=(8, 4))
        for icon, env in LIFESTYLE_ENVS:
            row_f = tk.Frame(life_card, bg=CARD, padx=12)
            row_f.pack(fill="x", pady=3)
            tk.Label(row_f, text=f"{icon} {env}", bg=CARD, fg=TEXT,
                     font=("Segoe UI", 9), width=20, anchor="w").pack(side="left")
            val = self.lifestyle[env].get()
            track = tk.Canvas(row_f, height=6, bg="#2d2d44", highlightthickness=0)
            track.pack(side="left", fill="x", expand=True, padx=8)
            track.update_idletasks()
            w = track.winfo_width() or 160
            track.create_rectangle(0, 0, int(w * val / 10), 6, fill=ACCENT, width=0)
            tk.Label(row_f, text=str(val), bg=CARD, fg=ACCENT,
                     font=("Segoe UI", 9, "bold"), width=3).pack(side="right")
        tk.Frame(life_card, bg=CARD, height=8).pack()

        # Tones
        tone_card = make_card(self.content, pady=3)
        tk.Label(tone_card, text="TONES", bg=CARD, fg=SUBTEXT,
                 font=("Segoe UI", 8, "bold"), padx=12).pack(anchor="w", pady=(8, 4))
        for priority, color in PRIORITIES:
            row_f = tk.Frame(tone_card, bg=CARD, padx=12)
            row_f.pack(fill="x", pady=3)
            tk.Label(row_f, text=priority, bg=CARD, fg=color,
                     font=("Segoe UI", 9, "bold"), width=8, anchor="w").pack(side="left")
            tk.Label(row_f, text=self.tones[priority].get(), bg=CARD, fg=TEXT,
                     font=("Segoe UI", 9)).pack(side="right")
        tk.Frame(tone_card, bg=CARD, height=8).pack()

    def _restart(self):
        self.occupation.set("")
        for v in self.lifestyle.values(): v.set(5)
        self.focus.set("")
        self.peak.set("")
        self.slots.clear()
        self.notif.set("")
        for v in self.tones.values(): v.set("Neutral")
        self.display.set("Standard")
        self.step = 0
        self.back_btn.pack(side="left")
        self.next_btn._draw("Next  \u2192")
        self.next_btn.cmd = self._next
        self._render_step()


if __name__ == "__main__":
    app = OnboardingApp()
    app.mainloop()
