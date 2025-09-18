import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from parking import Car, CarStatus, ManagerParking


car_list = ManagerParking().show_cars()


root = ttk.Window(title="Manage Parking", themename="cosmo")
root.geometry("1000x700")
root.resizable(False, False)


# main Frame
main_frame = ttk.Frame(root)
main_frame.pack(fill="both", expand=True, padx=10, pady=10)

# show cars frame
cars_frame = ttk.Frame(main_frame, bootstyle="light")
cars_frame.pack(side="left", fill="both", expand=True, padx=5, pady=5)

columns = ("plate", "budget", "arrival_time", "exit_time", "status")
tree = ttk.Treeview(main_frame, columns=columns,
                    show="headings", bootstyle="primary")
tree.pack(fill="both", expand=True, padx=10, pady=10)

tree.heading('plate', text="Plate")
tree.heading("budget", text="Budget")
tree.heading("arrival_time", text="Arrival")
tree.heading("exit_time", text="Exit")
tree.heading("status", text="Status")


tree.column("plate", width=200, anchor="center")
tree.column("budget", width=200, anchor="center")
tree.column("arrival_time", width=200, anchor="center")
tree.column("exit_time", width=200, anchor="center")
tree.column("status", width=200, anchor="center")


for car in car_list:
    tree.insert(
        "", END,
        values=(
            car["plate"],
            car["budget"],
            car["arrival_time"],
            car["exit_time"],
            car["status"]
        )
    )


# add new car or change status car frame
plate_frame = ttk.Frame(main_frame)
plate_frame.pack(side="bottom", fill="both", expand=True, padx=10, pady=10)


plate_label = ttk.Label(plate_frame, text="Enter Plate Number :")
plate_label.pack(side="left")

plate_car = ttk.Entry(plate_frame, bootstyle="primary")
plate_car.pack(side='left', padx=5, pady=5)


def parking():
    plate = plate_car.get().strip()
    car = Car(plate=plate)
    carStatus_obj = CarStatus(car).check_car()
    update_car_list = ManagerParking().show_cars()

    # update Tree view
    for item in tree.get_children():
        tree.delete(item)

    for car in update_car_list:
        tree.insert(
            "", END,
            values=(
                car["plate"],
                car["budget"],
                car["arrival_time"],
                car["exit_time"],
                car["status"]
            )
        )


check_btn = ttk.Button(plate_frame, text="Check Plate",
                       bootstyle="primary", command=parking)
check_btn.pack(side="left", padx=5, pady=5)


root.mainloop()
