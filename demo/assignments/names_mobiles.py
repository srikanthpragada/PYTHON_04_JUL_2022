names = ['Andy', 'Mark', "Roger", 'David']
mobiles = ['393939333', '98577777', '8928874744', '98888222']

for idx, name in enumerate(names):
    print(f"{name:20} {mobiles[idx]}")

for name, mobile in zip(names, mobiles):
    print(f"{name:20} {mobile}")
