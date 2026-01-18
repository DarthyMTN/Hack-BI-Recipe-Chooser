# Hack BI Cooking Project
# The purpose of this program is to give the user a recipe based on the choices of given ingredients that they make

import customtkinter as ctk

# Documentation for customtkinter: https://customtkinter.tomschimansky.com/tutorial/grid-system
# Google Gemini - used for learning the customtkinter and deriving a few functions to make our program work: https://gemini.google.com/app

class RecipeApp(ctk.CTk):
    def __init__(self):
        ctk.set_window_scaling(1.0)
        super().__init__()
    
        self.geometry("800x500")
        self.title("Recipe Selector")

        #screen 1: Choosing the type of meal 
        self.home_frame = ctk.CTkFrame(self, fg_color="transparent")
        
        self.title_label = ctk.CTkLabel(self.home_frame, text="Recipe Selector", font=("Arial", 40, "bold"), text_color="white")
        self.title_label.grid(row=0, column=0, columnspan=2, padx=20, pady=20)
        
        self.subtitle = ctk.CTkLabel(self.home_frame, text="Choose your meal type",font=("Arial", 20), text_color="white")
        self.subtitle.grid(row=1, column=1, columnspan=1, padx=0, pady=5)

        self.btn_main = ctk.CTkButton(self.home_frame, text="Main", command=self.show_main_frame)
        self.btn_main.grid(row=2, column=1, padx=0, pady=5)
        
        self.btn_dessert = ctk.CTkButton(self.home_frame, text="Dessert", command=self.show_dessert_frame)
        self.btn_dessert.grid(row=3, column=1, padx=0, pady=5)
        

        #screen 2 : Choosing the meat, starch, and vegetable
        self.main_result = ctk.CTkFrame(self, fg_color="transparent")
        

        # display question for meat choice
        self.main_title = ctk.CTkLabel(self.main_result, text="What kind of meat would you like?", font=("Arial", 20, "bold"))
        self.main_title.pack(pady=20)

        # dropdown menu for meat options
        self.meat_options = ctk.CTkOptionMenu(
            self.main_result, 
            values=[" ", "Steak", "Chicken", "Fish", "Pork", "No meat"],
            command=self.update_main_choice # Calls the function when changed
        )
        self.meat_options.pack(pady=10)


        # display question for vegetable choice
        self.main_title = ctk.CTkLabel(self.main_result, text="What kind of vegetable would you like?", font=("Arial", 20, "bold"))
        self.main_title.pack(pady=20)

        # dropdown menu for vegetable options
        self.vegetable_options = ctk.CTkOptionMenu(
            self.main_result,
            values=[" ", "Leaves", "Greens", "Legumes"],
            command=self.update_main_choice
        )
        self.vegetable_options.pack(pady=10)


        # display question for starch choice
        self.main_title = ctk.CTkLabel(self.main_result, text="What kind of starch would you like?", font=("Arial", 20, "bold"))
        self.main_title.pack(pady=20)
        
        # dropdown menu for starch options
        self.starch_options = ctk.CTkOptionMenu(
            self.main_result,
            values=[" ", "Pasta", "Potatoes", "Rice"],
            command=self.update_main_choice
        )
        self.starch_options.pack(pady=10)

        # create empty textbox to show choices
        self.main_display = ctk.CTkLabel(self.main_result, text="", font=("Arial", 18))
        self.main_display.pack(pady=20)
        
        # create button to finalize choices
        self.btn_finalize = ctk.CTkButton(self.main_result, text="Confirm Main Choices", command=self.get_main_list)
        self.btn_finalize.pack(pady=20)



        #screen 3 : Choosing dessert types
        self.dessert_result = ctk.CTkFrame(self, fg_color="transparent")
        

        # display question for flavor choice
        self.main_title = ctk.CTkLabel(self.dessert_result, text="What kind of flavor dessert would you like?", font=("Arial", 20, "bold"))
        self.main_title.pack(pady=20)

        # dropdown menu for flavor options
        self.flavor_options = ctk.CTkOptionMenu(
            self.dessert_result,
            values=[" ", "Chocolate", "Fruity", "Plain"],
            command= self.update_dessert_choice
        )
        self.flavor_options.pack(pady=10)


        # display question for temperature choice
        self.main_title = ctk.CTkLabel(self.dessert_result, text="What temperature would you like your dessert to be?", font=("Arial", 20, "bold"))
        self.main_title.pack(pady=20)

        # dropdown menu for temperature options
        self.temp_options = ctk.CTkOptionMenu(
            self.dessert_result,
            values=[" ", "Hot", "Cold", "Room Temperature"],
            command= self.update_dessert_choice
        )
        self.temp_options.pack(pady=10)


        # display question for texture choice
        self.main_title = ctk.CTkLabel(self.dessert_result, text="What kind of texture would you like?", font=("Arial", 20, "bold"))
        self.main_title.pack(pady=20)

        # dropdown menu for texture options
        self.texture_options = ctk.CTkOptionMenu(
            self.dessert_result,
            values=[" ", "Soft", "Crunchy", "Chewy"],
            command= self.update_dessert_choice
        )
        self.texture_options.pack(pady=10)

        # create empty textbox to show choices
        self.dessert_display = ctk.CTkLabel(self.dessert_result, text="", font=("Arial", 18))
        self.dessert_display.pack(pady=20)

        # create button to confirm choices
        self.btn_finalize = ctk.CTkButton(self.dessert_result, text="Confirm Dessert Choices", command=self.get_dessert_list)
        self.btn_finalize.pack(pady=20)

        # Show the home frame on startup
        self.show_home()

        
    # function was derived from Google Gemini - switches frame based on the type of meal
    def show_home(self):
        self.main_result.pack_forget()  # Hide results
        self.dessert_result.pack_forget()  # Hide results
        self.home_frame.pack(expand=True, fill="both") # Show home


    # functions for displaying recipe choices - syntax copied from show_home function
    def show_main_frame(self):
        self.home_frame.pack_forget()   # Hide home
        self.main_result.pack(expand=True, fill="both")

    def show_dessert_frame(self):
        self.home_frame.pack_forget()
        self.dessert_result.pack(expand=True, fill="both")
    
    # functions for displaying recipe results
    def show_main_recipe(self):
        self.home_frame.pack_forget()
        self.main_choice.pack(expand=True, fill="both")
        self.main_recipe = ctk.CTkLabel(self.main_result, text="What kind of starch would you like?", font=("Arial", 20, "bold"))
        self.main_recipe.pack(pady=20)


    def show_dessert_recipe(self):
        self.home_frame.pack_forget()
        self.main_choice.pack(exoand=True, fill="both")
        self.dessert_recipe = ctk.CTkLabel(self.main_result, text="What kind of starch would you like?", font=("Arial", 20, "bold"))
        self.dessert_recipe.pack(pady=20)

    # update functions to gather data
    def update_dessert_choice(self, choice):
        self.dessert_display.configure(text=f"You selected: {choice} 🍨")

    def update_main_choice(self, choice):
        self.main_display.configure(text=f"You selected: {choice} 🍽️")

    def get_dessert_list(self):
        selected_dessert = [self.flavor_options.get(), self.temp_options.get(), self.texture_options.get()]
        self.show_dessert_recipe()
        print("Selected dessert choices:", selected_dessert)
        return selected_dessert
    
    def get_main_list(self):
        selected_mains = [self.vegetable_options.get(), self.meat_options.get(), self.starch_options.get()]
        self.show_main_recipe()
        print("Selected main choices:", selected_mains)
        return selected_mains
    

    # this function was derived from Google Gemini, but altered to fit our program
    # checks if the user's choices match any combination of dessert items in the text file
    def show_dessert_recipe(self):
        dessert_choices = [self.flavor_options.get(), self.temp_options.get(), self.texture_options.get()]
        selected_dessert = []
    
        with open("Hack BI Desserts Catalogue.txt", "r") as desserts:
            for dessert in desserts:

                columns = [item.strip() for item in dessert.split(",")]

                recipe_name=columns[0]
                recipe_traits=columns[1:4]

                if recipe_traits == dessert_choices:
                    print("true")
                    selected_dessert.append(recipe_name)

        final_dessert_recipe = selected_dessert[0]
        print("Matching dessert recipes:", selected_dessert)
        self.dessert_display.configure(text=f"You should make: {final_dessert_recipe}!")
        self.show_dessert_recipe()


    # checks if the user's choices match any combination of main items in the text file (syntax copied from previous function)
    def show_main_recipe(self):
        main_choices = [self.meat_options.get(), self.vegetable_options.get(), self.starch_options.get()]
        selected_main = []

        with open("Hack BI Mains Catalogue.txt", "r") as mains:
            for main in mains:

                columns = [item.strip() for item in main.split(",")]

                recipe_name=columns[0]
                recipe_traits=columns[1:4]

                if recipe_traits == main_choices:
                    print("true")
                    selected_main.append(recipe_name)

        final_main_recipe = selected_main[0]
        print("Matching main recipes:", selected_main)
        self.main_display.configure(text=f"You should make: {final_main_recipe}!")
        self.show_main_recipe()       

if __name__ == "__main__":
    app = RecipeApp()
    app.mainloop()

