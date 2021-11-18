import tkinter as tk
import tkinter.font as tkFont
import tkinter.messagebox

import main


class TkinterWindow:
    def __init__(self, root):
        # setting title
        root.title("pytorch abstract art generation")
        # setting window size
        width = 600
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.verbose_value = tk.BooleanVar()
        GCheckBox_759 = tk.Checkbutton(root, variable=self.verbose_value)
        ft = tkFont.Font(family='Times', size=10)
        GCheckBox_759["font"] = ft
        GCheckBox_759["fg"] = "#000000"
        GCheckBox_759["justify"] = "center"
        GCheckBox_759["text"] = "Verbose"
        GCheckBox_759.place(x=160, y=450, width=74, height=30)
        GCheckBox_759["offvalue"] = "0"
        GCheckBox_759["onvalue"] = "1"
        GCheckBox_759["command"] = self.GCheckBox_759_command

        GButton_152 = tk.Button(root)
        GButton_152["bg"] = "#181a1b"
        ft = tkFont.Font(family='Times', size=10)
        GButton_152["font"] = ft
        GButton_152["fg"] = "#e8e6e3"
        GButton_152["justify"] = "center"
        GButton_152["text"] = "Render"
        GButton_152.place(x=240, y=450, width=120, height=30)
        GButton_152["command"] = self.GButton_152_command

        self.color_value = tk.BooleanVar()
        GCheckBox_963 = tk.Checkbutton(root, variable=self.color_value)
        ft = tkFont.Font(family='Times', size=10)
        GCheckBox_963["font"] = ft
        GCheckBox_963["fg"] = "#000000"
        GCheckBox_963["justify"] = "center"
        GCheckBox_963["text"] = "Colour"
        GCheckBox_963.place(x=20, y=20, width=70, height=25)
        GCheckBox_963["offvalue"] = "0"
        GCheckBox_963["onvalue"] = "1"
        GCheckBox_963["command"] = self.GCheckBox_963_command

        GMessage_863 = tk.Message(root)
        ft = tkFont.Font(family='Times', size=10)
        GMessage_863["font"] = ft
        GMessage_863["fg"] = "#000000"
        GMessage_863["justify"] = "center"
        GMessage_863["text"] = "Seed:"
        GMessage_863.place(x=0, y=60, width=54, height=30)

        self.radius_value = tk.BooleanVar()
        GCheckBox_56 = tk.Checkbutton(root, variable=self.radius_value)
        ft = tkFont.Font(family='Times', size=10)
        GCheckBox_56["font"] = ft
        GCheckBox_56["fg"] = "#000000"
        GCheckBox_56["justify"] = "center"
        GCheckBox_56["text"] = "Radius"
        GCheckBox_56.place(x=20, y=110, width=70, height=25)
        GCheckBox_56["offvalue"] = "0"
        GCheckBox_56["onvalue"] = "1"
        GCheckBox_56["command"] = self.GCheckBox_56_command

        self.bias_value = tk.BooleanVar()
        GCheckBox_699 = tk.Checkbutton(root, variable=self.bias_value)
        ft = tkFont.Font(family='Times', size=10)
        GCheckBox_699["font"] = ft
        GCheckBox_699["fg"] = "#000000"
        GCheckBox_699["justify"] = "center"
        GCheckBox_699["text"] = "Bias"
        GCheckBox_699.place(x=10, y=160, width=75, height=30)
        GCheckBox_699["offvalue"] = "0"
        GCheckBox_699["onvalue"] = "1"
        GCheckBox_699["command"] = self.GCheckBox_699_command

        self.GLineEdit_53 = tk.Entry(root)
        self.GLineEdit_53["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.GLineEdit_53["font"] = ft
        self.GLineEdit_53["fg"] = "#000000"
        self.GLineEdit_53["justify"] = "center"
        self.GLineEdit_53["text"] = "100"
        self.GLineEdit_53.place(x=50, y=60, width=70, height=25)

        GMessage_485 = tk.Message(root)
        ft = tkFont.Font(family='Times', size=10)
        GMessage_485["font"] = ft
        GMessage_485["fg"] = "#000000"
        GMessage_485["justify"] = "center"
        GMessage_485["text"] = "z:"
        GMessage_485.place(x=0, y=200, width=55, height=30)

        self.GLineEdit_944 = tk.Entry(root)
        self.GLineEdit_944["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.GLineEdit_944["font"] = ft
        self.GLineEdit_944["fg"] = "#000000"
        self.GLineEdit_944["justify"] = "center"
        self.GLineEdit_944["text"] = "[1., -1.], [1., -1.]"
        self.GLineEdit_944.place(x=40, y=200, width=99, height=30)

        GMessage_302 = tk.Message(root)
        ft = tkFont.Font(family='Times', size=10)
        GMessage_302["font"] = ft
        GMessage_302["fg"] = "#000000"
        GMessage_302["justify"] = "center"
        GMessage_302["text"] = "frames: "
        GMessage_302.place(x=0, y=250, width=49, height=30)

        self.GLineEdit_403 = tk.Entry(root)
        self.GLineEdit_403["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.GLineEdit_403["font"] = ft
        self.GLineEdit_403["fg"] = "#000000"
        self.GLineEdit_403["justify"] = "center"
        self.GLineEdit_403["text"] = "[-1.0, 1.0]"
        self.GLineEdit_403.place(x=50, y=250, width=70, height=25)

        GMessage_643 = tk.Message(root)
        ft = tkFont.Font(family='Times', size=10)
        GMessage_643["font"] = ft
        GMessage_643["fg"] = "#000000"
        GMessage_643["justify"] = "center"
        GMessage_643["text"] = "xres:"
        GMessage_643.place(x=10, y=300, width=30, height=30)

        self.GLineEdit_14 = tk.Entry(root)
        self.GLineEdit_14["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.GLineEdit_14["font"] = ft
        self.GLineEdit_14["fg"] = "#000000"
        self.GLineEdit_14["justify"] = "center"
        self.GLineEdit_14["text"] = "2048"
        self.GLineEdit_14.place(x=50, y=300, width=70, height=25)

        GMessage_954 = tk.Message(root)
        ft = tkFont.Font(family='Times', size=10)
        GMessage_954["font"] = ft
        GMessage_954["fg"] = "#000000"
        GMessage_954["justify"] = "center"
        GMessage_954["text"] = "Depth:"
        GMessage_954.place(x=0, y=350, width=46, height=30)

        self.GLineEdit_345 = tk.Entry(root)
        self.GLineEdit_345["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.GLineEdit_345["font"] = ft
        self.GLineEdit_345["fg"] = "#000000"
        self.GLineEdit_345["justify"] = "center"
        self.GLineEdit_345["text"] = "8"
        self.GLineEdit_345.place(x=50, y=350, width=70, height=25)

        GMessage_656 = tk.Message(root)
        ft = tkFont.Font(family='Times', size=10)
        GMessage_656["font"] = ft
        GMessage_656["fg"] = "#000000"
        GMessage_656["justify"] = "center"
        GMessage_656["text"] = "Image Name:"
        GMessage_656.place(x=0, y=400, width=80, height=25)

        self.GLineEdit_370 = tk.Entry(root)
        self.GLineEdit_370["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.GLineEdit_370["font"] = ft
        self.GLineEdit_370["fg"] = "#000000"
        self.GLineEdit_370["justify"] = "center"
        self.GLineEdit_370["text"] = "test"
        self.GLineEdit_370.place(x=80, y=400, width=70, height=25)

    def GCheckBox_759_command(self):
        print("Verbose")
        main.ArtMoment.verbose = self.verbose_value.get()
        print(main.ArtMoment.verbose)

    def GButton_152_command(self):
        # put all values to default first

        main.ArtMoment.seed = 10000
        main.ArtMoment.z = None
        main.ArtMoment.xres = 2048
        main.ArtMoment.depth = 8

        temp_seed = 0
        entry_string = self.GLineEdit_53.get()
        if entry_string is not None and len(entry_string) >= 1 \
                and entry_string.isdigit():
            temp_seed = int(entry_string)

        if not entry_string.isdigit() and entry_string is not None and 1 <= len(entry_string) <= 10:
            print('Seed is a string, that should be an int my guy')
            tk.messagebox.showwarning('Invalid Input', 'Seed input is supposed to be an integer not '
                                                       'greater than 10 digits long.')
            return

        if temp_seed == 0:
            main.ArtMoment.seed = None
        else:
            main.ArtMoment.seed = temp_seed

        main.ArtMoment.image_name_to_save = self.GLineEdit_370.get() + ".png"

        if self.GLineEdit_944.get() is not None and len(self.GLineEdit_944.get()) >= 1 \
                and self.GLineEdit_944.get().isdigit():
            main.ArtMoment.z = float(self.GLineEdit_944.get())

        # main.ArtMoment.xlim =

        if self.GLineEdit_14.get() is not None and len(self.GLineEdit_14.get()) >= 1 \
                and self.GLineEdit_14.get().isdigit():
            if int(self.GLineEdit_14.get()) == 1024 \
                    or int(self.GLineEdit_14.get()) == 2048 or int(self.GLineEdit_14.get()) == 4096:
                main.ArtMoment.xres = int(self.GLineEdit_14.get())

        if self.GLineEdit_345.get() is not None and len(self.GLineEdit_345.get()) >= 1 \
                and self.GLineEdit_345.get().isdigit():
            main.ArtMoment.depth = int(self.GLineEdit_345.get())

        if main.ArtMoment.verbose:
            print('Render')
            print(main.ArtMoment.seed)
            print(main.ArtMoment.image_name_to_save)
            print(main.ArtMoment.z)
            print(main.ArtMoment.depth)
            print(main.ArtMoment.xres)

        if self.GLineEdit_403.get() is not None and len(self.GLineEdit_403.get()) >= 1 \
                and self.GLineEdit_403.get().isdigit():

            frames = int(self.GLineEdit_403.get())
            if frames is None or len(self.GLineEdit_403.get()) <= 0:
                main.main_render()

            else:
                for frame in range(frames):
                    print(f'Rendering frame {frame}')
                    main.ArtMoment.seed += 1
                    main.ArtMoment.image_name_to_save = "frames/" + str(frame) + ".png"
                    main.main_render()
                main.make_gif(main.ArtMoment.verbose)
        else:
            main.main_render()

    def GCheckBox_963_command(self):
        value = self.color_value.get()
        if value:
            main.ArtMoment.channels = 3
        else:
            main.ArtMoment.channels = 1

        if main.ArtMoment.verbose:
            print("Color")
            print(main.ArtMoment.channels)

    def GCheckBox_56_command(self):
        main.ArtMoment.radius = self.radius_value.get()
        if main.ArtMoment.verbose:
            print("Radius")
            print(main.ArtMoment.radius)

    def GCheckBox_699_command(self):
        print("Bias")
        main.ArtMoment.bias = self.bias_value.get()
        print(main.ArtMoment.bias)


if __name__ == "__main__":
    root = tk.Tk()
    root.iconbitmap('icon.ico')
    app = TkinterWindow(root)
    root.mainloop()
