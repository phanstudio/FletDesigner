import flet as ft
import json


class Parser:
    def __init__(self, jsonfilepath=None):
        if jsonfilepath:
            with open(jsonfilepath) as f:
                self.json = json.load(f)
        self.keys = {}

    def parse(self):
        for item in self.json:
            for key, val in item.items():
                if val["type"] == "Container":
                    self.keys[f"{key}"] = ft.Container()
                    # Update the properties of self.c1
                    self.keys[f"{key}"].width = val["width"]
                    self.keys[f"{key}"].height = val["height"]
                    self.keys[f"{key}"].bgcolor = val["bgcolor"]
                    self.keys[f"{key}"].opacity = val["opacity"]
                    self.keys[f"{key}"].border_radius = ft.border_radius.all(
                        val["border_radius"]
                    )
                    self.keys[f"{key}"].expand = False

                if val["type"] == "IconButton":
                    self.keys[f"c1"].content = ft.Row()
                    try:
                        self.keys[f"{key}"] = self.keys[f"c1"].content.controls.append(
                            ft.TextButton()
                        )
                        print(self.keys[f"c1"].content)
                        # Update the properties of self.c1
                        self.keys[f"{key}"].width = val["width"]
                        self.keys[f"{key}"].height = val["height"]
                        # self.button.bgcolcolor"]
                        self.keys[f"{key}"].icon = ft.icons.COFFEE
                        self.keys[f"{key}"].text = val["text"]
                        self.keys[f"{key}"].opacity = val["opacity"]
                        self.keys[f"{key}"].expand = False
                    except Exception as e:
                        print(e)

    # def AddWidget(self, Control):
    #     pass