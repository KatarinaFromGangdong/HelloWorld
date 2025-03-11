import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title('Calculator')
        self.master.resizable(False, False)
        
        # Create Entry Widget to display the result
        self.result = tk.Entry(self.master, width=15, font=('Arial', 16), justify='right')
        self.result.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        
        # Create Buttons
        button_list = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        
        # Use a for loop to create and place the buttons
        r = 1
        c = 0
        for btn_text in button_list:
            btn = tk.Button(self.master, text=btn_text, width=3, font=('Arial', 16), command=lambda x=btn_text: self.click(x))
            btn.grid(row=r, column=c, padx=5, pady=5)
            c += 1
            if c > 3:
                c = 0
                r += 1
    
    # Define the click method for the buttons
    def click(self, key):
        if key == '=':
            result_str = self.result.get()
            try:
                result = eval(result_str)
                self.result.delete(0, tk.END)
                self.result.insert(tk.END, result)
            except:
                self.result.delete(0, tk.END)
                self.result.insert(tk.END, "Error")
        else:
            self.result.insert(tk.END, key)
    
# Create the main window
root = tk.Tk()

# Create an instance of the Calculator class
calc = Calculator(root)

# Start the main event loop
root.mainloop()