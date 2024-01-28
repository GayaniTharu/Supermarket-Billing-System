import tkinter as tk
from tkinter import messagebox, ttk

class SupermarketBillingSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Supermarket Billing System")

        # Styles
        style = ttk.Style()
        style.configure("TFrame", background="#E1F5FE")
        style.configure("TLabel", background="#E1F5FE", font=("Arial", 12))
        style.configure("TButton", background="#1565C0", foreground="white", font=("Arial", 12))
        style.configure("TCombobox", background="white", font=("Arial", 12))
        style.configure("TEntry", font=("Arial", 12))

        # Product database (Product ID: [Product Name, Price])
        self.products = {
            1: ["Bread", 2.5],
            2: ["Milk", 1.5],
            3: ["Eggs", 1.0],
            # Add more products as needed
        }

        # Dictionary to store selected items and quantities
        self.cart = {}

        # GUI components
        self.frame = ttk.Frame(root)
        self.frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        self.product_label = ttk.Label(self.frame, text="Select Product:")
        self.product_var = tk.StringVar()
        self.product_dropdown = ttk.Combobox(self.frame, textvariable=self.product_var, values=list(self.products.keys()), state="readonly")

        self.quantity_label = ttk.Label(self.frame, text="Enter Quantity:")
        self.quantity_entry = ttk.Entry(self.frame)

        self.add_to_cart_button = ttk.Button(self.frame, text="Add to Cart", command=self.add_to_cart)
        self.generate_receipt_button = ttk.Button(self.frame, text="Generate Receipt", command=self.generate_receipt)

        # Layout
        self.product_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.product_dropdown.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        self.quantity_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.quantity_entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
        self.add_to_cart_button.grid(row=2, column=0, columnspan=2, pady=10)
        self.generate_receipt_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Column weights for resizing
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)

    def add_to_cart(self):
        try:
            product_id = int(self.product_var.get())
            quantity = int(self.quantity_entry.get())

            if product_id in self.products:
                if product_id in self.cart:
                    self.cart[product_id] += quantity
                else:
                    self.cart[product_id] = quantity
                messagebox.showinfo("Added to Cart", f"Added {quantity} {self.products[product_id][0]} to the cart.")
            else:
                messagebox.showwarning("Invalid Product", "Please select a valid product.")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numeric values for quantity.")

    def generate_receipt(self):
        total_amount = 0
        receipt_text = "===== Supermarket Receipt =====\n"

        for product_id, quantity in self.cart.items():
            product_name, price = self.products[product_id]
            total_price = price * quantity
            receipt_text += f"{product_name} x {quantity}: ${total_price:.2f}\n"
            total_amount += total_price

        receipt_text += f"\nTotal Amount: ${total_amount:.2f}\n=============================="

        messagebox.showinfo("Receipt", receipt_text)
        self.clear_cart()

    def clear_cart(self):
        self.cart = {}
        self.product_var.set("")
        self.quantity_entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = SupermarketBillingSystem(root)
    root.mainloop()
