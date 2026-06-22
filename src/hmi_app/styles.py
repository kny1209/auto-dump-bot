import customtkinter as ctk
import threading
import time

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


class FoodWasteGUI:

    def __init__(self):

        self.root = ctk.CTk()

        self.root.geometry("1000x650")
        self.root.title("음식물 처리 시스템")

        self.root.configure(
            fg_color="#d8c6ff"
        )

        self.home_button=None

        self.steps = [
            "통 파지",
            "배출 위치 이동",
            "음식물 배출",
            "세척 중",
            "초기 위치 복귀",
            "작업 완료"
        ]

        self.step_labels=[]

        self.create_ui()

        self.root.mainloop()



    def create_ui(self):

        for widget in self.root.winfo_children():
            widget.destroy()

        self.step_labels=[]

        title=ctk.CTkLabel(

            self.root,
            text="음식물 처리 시스템",
            font=("맑은 고딕",35,"bold")

        )

        title.pack(
            pady=(30,10)
        )


        subtitle=ctk.CTkLabel(

            self.root,
            text="작업 유형 선택",
            font=("맑은 고딕",18)

        )

        subtitle.pack()



        card=ctk.CTkFrame(

            self.root,

            width=800,
            height=180,

            fg_color="white",

            corner_radius=30

        )

        card.pack(
            pady=30
        )



        btn1=ctk.CTkButton(

            card,

            text="유형1\n일반 배출 + 세척",

            width=220,
            height=80,

            corner_radius=20,

            font=("맑은 고딕",16,"bold"),

            command=lambda:self.start(1)

        )

        btn1.place(
            x=120,
            y=50
        )



        btn2=ctk.CTkButton(

            card,

            text="유형2\n강한 흔들기 + 세척",

            width=220,
            height=80,

            fg_color="#ff5ba6",

            hover_color="#ff2f87",

            corner_radius=20,

            font=("맑은 고딕",16,"bold"),

            command=lambda:self.start(2)

        )

        btn2.place(
            x=450,
            y=50
        )



        self.status=ctk.CTkLabel(

            self.root,

            text="대기중",

            font=("맑은 고딕",30,"bold")

        )

        self.status.pack(
            pady=20
        )



        self.progress=ctk.CTkProgressBar(

            self.root,

            width=600,
            height=25

        )

        self.progress.pack()

        self.progress.set(0)



        # ========= 단계 표시 =========

        line_frame=ctk.CTkFrame(

            self.root,

            fg_color="transparent"

        )

        line_frame.pack(
            pady=50
        )


        for i,step in enumerate(self.steps):

            label=ctk.CTkLabel(

                line_frame,

                text=step,

                width=100,

                height=40,

                fg_color="#d9d9d9",

                corner_radius=15,

                text_color="black",

                font=("맑은 고딕",14,"bold")

            )

            label.pack(
                side="left",
                padx=5
            )

            self.step_labels.append(label)


            if i<len(self.steps)-1:

                arrow=ctk.CTkLabel(

                    line_frame,

                    text="➜",

                    font=("Arial",24)

                )

                arrow.pack(
                    side="left"
                )



    def start(self,mode):

        self.progress.set(0)

        thread=threading.Thread(

            target=self.run_process,
            args=(mode,)
        )

        thread.daemon=True
        thread.start()



    def run_process(self,mode):

        total=len(self.steps)

        for i,step in enumerate(self.steps):

            progress=(i+1)/total

            self.root.after(

                0,

                self.update_ui,

                i,
                step,
                progress
            )

            time.sleep(2)


        self.root.after(
            0,
            self.show_home_button
        )



    def update_ui(

        self,
        current,
        step,
        progress

    ):

        self.status.configure(
            text=step
        )

        self.progress.set(
            progress
        )


        for i,label in enumerate(self.step_labels):

            if i<current:

                label.configure(
                    fg_color="#47c47d"
                )

            elif i==current:

                label.configure(
                    fg_color="#ff5ba6"
                )

            else:

                label.configure(
                    fg_color="#d9d9d9"
                )



    def show_home_button(self):

        self.home_button=ctk.CTkButton(

            self.root,

            text="처음으로",

            width=180,
            height=55,

            font=("맑은 고딕",18,"bold"),

            fg_color="#47c47d",

            hover_color="#2da863",

            corner_radius=20,

            command=self.create_ui

        )

        self.home_button.pack(
            pady=20
        )


FoodWasteGUI()